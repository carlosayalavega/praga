import gym 
import numpy as np


env = gym.make('CartPole-v0')

best_weights = np.random.rand(4) * 2 - 1
best_reward = 0

for i in range(10000):
    
    s = env.reset()
    total_reward = 0
    
  
    for j in range(200):
        env.render()
      
        weights = np.random.rand(4) * 2 - 1

        a = 1 if np.matmul(weights, s)<0 else 0
        
        
        
        s1, r, d, _ = env.step(a)    
        total_reward +=r
        
        if d:
            print(best_reward)
            break
    if (total_reward >= best_reward):
        best_reward = total_reward
        best_weights = weights

print(best_reward)
env.close()        
