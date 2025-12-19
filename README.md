# Falsification_using_RL

All material related to the master thesis project 'Falsification using Reinforcement Learning' during spring 2022. Instructions on how to use the different folders below. 

## Prestudy_Falsification_RL 

This folder contains relevant papers and some other sources to start the prestudy phase of the project. The numbers in the subfolders indicate the recommended order of reading. The mandatory readings are marked in **bold font** below. The expected learning outcome is also outlined. 

### 1_Falsification

*Learning outcome*: Explain how optimization based falsification works and identify different components in an optimization based falsification framework. Understand the robustness function used in this framework so that you can follow the papers in the folder titled 3_RL_Falsification

- **Licentiate_JohanE**: **Mandatory reading only Chapter 3.** You can skip the other chapters for now. 
- Falsification_ACC_Matlab_Zahra: This paper evaluates two different semantics for the falsification of an ACC controller from the MATLAB toolbox. Currently, a design project aims to use the same example to falsify the ACC controller using RL. The report from the design project will be available before the start of the thesis project.
- Tutorial_Breach_DemoAFCmain: Breach is a Matlab toolbox for simulation-based design and falsification of cyber-physical systems. This document is a tutorial on how to get started with Breach. Breach can be found here: https://github.com/decyphir/breach

### 2_RL 

*Learning outcome*: Understand and be able to explain the different RL algorithms. Understand the difficulties and practical challenges that arise when you use RL to solve a problem. 

- **RL_Cheat_Sheet**: Mandatory reading.
- intro RL: Assignment from one of the courses at Chalmers. Constantin has specially modified the assignment for the context of this project. 😉  
- Some other material to read in this part include:
  - **Deep Reinforcement Learning Doesn't Work Yet**: Mandatory reading of the blog post https://www.alexirpan.com/2018/02/14/rl-hard.html
  - John Schulman's talk about the practical tips to consider when doing Deep RL: https://www.youtube.com/watch?v=8EcdaCk9KaQ and the slides to his talk http://joschu.net/docs/nuts-and-bolts.pdf
  - Bertsekas video lectures and other material from his course on RL: http://www.mit.edu/~dimitrib/RLbook.html

### 3_RL_Falsification

*Learning outcome*: Understand how existing research uses RL to falsify and/or test cyber-physical systems. Be able to explain the strengths in each method and highlight the differences to our proposed solution. Get inspiration to solve our problem.  

- **AST_RewardAugmentation_Stanford**: Mandatory reading. You have already read this during your preparation for our interview. 
- **AutomaticTesting_AdversarialAgents_Deshmukh**: Mandatory reading. You are not expected to write theorems and prove them in this project. Therefore you can skip Section IV. The first three sections in this paper and the two case studies in the end are recommended. 
- **Falsification_CPS_DeepRL_Yamagata**: Mandatory reading.
- MasterThesis_AnderssonKara_2021: Master thesis from spring 2021. The project uses RL to falsify a human-robot collaborative workstation. The project investigates different RL algorithms and provides insights. Will be a good reference during the course of your project. 
