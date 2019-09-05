        q_table[state,action] = (1-learning_rate)*q_table[state,action] + learning_rate*(reward_current_episode+discount_rate*(np.max(q_table[new_state,:])))
