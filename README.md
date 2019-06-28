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

![user has entered text and is ready to eggify the input](https://lh3.googleusercontent.com/RTS6w9_UysOJzgq8zlE9XsGCylYSEBvy3QXQhXdqebcERwie1vPUFwFX9XwdU3xmpdVDGzOyVO7T6MbNYu7-LkQ03kUaWx5HjtCSIHveLz3kgcQv5ZNlopAzE81zLO9kDkNNWmGUx1JBRUWGi00qoz2n88C2zOY7kBXuYDqM8vdk9xNqtj6DYxXJ8-HIyIeEox7E2DqKajnzjBYws8d5lcpF681fzeK2wvLe9C7LMBKlAwgvnAwp6rib7ze5H54FgKoeV5ZHaEXcfT-E9VfBJxfHx31XCa8bytX5ApYKAyTqEIRyC_QUy4O7qTEPPkITuM8yObiW0V-T3AoYdpdjNA1IB5RD20MSa2EGJ_88EhVGgT_1_jpXI_yk4tUEg2iz7-GwAhN8pXaiz4zm2D788Zt5jTJU6NDG9bWe3OCjfQ44JjWxd12eRtYHHOmdIVuQ5lGYRV_wX06i-cN50met7vHH5nvIvmxugdb5x8qiPrHH5gyEOB0gFL0xdPUbKXX3xZPl3b0DA-encWINktIdCGv5Td79hxBhE-p2vw6HDoMg8O5EpyBqY_eE6Ivblf30V_JVnS60qBxHrTfzThti7kP1HD1Tgye_ev01DE3_d9xXZQlHiQutEHiD64fSoWwArsLR5WxrixB6GDnM9klSndn9Rn9fYw=w1756-h890-no)

4. New object is created from user input and saved into database
5. User input is eggified to specified language
6. Eggified output sent to front end and displayed
7. Object id is sent to front end and appended to hostname and url

![eggified output is displayed along with a link for the original input](https://lh3.googleusercontent.com/E3074WkxLBR6NgR91OGd67cBTy13QJ4DOWvXgSBzdrEJKsBx2zPF9F0NiyarfKL8n0x2dLWaVAmkmIcBRj9xYowTdjqjPYHj6oR6wZADml8EKvlpp9lco7Bmi3Vr6pFZJeY1F8hnryGvyYdGdnOr0NFfz3KoM_E4mkza2s8oUcM3eVIe3iVTgReLQ-d0aUxpNi9Wc8T3BqHuk63q13yK006zlYp6pszUiEBwNKGf5iNacfCZx-ACLlRu_XmzrJHHpfebNxWFIitj13s83TUluAOIMiweIV0ZWnDaPUrSroMyE2-u7_sv4z7j8u_7BucA2TZFOhsrRETzCZAbNT1kfyQAZC5iEoVzZLxEAWomIKdvZ0FCzL-_A59H6x0x1DbmhQ9rIMSVKpM3hbUtPgoxdbvQ75qM1OqHd4a6vAu8jw7BPjmFLMoUt348_k8kPXsgGKoPRJvpqUIFzDXgnMiaB1INVvhiZVor76nkWn8sJv-YKKYN2cisDbNJ_P_FYT_CLgZMt-BfcHo2hQUoTfrdvJ3mmw-bUG_IiOFN6770jdPBhaGD4WFGmZf9dpv7KTeyperYzfIvNjArvlbIlRrq9LP1mkn-OnHwXYHHufsyGHS-VAF1Rw3qmJr4LNQn8x2O7PNlmPbVANKaDsAvf9hHjPV4PmLFKQ=w1744-h1104-no)

8. User can use top button to copy eggified out put to share with egg community, and use the bottom button to copy link to original input to share along with eggified output
9. Someone not fluent in egg visits link to someone's original input

![user can see original input](https://lh3.googleusercontent.com/2bqnnp8eSBL-byMlWwJ-1fQIRCR2zbha7pw4BgER5BDwxG4TXPXd3xtpaRtpWn_TMv5JLySUdoWODpc82RVXRs7whoOyFMe_clRZ8cFJwNfc35OjJLRI9o4DmWKzIpSF0AUFWBeN0B54Ah8Mywc44sBu0vR3BNH73pPyj73iXTjXE7r-Gh1LI1orKGRa_MJBYdilwUGMtAxd6FmLm9cwIIBxCx-dtrmNfUqXWIjXc5pdassS48u38V0SCFoPbsWytFIf7KWufgBXljvhaDgvZ31zX1ZId8n0hpbWh1zB2HNF_CVsQEdc0FkrzQqRhIZPbwShlbRZWmAxluk0qUYYK45EpQq4blhldcwBNx8LSvpei6sUn9EcKynHeRKLHTb20mxvWxAsoTwPlP7FFk0M0H_Ay0UqO--x763gTrdPnu2CjcKDpO8vm3qgXXV4v9q2kOvj93GCQegZ-jkv8X1e3FAjhw4FWmgcGyi4SuYONT99UDoGGQW8G99frYssHZGKf2vvd2YOdC1U0nKqnPfQxp3lW6b6EDJmR4wGJwp1SVQT53bHSx_QhzR3eDG4EMEavXgevIMBcoAxUeXB3OFtlF5aLg0A2UJLm2G4EXU4NPWIQPAMkQYTK9kJCdGY1hRWcyKkMPh_94spiDR49a76LqlVi5FjsQ=w1740-h714-no)

**SRE stuff:**

![developer's portal with DEPLOY, PROVISION, PP_INSTALL, DOWN buttons](https://lh3.googleusercontent.com/ZNjWXh9ANFc32fZdozQhAsC98wKXnngYMEy9OO8ux27NWBzKskCBVXYSHjnnbLHbdxympoI8YpL8oSai8z9vvJbrXwFAPTVzt3SjTIJPp84KNRRx0FIZGWWAbEu9YJyG-ZscqlmI891weFSVMPxs7ClTCNI2wiLZ5onyWKEVFyZ8dfCPtWkdlgmL68tArBvwD2gzfl3cx2013qDE2ByyFwYl9L5ZKUk7arJ1m413Gvq7aKKOse2PNy5tghd2j1Idn1wh6J8HprNcSHWmwR9g-H8zfqVDy9TM5BMCEaF1m3QkCMpi3ZaNb7L8juUproW5F3sdV9FNYTR5zja3wCKqTQe5yWZsWKCOqs4tltQxY3gkBEPQwdw5nN5E2_pBF80y2pMb9ROApW1fGjLg6ChXfanKw9prsAcymJg9ghbv_9WAfN1Kqyl6O4zY8gRNo2ZNtCjXi00ieflg2jExIICRnZqGFJB295hDS8ucUa6Af72MedG2bRD6q06KdjUFQ3L-TnldeCC1ryOAqjFpJWiy6yNcoDEY1pLiBhB3PYH-JqyD72Jl3rg5XhLQIKvdz9NTkbsyONEm7V3pQW34EyxjxwLaJtKHVbp1tyLRKxqWZ90KFSKWkOPCLRyiKvtJkutu-ZyqPZnw5cIjcIcG1Ph1il4X-JjNOQ=w1186-h446-no)

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
