# virtual-ai-code

## Inspiration
Many people worldwide suffer from skin conditions that negatively impact their mental and physical well-being. They often resort to taking dangerous medications to treat the symptoms without addressing the root causes. Skeen aims to change that.

## What it does
Skeen is an app that detects skin conditions from user-uploaded pictures, analyzes the user’s lifestyle and habits to identify potential causes, and provides suggestions for remedying the problem. Additionally, Skeen features an AI Assistant chatbot for skincare, powered by the GPT-3.5 Turbo model, that can answer all questions related to skincare.

## How we built it
We trained a TensorFlow convolutional neural network using data from DermNet NZ, the world’s leading online resource for skin-related information. This network classifies images of skin conditions. We then used Terra’s API to collect user data from all health applications and devices that the user granted access to, in order to pinpoint potential causes such as nutrition and dietary issues, sleep problems, and stress. We also developed an AI chatbot using the GPT-3.5 Turbo model to provide users with personalized skincare advice.

## Challenges we ran into
Artificial intelligence is not widely used in the skin health sector, making it ripe for innovation. However, datasets are not open-source, so we relied on DermNet as the most complete and reliable dermatology dataset. We also used data augmentation and pre-processing techniques to improve model accuracy.

## Accomplishments that we’re proud of
We are proud of our model’s ability to detect 23 skin conditions with good accuracy. Additionally, our data analytics demonstrate the feasibility of using health data from apps and devices to identify users’ bad habits that may be contributing to their skin problems. We are also proud of our AI chatbot, which provides users with personalized skincare advice.

## What’s next for SKEEN
We plan to expand our solution to address more health-related concerns and identify more potential causes from users’ lifestyles.
