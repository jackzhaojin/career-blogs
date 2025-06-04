# Making Sense of 7 AEM Capabilities: Tradeoffs, Narratives, and Why It Matters

Before we dive in, this series of AEM blog posts will use fictitious language to protect my current and past clients. Instead of saying "we did this x times", I'll choose to say "it's possible to do this". For client protection, maybe from time to time, I might be making things up, but this should be rare.

---

### Part 1: What the Situation Could Be

When consulting companies go to market, we pick a few of these to bring to customers. Some because the customer asked for it. At best, we take what we think is best for our customers. At worst, we focus on what we can execute on.

All of these options will not make it to any one single sales slide, I would imagine, from Adobe or any consulting firm. Capturing opportunities is about storytelling and narrative building. This slide, if shown out of context, will distract and confuse.

If Adobe had a workshop and decided EDS, service providers will bring EDS stories. If a long-time consulting team decided on headless CMS, then headless CMS will be the focus of storytelling from Adobe.

At best, consulting firms have the breadth to bring the best solution to the client. Leaner Adobe consulting partners may have to bring what they know or what they have staffing for.

To me, the big picture of all Adobe offerings is often lost in the process. However, seeing this landscape helps my technical brain. And hopefully, it’ll help you as well, without reading a 20 page readout.

---

### Part 2: Approach and Implementation Journey

#### Section 1: Comparing the Landscape

(Insert both tables from `Main-Comparison.md` here, covering Functional/Authoring/End User Experience and Technical/Infrastructure/Analytics)

These tables provide a snapshot of how the seven major AEM platform variations stack up. They range from traditional AEM 6.5 to full-on Edge Delivery Services, with multiple hybrid models in between. Each has tradeoffs across authoring experience, delivery model, backend extensibility, and real-world publishing speed.

#### Section 2: Generally Aligned Adobe Perspectives

* Universal Editor is no longer experimental. When properly instrumented, it's capable of in-context editing for everything from page content to experience fragments.
* `.model.json` is still foundational for Sites and SPA use. Developers must define content models carefully to support authoring and preview.
* Document-based authoring in EDS is fast, scalable, and predictable. It doesn’t support personalization or omnichannel out of the box, but it offers the lowest friction for publishing.
* EDS in general shifting from disabling server side rendered content to server side compile time generated capabilities cached at edge side is what makes edge go fast
* GraphQL and persisted queries represent the direction Adobe is pushing headless CMS. They allow structure, cacheability, and security.
* Most developers underestimate the effort to fully enable UE. It’s not just a toggle. It's a dev workflow shift of having front end friends build dialogs and maybe even model definitions.

#### Section 3: My Spicier Takes, Not Aligned with Anyone

* EDS lacks editable templates. That’s a non-starter for teams expecting full author control. This is by design. Layout lives in the boilerplate.
* Sites/Page with UE is a confusing middle-ground. You get in-context editing, but only if your `.model.json` and instrumentation are airtight. Or you can try and use .infinity.json as seen in [https://ue-remote-app.adobe.net](https://ue-remote-app.adobe.net), which is also as confusing.
* Headless CF + UE has strong omnichannel story but can be overkill if you're not integrating across multiple touchpoints. Or as referred by my previous blog, front end team is very strong or is tightly coupled with another vital system.
* Classic AEM still has one of the best WYSIWYG experiences. But you carry all the weight of on-prem or container-based management. May not be as cool as UE, but way more functional and best in the industry.
* Docs-based EDS authoring will scale faster than any other model. It's one of the few models where the authoring experience is so streamlined that content teams can scale independently of deep AEM development effort.

---

### Part 3: How Things Could End Up

No single pattern wins. They all exist for a reason.

Sometimes it's political. Sometimes it's what the client asked for. Sometimes it's the shape of the wedding cake.

But knowing the tradeoffs and comparisons is vital to the first step of any implementation. Not every project has the luxury of time to evaluate seven options. But when you’ve seen the full map, you can steer better.

This matrix isn't a prescription. It’s a way to ask better questions.

---
