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

**Athena**: [GitHub](https://github.com/ad-egg) / [Twitter](https://twitter.com/CloudyCloak) / [LinkedIn](https://www.linkedin.com/in/ad-egg/)

_Hi, my name is Athena and I like eggs, puns, and word games. I started studying at [Holberton School](https://www.holbertonschool.com/) and realized that I enjoy coding and how much I like eggs. I like them so much that I founded the public `egg` channel in our school Slack! Somewhere along the way I discovered there are corners of the internet where you are only allowed to say the word “egg” and other variations of it, and the idea for eggify was born. I wanted to make a web app that incorporated my love of egg and the concepts I learned at school. I am looking for a backend developer position so hire me please!_

## Features
- eggify input text 
- different languages output
- link to original input
- deployed in container 
- one click deploy/down

## How it works
back end and front end:

1. User visits eggify site
2. User inputs text
3. User clicks “eggify” button, which sends POST request
   <img src="https://lh3.googleusercontent.com/Sy4hZr5H9mRDuhKCSnodGB6nHWNFyqvWGZ4o8J8nqb8KO6xKyu1OXst2hLZdOY9lvhkxUVRalycm71FOdtFuVbAP1-Ej0AIZP65ZwEg3CMV--V9Us6IRMJdI0lbo_qE_MpmEaLcA-Nut8Mq7D1DbNbLtUbPfluBw6OPDKp0pjIv_1pM3xNJ6wNyXVeo-eXZ0zFcVuYCRAo8GWp9r3hR3TyP58X9LdeTJBugMrJgplbSw7aPKIZ2Y3UppZ0lbbcJI_aF53O-SYNG8lPPcMhBKUBgM9koM37v-HW7UhoA2JWJKX8Gj5CMpkX2RUmiZRo4RzE6K_GAVn2vMWxYQITuhlCymGztc_MTzzsX-EGoLM_xH0pffNhshls5ryAdOv2-Z6zgwyk2xdzIJgPbt5Fl7wsnpVeN5tOBhNt_ZgB9_FBamQLnzwEUYMb1F1YWR8GhTTYUYn-7SlCmRin6GpOMLXRCLEdAp_cYG3i_ajT0gFspdZaQgp6Gt4Zb-c4OPbolk5OkouruzS7NsRgx22727WlyavjzOtDkBNzM3gpJgxMQnsbIJWa-KLCzNI6y2WTaSXCP2RzYsLHOVlaPgkSdvthJ5YEut-XY0k7alcNyNbvxQ3f6sE65sCPGTD9-P39ratRRxCPXsaOSMjlEs4cZfh-nZPa2SPg=w1756-h890-no" alt="user has input text and is ready to eggify">
4. New object is created from user input and saved into database
5. User input is eggified to specified language
6. Eggified output sent to front end and displayed
7. Object id is sent to front end and appended to hostname and url
   <img src="https://lh3.googleusercontent.com/Hy7cNaK2IgsUxJJFNWkwIIYNdTiRoz2MjkuVv9h-Jk0HhHEA5j_YXhOWSeufAmS8fECKhYkXwh-mg9FWIlR0OmAmuKEimO1ecSM3urXSLTfoP85eMCPTi-F58kjP50GNGiET7U3IqyGX66186B6RfzZZf6jud5MKPS4CrvHDBa9fVog-sVLn2uyYZNcu5GiWNYoLjuuFM4PTkhwo3bfCA59IucbaWErq2jG_DIfulaDFzgL9ueM9JXSo5xlnZ4ovC8REutruWsWRGV-vqGrSTkRDege1A7qLSVnnCffeaP5JqXCvnPL4SzwJF4w6SR-k7ac5PPvcRRvOlYwAQADo-tJPwLEpb81GUivFwtna2A6xiYmKMxb4vj57I4NWzBDUChbG5qtCyKB3shTGWo5vl9mWBpNrQ9kI5DDRfvusqXm6zBSWxtoCWoUPbkKcCEK_l8DWmbKfINP6ePdV4Ck1D-BXT80FzCbK6AFHyUDEyMAPclQuDv_pgEfaA9_S3jLWdQuILcdbgpSKe9mvNjAjM7gpGWNF21tquvGqyrzUi_WOrWriZ7Bou1nuSswGjbewR50AzxhldqgjUaSe5Yq3VhHLLbyzRPVuw0j03TSGBOIXwwwPBFqVzGastQgFyewSvGIJ6DmStqRfclX4sU9Pvf8ZKRYUqw=w1744-h1104-no" alt="eggified output with link to original input">
8. User can use top button to copy eggified out put to share with egg community, and use the bottom button to copy link to original input to share along with eggified output
9. Someone not fluent in egg visits link to someone's original input
   <img src="https://lh3.googleusercontent.com/H19YJ1Kfp23vgIUh_UkGOE4eYG-qIH2fyi6dBNW_CLb2YPNi3BPHyqGLS08VbuLw8G84Gco0n1r9cINP7WsGlFn62gkZnz3JIIfA6HtYEflRygNvulye2DnGLGh_bQbEUSELPyX_ZI0u8g4DS0vK5pATXKMICO_rK7_yG5jMcANvaDlr0k6-ot1gXweSEGJduS3VoT7xKW73Zz8Z8E7WPVbsrMmCKcsIdoiD7dU1i3rSZ5hwKq_aqaF0Xh_rv4wEeJ81V3Xq3iDXEraD1Hrlt7Or13Vr91JuchdWnNbHWEwGsFtNQdTzjQAxS698IS_LEG5TS6s3AeB8Q_WpCr09b3P-joeqGooVOyAv1SlKkd2NYktThLBMT2jDYSM3oBO6c3vBRrdED0PevcAl76JbWsIzuCAcopzpe0EyH8p_mpiPdGIt2IzWIT9uZQUPxPU_V4gBu5EoIy5auZ0QaXgfIXh2fbD-jPe49aeuRvFmJR1FygHz7t-a9rEiJVngFFfo8t9Ak7u3KKM_SYEpi9OpsNjf8Q9Y-MIQhuZ4Ksuo-cypAyowGuBzAYH0QUyxreTBkquAs-ZYSc9QdRR3GKTa6ppC8KHgUg_Qm3Fd9-cVtM8TzMq-dw4uaIBoThAUbvHsyrkc6EdvYkyh7pD5OwFO1a7knO0hAA=w1740-h714-no" alt="original input is displayed">

SRE stuff:


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

If you have any good ideas for features, please contact Athena through [Twitter](https://twitter.com/CloudyCloak) or [LinkedIn](https://www.linkedin.com/in/ad-egg/). For deployment ideas, please contact Samie through [Twitter](https://twitter.com/AzadSamie) or [LinkedIn](https://www.linkedin.com/in/samieazad/).
