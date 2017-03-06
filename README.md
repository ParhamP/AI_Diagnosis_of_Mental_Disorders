# AI_Diagnosis_of_Mental_Disorders
Artificial Intelligent Diagnosis of Mental Disorders based on "Diagnostic and Statistical Manual of Mental Disorders" (DSM-5)

## Under Development!

## Inspiration

While studying "Diagnostic and Statistical Manual of Mental Disorders", I became inspired to use it as my big data and extract useful information from it using machine learning in order to give computers an early chance to diagnose mental disorders based on patients' symptoms. 

## What it does

It's an interactive AI that listens to patients talking about their mental condition and tries to communicate with them in order to narrow down the diagnosis.

## How I built it

I extracted the text of DSM-5 which is a thousand page manual with mental disorders and their signs and symptoms. I then used that text as my data and tried to get insights from it using some data wrangling and regex. All mental disorders then get classified and a separate module is built for each of them so that we can use them. We then use Microsoft cognitive Services Academic Knowledge API to find out the cosine similarity between each of classified mental disorders and the symptoms of the patient that we have listened to. Each mental disorder gets a point based on the number of the similarity was found. We take the two most probable mental disorders and also use Microsoft Cognitive Services Text Analytics on them to make our diagnosis more accurate. After this we ask the user manually crafted question based on the exact signs of the mental disorder given in the manual in order to narrow down the diagnosis.

## Challenges I ran into

Working with big data, data wrangling and natural language understanding by the AI. 

## What's next for Artificial Intelligent Diagnosis of Mental Disorders

Improve the performance and polish the code. 