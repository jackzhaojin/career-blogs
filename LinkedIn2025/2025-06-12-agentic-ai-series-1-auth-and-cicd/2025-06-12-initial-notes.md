# Cloud App Authentication Series

**User:** Jack Jin (jackzhaojin@gmail.com)  
**Created:** 6/12/2025 7:55  
**Updated:** 6/12/2025 17:23  
**Exported:** 6/12/2025 17:55  

## Prompt:
Maybe let’s do a start of a short article series that’s technical and full of diagrams and code samples. First one focused on authentication and authorization with cloud based apps and codex ai agent enablement. This blog should maybe give an intro of this series and mention will do less story and more code samples, screenshot and diagrams. Also URLs.

Most of the authentication is passwordless except for Codex that doesn’t support OCID yet and authorization RBAC in azure 

Maybe we’ll have the completed picture of the diagram as the intro picture.

After intro section, second section should be about enabling local agents to validate the code through az login. Password less 

Third section should be allowing cloud deployment, getting AI to do tests against azure Azure. Also build UI based integrated test harness.

4th section is also password authorization from GitHub to azure to restart server for full cicd after building GitHub image. So after AI generated or manual code changes are done, things are deployed a couple minute later.

5th should be about enabling newest AI agent Codex to use service principle to use Azure Servicrs to test. Stress on automation and Codex can now use my Azure storage account and AI foundary to validate its work.


6th section should be conclusion and tie it all together 
No response needed for now

## Response:
OK, got it

## Prompt:
Story blog intro theme story: 4th authentication and authorization pattern used for a simple for Agentic project with Azure

## Response:
OK, got it

## Prompt:
Theme should also stress on technical deep dive and step by step and not some of higher level stuff I’ve been doing

## Response:
OK, got it

## Prompt:
Okay, let's go section by section. So for the second section on local, let's focus on the importance for development to happen with Azure and being able to authenticate, however, not giving all the credentials. So the technique here is basically using my local credential with az-login, which gives my personal account a serverless password, not serverless, I'm sorry, passwordless login onto Azure, and if I do az-login, then typing npm run dev, it'll give my local dev server a way to access Azure with Azure CLI. And this is important to maybe show a diagram and then show some code snippets, why the local thing works, and then maybe enable to tell that, you know, the agents I'm using right now with this is GitHub Copilot, has full access to Azure Blob, as well as AI Foundry.

## Response:
OK, got it

## Prompt:
The third section should really be about Azure and Managed Identity, and then basically the thing working on Azure without a password either, and we're using best practice here with Azure and Managed Identity. This is so that Azure things can talk to each other, and work with each other, and give each other permissions with proper raw backup authorization by using Managed Identity. It's proven to be the best authorization capability within Azure and for services to identify themselves. In this case, I'm using an Azure web app, which is an Azure resource that's native. There's no enterprise applications or service principle that's needed here. Then this is working directly with my Azure storage account, which is similar to an S3, as well as my AI Foundry. Having this working, it's a pattern number 2. It allows for authorization into the storage accounts from the server stuff. This is probably the most baseline stuff, but it's important to have it working.

## Response:
OK, got it

## Prompt:
The third one is the authorization pattern between GitHub and then GitHub Action and then, you know, and GitHub and then Azure. This is important because I want to basically have GitHub Action compile my container, right, so it's deployable anywhere, so it's a really important step. And then the second step, right, is that my Azure web app is configured to use that container. However, right now Azure, at least the free plan that I'm using, we're a very low-cost plan, or free plan actually, that doesn't actually restart when the container is touched. So what I'm doing here is I'm using OpenID Connect, which is a pretty cool capability. Azure is one of the better cloud providers that enables it. So what's happening here is that Azure, you configure an enterprise application, and after that, you configure a service, not exactly a service potential, but another service principle. That kind of ties the permissions together, and then there, Azure will attach some screenshots for this, but Azure has a way to kind of have a drop-down configuration for me to figure out to kind of get this whole thing working. And then maybe a tip for the user here is that if you take a screenshot of your form and a screenshot of your GitHub branch that you're trying to do this passwordless capability in, Azure, GitHub, Copilot, and other AIs will figure out and tell you which form to type in if it's confusing.

## Response:
OK, got it

## Prompt:
Okay, and then the last section is probably my favorite one for the AI agents. I'm using OpenAI's codecs, right? And one of the biggest challenges with codecs is that it's brand new, right? It came out like two weeks ago for Plus users, maybe a month ago for Pro users. Here, the challenge is that codecs also need the same capability, right? You don't want a teammate or someone on your team, right, who can't test, right? And if the AI can't test, AI can't code. This is very important. So what I'm doing here is that because codecs doesn't quite support the more fancy OpenID Connect, we're going with still authorization, right? Still going with ABAC. I'm not giving them storage account keys. I'm not giving them OpenAI keys, right? That's not what I consider, you know, being a security-first-minded person, a proper way to give authorization. So instead, what I'm doing here is I'm using a service principle. And then, unfortunately, here, I am using a password into that service principle. However, the permissions are much more micro-controlled with Azure's role-based access control. So maybe let's have a diagram of how that's working all together. And then also, right, kind of talk about, you know, the basic secret-based authentication. And I'll add a screenshot with my OpenID showing how it's done. And maybe some pull requests with AI validating its work against Azure.

## Response:
OK, got it

## Prompt:
And then back to the narrative portion of my thoughts. So I'll kind of start this as personal, right? I'm not the Azure or this whole expert, but however, this is part of the journey of me using AI. And then the theme, the more I think about it, is enabling AI to have proper authorization, agents locally and on the cloud, and it's enabling all four of us, right? So think about it, there's four things that we're enabling. We're enabling local, we're enabling Azure, and then we're enabling GitHub Action, and then we're enabling codecs, all to have proper authorization. Maybe start the blog with being humble, right? I was always not the best at authorization. However, right throughout my career journey, I'm more focused on it. And now with AI, this whole thing can tie all together.

## Response:
OK, got it

## Prompt:
This is the NOT PART of the actual text content of the blog, but I was thinking that we would also have a way for kind of to show the main picture. Maybe each one will put together a different picture to add to it. Like, you know, you show the final picture, but each, you know, blog, we add one piece to it. So anyways, the final blog, I was thinking on the very left side, we have four actors, right? We have our local, then we have our Azure server, then we have our GitHub action, and then we have our, you know, password with codex, service principle. And then this is where the next level, right? I always think that we will use the Azure authentication method. The local will be using the default credential, using the local user context, right? And then both, however, this is something that's cool, that both the OpenID Connect, right, and GitHub action shared that service principle in a way that it's an enterprise application that we're enabling in Azure. So we show that. So both the GitHub action and as well as the, I'm sorry, as well as GitHub action, as well as the service principle that OpenID uses. So both of them are more through an enterprise application service principle pattern that Azure has. And then lastly, right, managed identities for Azure to Azure connectivity. And then all of them may be in the diagrams, really important to show that all of them has its own role-based access control in Azure. So that we're missing, we're using, you know, even for my front project, we're using very high security standards with, you know, very minute permission capabilities. And then lastly, right, we'll then kind of show that these role-based access controls, right, has access to both my storage account and AI Foundry. And then maybe do even show off even a little bit more, right? The storage accounts have, you know, have blob stores, right, for now, maybe queues later, but for now just blob stores. And then AI Foundry, right, show off that it's capable of enabling multiple AI models from all the vendors.

## Response:
OK, got it

## Prompt:
No respnose needed for now.

For local we should hae 2 personas called out, myself, github co pilot being separate actors

no response needed for now.

## Response:
OK, got it

## Prompt:
idea of title of the blog: Enabling Agentic AI agents with proper role based access control. should be engaging and focused on the technical nature of the blgo however approachable by a non techncial audience. Also ideally add in CICD / Dev Ops theme since it is important to get thigns setup automatically deploying as well.

No response needed for now.

2/2

## Response:
OK, got it

## Prompt:
OK we'll want an entro the series before entro the blog.

We're going to build a client public facing AI agent, without writing a single line of code oursleves. It's going to have a modern UI and no authentication required (however it'll remember you and let you download your work here before).

100% Ai coded code and test automation.

I will only do the following
1. Update markdown files this includes 
the product requirement document specification
agent instructions
project plan markdown mdc
2. Testing, I will test locally and on Azure, but will not directly change code or test automation code and configuration.
3. To keep the scope of this project reasonable, there is no IaC and I will configure azure and have AI help me document in infrastructure.md


I'll write about my journey as I learn about agentic programming, and ultimately if I keep going, we'll come to an ending of either success or failure.

## Response:
OK, got it

## Prompt:
First section will be blog series introduction.

OK so we'll have the following sections

1. Blog series introduction, focus on 100% agentic coding and what I'll do detailed above
2. Blog entry introduction, focus on the tileidea of title of the blog: Enabling Agentic AI agents with proper role based access control. should be engaging and focused on the technical nature of the blgo however approachable by a non techncial audience. Also ideally add in CICD / Dev Ops theme since it is important to get thigns setup automatically deploying as well. Make sure we'll have the theme of the blog entry defined as passwordless as possible with Azure ahtnetication
3. Local authorization, enables myself and github co pilot. Maybe claude desktop / cursor later on.
... Previous sections works.
As conclusion do not conlude the series, but mention how this is a very important step to have full CICD and enable both of my agents (local + Codex) to be able to validate its work.


## Response:
OK, got it