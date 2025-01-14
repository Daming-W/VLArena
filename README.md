# VLArena: Integrating End-to-End Multimodal Models with Closed-loop Generative Simulation for Autonomous Driving

## Abstract 📄

VLArena integrates the End-to-End Multimodal Model for Autonomous Driving (EMMA) with the DriveArena simulation platform to advance autonomous driving research. By combining EMMA's capability to process raw sensor data into driving-specific outputs with DriveArena's high-fidelity, closed-loop simulation environment, VLArena enables the development and evaluation of autonomous driving agents in realistic and interactive scenarios. Additionally, this project has open-sourced a Chain-of-Thought (CoT) data auto-labeling pipeline tool, streamlining the annotation process for complex datasets. This integration facilitates comprehensive testing and refinement of autonomous driving models, promoting safer and more efficient autonomous vehicle technologies. 

## Table of Contents 📚

- [VLArena: Integrating End-to-End Multimodal Models with Closed-loop Generative Simulation for Autonomous Driving](#vlarena-integrating-end-to-end-multimodal-models-with-closed-loop-generative-simulation-for-autonomous-driving)
  - [Abstract 📄](#abstract-)
  - [Table of Contents 📚](#table-of-contents-)
  - [Demo and Key Results 🎯](#demo-and-key-results-)
  - [VLArena Overview 🏎️](#vlarena-overview-️)
  - [Auto-Labeling Pipeline 🔖](#auto-labeling-pipeline-)
  - [VLM for Autonomous Driving 🚗](#vlm-for-autonomous-driving-)
  - [DriveArena Platform 🛠️](#drivearena-platform-️)
  - [Acknowledgement 🙏](#acknowledgement-)

## Demo and Key Results 🎯

Showcase demonstration videos, screenshots, and highlight the key outcomes of the project.

## VLArena Overview 🏎️

Provide a detailed description of VLArena's architecture, functionalities, and features.

## Auto-Labeling Pipeline 🔖

Describe the process, tools, and methods used for data auto-labeling.

## VLM for Autonomous Driving 🚗

The driving agent in VLArena is designed to leverage Multimodal Large Language Models (MLLMs) to process complex visual data and reason about driving scenarios, enabling efficient and effective autonomous driving. Specifically, we have replicated the core functionality of closed-source models like EMMA from Waymo.

This project is developed based on LLaMA-Factory and uses various open-source pre-trained VLM solutions, such as Qwen2VL and LLaVA. Through the Chain-of-Thought (CoT) reasoning process, the agent generates detailed object descriptions, behavioral insights, and meta-driving decisions. It directly infers the necessary context required by the model to generate waypoints.

## DriveArena Platform 🛠️

Introduce the functionalities of DriveArena, how to use it, and its role within the project.

## Acknowledgement 🙏

Express gratitude to individuals or organizations that provided support during the project's development.
