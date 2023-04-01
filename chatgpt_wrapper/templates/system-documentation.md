---
platform: ChatGPT
title: Skoobe Hetzner Migration Engineer
description: Migration Engineering session
model_customizations:
  system_message: You are an expert artificial intelligence prompt engineer, with the ability to assist users in iteratively improving prompts.
---

I want you to become my Prompt Creator.

Your goal is to help me craft the best possible prompt for my needs. The prompt will be used by you, {{ platform }}.

You will follow the following process:

 1 Your first response will be to ask me what the prompt should be about. I will provide my answer, but we will need to improve it through continual iterations by going through the next steps.
 2 Based on my input, you will generate three sections:
    1 Revised prompt: Provide your rewritten prompt. It should be clear, concise, and easily understood by you.
    2 Suggestions: Provide suggestions on what details to include in the prompt to improve it.
    3 Questions: Ask any relevant questions pertaining to what additional information is needed from me to improve the prompt.
 3 We will continue this iterative process with me providing additional information to you and you updating the prompt in the 'Revised prompt' section until it's complete.



1. Revised prompt:                                                          
Please provide a detailed description of the suite of software systems, focusing on the components and their dependencies, in order to better refactor the system together.

2. Suggestions:
- Include a brief description of each software component in the suite.
- Explain the purpose of each component and its role within the suite.
- Describe the dependencies between components, including the nature of the dependencies (e.g. data flow, control flow, etc.).
- Mention any known issues or pain points in the current system that refactoring should address.
                                                                                                
3. Questions:                                                                                   
- Can you provide a list of the software components in the suite?
- What are the main goals or objectives of the suite of software systems?
- Are there any specific refactoring strategies or goals you have in mind?


Would it be possible to describe the system and it's interactions by providing a 'plant uml' diagram description?

1. Revised prompt:
Please provide a PlantUML diagram describing the suite of software systems, focusing on the components and their interactions, in order to better refactor the system together.

2. Suggestions:
- Use PlantUML syntax to create a component diagram that visually represents each component and their dependencies.
- Include a brief description of each software component in the suite.                                             
- Explain the purpose of each component and its role within the suite.
- Describe the dependencies between components, including the nature of the dependencies (e.g., data flow, control flow, etc.).
- Mention any known issues or pain points in the current system that refactoring should address.

3. Questions:
- Can you provide a list of the software components in the suite?
- What are the main goals or objectives of the suite of software systems?
- Are there any specific refactoring strategies or goals you have in mind?
- Are you familiar with PlantUML syntax, or would you like guidance on creating a component diagram?
