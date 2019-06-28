# eggify
## Where to find eggify
click [HERE](http://eggventure.online/)

## What is eggify
This project is a collaboration between Samie Azad and Athena Deng for their portfolio project at the end of their foundation year at [Holberton School](https://www.holbertonschool.com/). It was designed to be the ultimate portfolio project: 
Athena using Django framework to build the backend web application, MySQL to store client data, HTML, CSS, and JavaScript for the frontend; 
and Samie deploying the web application in containers, using Kubernetes to manage the clusters, Puppet manifests to configure the containers, and PHP.

## What eggify does
When you have any non-egg (eggn't) content to share with a "only allowed to say egg" community, like a funny story or joke, sharing it just as it is will result in you getting removed from the community! That is where eggify swoops in to save the day, by helping you turn all of your words into "egg"! Now your story or joke or whatever is safe to share. A link is also provided, for friends who are in these communities but do not speak fluent egg, to view the original input. As a bonus, any digit in the input is replaced by "0" to make the output more egg-like.

## About us
**Samie**: [GitHub](https://github.com/sazad44) / [Twitter](https://twitter.com/AzadSamie) / [LinkedIn](https://www.linkedin.com/in/samieazad/)

_Samie's intro goes here?_

[**Athena**](https://ad-egg.github.io/): [GitHub](https://github.com/ad-egg) / [LinkedIn](https://www.linkedin.com/in/ad-egg/)

_Hi, my name is Athena and I like eggs, puns, and word games. I started studying at [Holberton School](https://www.holbertonschool.com/) and realized that I enjoy coding and how much I like eggs. I like them so much that I founded the public `egg` channel in our school Slack! Somewhere along the way I discovered there are corners of the internet where you are only allowed to say the word “egg” and other variations of it, and the idea for eggify was born. I wanted to make a web app that incorporated my love of egg and the concepts I learned at school. I am looking for a backend developer position so hire me please!_

## Features
- eggify input text 
- different languages output
- link to original input
- deployed in container 
- one click deploy/down

## How it works
**back end and front end:**

1. User visits eggify site
2. User inputs text
3. User clicks “eggify” button, which sends POST request
   
4. New object is created from user input and saved into database
5. User input is eggified to specified language
6. Eggified output sent to front end and displayed
7. Object id is sent to front end and appended to hostname and url
   
8. User can use top button to copy eggified out put to share with egg community, and use the bottom button to copy link to original input to share along with eggified output
9. Someone not fluent in egg visits link to someone's original input
   

**SRE stuff:**



## Challenges
- learning new frameworks/technologies: Django, HTML, CSS, JavaScript, Docker, PHP
- serving static files in production 

## How to deploy this code
* You must create an empty directory after cloning named `mysql`

## Future of eggify
- user accounts to store history
- support input languages other than English
- support emojis
- dark theme
- single page app
- CI/CD pipeline
- website is 100% accessible

If you have any good ideas for features, please contact Athena through [LinkedIn](https://www.linkedin.com/in/ad-egg/). For deployment ideas, please contact Samie through [Twitter](https://twitter.com/AzadSamie) or [LinkedIn](https://www.linkedin.com/in/samieazad/).

