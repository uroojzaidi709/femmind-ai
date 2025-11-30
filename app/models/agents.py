import google.generativeai as genai
import os
import json

class WellnessAgents:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")
        self.agents = {
            'wellness': {
                'name': 'Wellness Coach',
                'instruction': """
                You are a holistic wellness coach specializing in women's health.
                Provide balanced advice on general wellness, lifestyle, and healthy habits.
                Be supportive, practical, and evidence-based.
                """
            },
            'nutrition': {
                'name': 'Nutrition Expert',
                'instruction': """
                You are a nutrition specialist for women's health.
                Focus on balanced diets, meal planning, and nutritional needs specific to women.
                Consider different life stages like pregnancy, menopause, etc.
                """
            },
            'fitness': {
                'name': 'Fitness Trainer',
                'instruction': """
                You are a women's fitness expert.
                Provide safe exercise recommendations, workout plans, and fitness guidance.
                Consider different fitness levels and health conditions.
                """
            },
            'mental_health': {
                'name': 'Mental Health Supporter',
                'instruction': """
                You are a mental health supporter for women.
                Provide emotional support, stress management techniques, and mindfulness advice.
                Be empathetic and always recommend professional help for serious concerns.
                """
            },
            'reproductive': {
                'name': 'Reproductive Health Advisor',
                'instruction': """
                You are a reproductive health advisor.
                Provide information on menstrual health, fertility, pregnancy, and women's health topics.
                Be professional, sensitive, and evidence-based.
                """
            }
        }
        print("✅ Multi-agent system created with 5 specialized agents!")

    def get_agent_response(self, agent_name, user_message):
        if agent_name not in self.agents:
            return "Agent not available."
        agent = self.agents[agent_name]
        prompt = f"""
        {agent['instruction']}

        User Question: {user_message}

        Please respond as {agent['name']}:
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Sorry, I'm having trouble responding. Please try again."

    def select_agents_for_query(self, user_message):
        message_lower = user_message.lower()
        selected_agents = ['wellness']
        keyword_map = {
            'nutrition': ['food', 'diet', 'nutrition', 'eat', 'meal', 'weight', 'calorie', 'protein'],
            'fitness': ['exercise', 'workout', 'fitness', 'run', 'walk', 'gym', 'yoga', 'cardio'],
            'mental_health': ['stress', 'anxiety', 'mental', 'mood', 'emotional', 'depress', 'worry'],
            'reproductive': ['period','menstrual','pregnancy','fertility','cycle','ovulation','pms']
        }
        for agent, keywords in keyword_map.items():
            if any(keyword in message_lower for keyword in keywords):
                selected_agents.append(agent)
        return selected_agents

class AgentCoordinator:
    def __init__(self, agents, memory):
        self.agents = agents
        self.memory = memory
        self.model = genai.GenerativeModel('gemini-pro')
        print("🤖 Agent coordinator ready!")

    def process_query(self, user_id, user_message):
        print(f"👤 User asked: {user_message}")
        selected_agents = self.agents.select_agents_for_query(user_message)
        print(f"🤖 Using agents: {selected_agents}")
        all_responses = {}
        for agent_name in selected_agents:
            answer = self.agents.get_agent_response(agent_name, user_message)
            all_responses[agent_name] = answer
        if len(selected_agents) == 1:
            final_answer = list(all_responses.values())[0]
        else:
            final_answer = self.combine_answers(user_message, all_responses)
        self.memory.log_interaction(user_id, user_message, final_answer, selected_agents)
        return {
            'response': final_answer,
            'agents_used': selected_agents,
            'agent_count': len(selected_agents)
        }

    def combine_answers(self, question, responses):
        prompt = f"""
        Question: {question}

        Expert Answers:
        {json.dumps(responses, indent=2)}

        Combine these into one helpful answer:
        """
        try:
            result = self.model.generate_content(prompt)
            return result.text
        except:
            combined = "Expert advice:\n"
            for expert, advice in responses.items():
                combined += f"\n{expert}: {advice}\n"
            return combined

