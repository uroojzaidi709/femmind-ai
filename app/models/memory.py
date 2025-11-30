import pandas as pd
import numpy as np
from datetime import datetime

class MemorySystem:
    def __init__(self):
        self.sessions = {}
        self.conversations_df = pd.DataFrame()
        self.wellness_metrics_df = pd.DataFrame()
        print("✅ Memory system with Pandas/NumPy initialized")

    def create_session(self, user_id):
        self.sessions[user_id] = {
            'created_at': datetime.now(),
            'interaction_count': 0,
            'preferences': {}
        }

    def log_interaction(self, user_id, user_message, ai_response, agents_used):
        if user_id not in self.sessions:
            self.create_session(user_id)
        new_row = {
            'user_id': user_id,
            'timestamp': datetime.now(),
            'user_message': user_message[:100],
            'ai_response_length': len(ai_response),
            'agents_used': ','.join(agents_used),
            'agent_count': len(agents_used)
        }
        new_df = pd.DataFrame([new_row])
        if self.conversations_df.empty:
            self.conversations_df = new_df
        else:
            self.conversations_df = pd.concat([self.conversations_df, new_df], ignore_index=True)
        self.sessions[user_id]['interaction_count'] += 1

    def add_wellness_metric(self, user_id, metric_type, value):
        new_metric = {
            'user_id': user_id,
            'timestamp': datetime.now(),
            'metric_type': metric_type,
            'value': value
        }
        new_df = pd.DataFrame([new_metric])
        if self.wellness_metrics_df.empty:
            self.wellness_metrics_df = new_df
        else:
            self.wellness_metrics_df = pd.concat([self.wellness_metrics_df, new_df], ignore_index=True)

    def get_user_analytics(self, user_id):
        if user_id not in self.sessions:
            return {"error": "User not found"}
        if self.conversations_df.empty:
            return {"message": "No conversation data yet"}
        user_data = self.conversations_df[self.conversations_df['user_id'] == user_id]
        analytics = {
            'basic_stats': {
                'total_interactions': len(user_data),
                'first_interaction': user_data['timestamp'].min() if not user_data.empty else 'None',
                'last_interaction': user_data['timestamp'].max() if not user_data.empty else 'None'
            },
            'agent_analysis': self._analyze_agent_usage(user_data),
            'wellness_trends': {"message": "No wellness metrics yet"}
        }
        return analytics

    def _analyze_agent_usage(self, user_data):
        if user_data.empty:
            return {}
        all_agents = []
        for agents in user_data['agents_used']:
            all_agents.extend(agents.split(','))
        agent_series = pd.Series(all_agents)
        agent_counts = agent_series.value_counts().to_dict()
        response_lengths = user_data['ai_response_length'].values
        stats = {
            'most_used_agents': agent_counts,
            'avg_response_length': np.mean(response_lengths) if len(response_lengths) > 0 else 0,
            'max_response_length': np.max(response_lengths) if len(response_lengths) > 0 else 0,
            'total_agents_used': len(agent_counts)
        }
        return stats

