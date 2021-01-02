# MaskMandator

## Repository no longer in use: [New link](https://github.com/Mask-Mandator)

## [Hackathon submission for HackRPI 2020](https://devpost.com/software/mask-mandator?ref_content=user-portfolio&ref_feature=in_progress)

Awards won:
- 2nd Place FCA AI Best Hack
- Google Cloud COVID-19 Response Hack Finalists 
- Google Cloud COVID-19 1st Place
- Top 15 Teams By Wolfram


## Inspiration
Mask Mandator is inspired by the ever increasing threat of the Sars-CoV-2 pandemic. Despite America consistently breaking top COVID infection statistics, there are still many people who do not follow simple guidelines for safety. Seeing those people without masks on our campus makes us feel quite uncomfortable, and we wished that there were more guidelines in place. Our desire to aid in the fight against the pandemic and protect people inspired us to launch this project.

## What it does
Mask Mandator is a campus-wide system that enforces the proper usage of masks before entry into common areas and other population dense buildings. Our idea is to combine already widely used card/ID systems with cameras and AI to detect if someone is properly protecting themselves and others by wearing a mask before entering. The system would check with a cloud hosted data base to match students IDs with data such as if they're immunocompromised and the number of mask infractions they've had in the past and act accordingly to grant or reject the student access. 

## How we built it
Unfortunately, implementing a campus-wide system without our University's permission wasn't possible within 24 hours. As a proof of concept, we made a web application to act as a "door" and we used QR codes to act as some sort of ID or card swipe. 

Our webapp was built using Flask, JavaScript, HTML, CSS, and Python. We were able to take a photo of the user using webcams and we then processed that data using Python. To detect and read the QR code in the image, we utilized Google Vision API to find the bounds of the QR code and OpenCV2 to process the QR code to get an ID out of it. Once we got the user's ID, we were able to query data from an IBM Cloudant database, where we made up some fake data to simulate different students. We also used a trained a Google Vision AutoML model with 3k pieces of labeled data to identify if the student has a mask on or not with 99.73% accuracy. We used the aforementioned data to decide whether or not to let the student into the room.

## Challenges we ran into
- Properly reading the QR code + face from a single image
- Managing API keys with GitHub to ensure no leakage (thanks .gitignore!)
- Training a brand new AI model took some trial and error
- Integration between a frontend domain and maintaining project structure
- Deploying the webapp using Firebase and Flask proved to be extremely difficult

## Accomplishments that we are proud of
- Proud that we were able to combine a bunch of extremely powerful 3rd party systems to create this project, this isn't something any of us are experienced in
- Learned how to utilize Google Cloud services
- Able to pull ourselves together to do this right after midterm week

## What I learned
**Arjun**: I really wanted to ensure that our project at HackRPI was both challenging implementation-wise and useful. Working with mostly the frontend and webserver/backend integration, I increased my knowledge in Flask by integrating it with Firebase, as well as more about HTTP requests and handling using python. I also attempted to implement a custom .xyz domain, however, this was not used. Nonetheless, I learned the process of managing a domain and connecting with web hosting services. I gained an introduction to Node.js frameworks and JQueries.


**Bryan**: I learned some the basic components of Google Vision API and Google AutoML API, as well as how to train AutoML with large data sets.


**Jacob**: I gained so much experience trying to utilize Google Cloud services and IBM's database services. I think the most exciting part of this project for me was seeing how easy it was to utilize Google's AutoML service to create a custom classifier. AI has always been intimidating to me, but I learned it's an extremely easy tool to use with the right services!


**Jeongbin**: I was able to glimpse quite a bit of how some of the models of AIIs were trained and employed. I learned a bit of more python and flask. Also, now I understand that how comfortable tool those ApIs are.

## What's next for Mask Mandator
- Enhance the precision of detection
- Finish deploying online
- Differentiate between full mask coverage and partial coverage
- Add detailed instructions, that describe to the user how to adjust their mask
- Add ID card compatibility, and utilize idea in public with a Raspberry Pi
