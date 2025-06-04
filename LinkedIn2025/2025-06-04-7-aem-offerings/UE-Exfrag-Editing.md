# Using Adobe Universal Editor to Edit Experience Fragments In-Context

## Overview

This document summarizes how Adobe Experience Manager as a Cloud Service (AEMaaCS) allows editing of **Experience Fragments (XFs)** in the context of a page via the **Universal Editor (UE)**, based on Jack Jin's use case. Jack is a senior AEM architect focused on headless CMS and generative AI integrations, looking to streamline authoring workflows for AEM sites.

## Key Insights

* **Traditional AEM editing** requires authors to open Experience Fragments in a separate tab using the "Open Original" function. There is no native in-page editing of XF components in Sites Editor.
* **Universal Editor changes this** by enabling real-time, in-context editing of reusable blocks like XFs directly within the rendered page view.

## Requirements for In-Context XF Editing with UE

To enable Universal Editor editing for Experience Fragments, you must:

### 1. Instrument the DOM with UE Data Attributes

Ensure XF components include UE metadata:

```html
<div
  data-aue-resource="urn:aemconnection:/content/experience-fragments/my-xf/jcr:content"
  data-aue-type="component"
  data-aue-prop="text"
  data-aue-label="Experience Fragment Text">
  <!-- Editable content -->
</div>
```

### 2. Add the Universal Editor CORS Script

```html
<script src="https://universal-editor-service.adobe.io/cors.js" async></script>
```

### 3. Define AEM Connection in HTML Head

```html
<meta name="urn:adobe:aue:system:aemconnection" content="aem:https://author.example.com">
```

### 4. AEM Configuration Updates

* **Sling Servlet Headers**: Set `X-Frame-Options` to allow iframe usage.
* **Token Auth Cookies**: Configure `SameSite=None` to allow cross-origin requests.

## Adobe Official Documentation

These Experience League links are Adobe's canonical sources for Universal Editor setup and usage:

* [Universal Editor - Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction)
* [Getting Started Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/getting-started)
* [Authoring in Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring)

## Related Jack Jin Context

* Interested in in-context editing to streamline workflows across headless and Sites setups.
* Familiar with editable templates, AEM as a Cloud Service, and hybrid use of Sites and Content Fragments.
* Wants practical, referenceable examples (e.g., experienceleague.adobe.com or Adobe.com implementations).

## Summary

You **can** edit Experience Fragments in context with Universal Editor, provided your site is properly instrumented and AEM is configured to support UE. This offers a more intuitive authoring experience compared to the traditional XF editing flow.
