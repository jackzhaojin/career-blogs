# Career Blogs & Professional Content Repository 📝

Welcome to my professional content repository! This space tracks my journey in technology, cloud architecture, AI development, and professional growth through various articles, blog posts, and thought leadership content.

## 🎯 Purpose

This repository serves multiple purposes:
- **Content Tracking**: Organized storage of all my professional articles and blog posts
- **Portfolio Documentation**: A simple, browsable view of my professional writing journey
- **Resource Sharing**: Tools and utilities I've created while developing content
- **Professional Growth**: Documentation of my learning and expertise development over time

## 📚 Content Organization

### Directory Structure
```
career-blogs/
├── LinkedIn2025/                    # 2025 LinkedIn articles and posts
│   ├── 2025-04-13-vibe-coding-on-star-story-generator/
│   ├── 2025-05-25-new-hobby-post/
│   ├── 2025-05-28-aem-headless-frontend/
│   ├── 2025-06-01-gpt-generational-aem/
│   ├── 2025-06-04-7-aem-offerings/
│   ├── 2025-06-08-adobe-eds-cms-shift/
│   ├── 2025-06-10-ai-blog-writing/
│   ├── 2025-06-12-agentic-ai-series-1-auth-and-cicd/
│   └── list.md                     # Index of all 2025 content
├── resize_image_to_1920x1080.py   # Image processing utility
└── README.md                       # This file
```

### Content Categories

**🤖 AI & Machine Learning**
- Agentic AI development and implementation
- AI-assisted content creation workflows
- Azure AI services and integration patterns

**☁️ Cloud Architecture & Azure**
- Azure authentication and RBAC patterns
- DevOps and CI/CD best practices
- Serverless and container deployment strategies

**🏗️ Enterprise Content Management**
- Adobe Experience Manager (AEM) development
- Headless CMS architectures
- Content delivery and optimization

**💼 Professional Development**
- Career transition insights
- Technology adoption strategies
- Industry trend analysis

## 🛠️ Utilities & Tools

### Image Resizing Tool

I've included a Python utility for resizing images to social media-friendly dimensions while maintaining aspect ratios.

#### Installation
```bash
# Install required dependencies
pip install Pillow
```

#### Usage

**Basic usage (adds white padding to bottom):**
```bash
python resize_image_to_1920x1080.py "path/to/your/image.png"
```

**Add padding to top instead:**
```bash
python resize_image_to_1920x1080.py "path/to/your/image.png" --top
```

**Custom dimensions:**
```bash
python resize_image_to_1920x1080.py "image.jpg" --width 1200 --height 800
```

**Examples:**
```bash
# Process a blog header image
python resize_image_to_1920x1080.py "LinkedIn2025/2025-06-12-agentic-ai-series-1-auth-and-cicd/2025-06-12-post-image.png"

# Process with padding on top
python resize_image_to_1920x1080.py "assets/diagram.png" --top

# Custom LinkedIn post dimensions
python resize_image_to_1920x1080.py "thumbnail.jpg" --width 1200 --height 627
```

#### What it does:
- ✅ Maintains original aspect ratio (no stretching or distortion)
- ✅ Adds white padding to achieve target dimensions
- ✅ Supports PNG, JPG, JPEG, BMP, TIFF, and GIF formats
- ✅ Automatically saves output in the same directory with "-{width}x{height}" suffix
- ✅ Optimized for social media platforms (default 1920×1080 for LinkedIn, YouTube thumbnails)

#### Output:
- Input: `my-image.png` → Output: `my-image-1920x1080.png`
- Input: `blog-header.jpg` → Output: `blog-header-1920x1080.jpg`

## 📊 Content Index

### 2025 Publications

| Date | Title | Topics | Format |
|------|-------|--------|---------|
| 2025-06-12 | [Enabling Agentic AI Agents with Azure RBAC](LinkedIn2025/2025-06-12-agentic-ai-series-1-auth-and-cicd/) | Azure, RBAC, AI Agents, Authentication | LinkedIn Article |
| 2025-06-10 | [AI Blog Writing](LinkedIn2025/2025-06-10-ai-blog-writing/) | Content Creation, AI Tools | LinkedIn Post |
| 2025-06-08 | [Adobe EDS CMS Shift](LinkedIn2025/2025-06-08-adobe-eds-cms-shift/) | Adobe, CMS, Industry Trends | LinkedIn Article |
| 2025-06-04 | [7 AEM Offerings](LinkedIn2025/2025-06-04-7-aem-offerings/) | Adobe Experience Manager | LinkedIn Post |
| 2025-06-01 | [GPT Generational AEM](LinkedIn2025/2025-06-01-gpt-generational-aem/) | AI, AEM, Development | LinkedIn Article |
| 2025-05-28 | [AEM Headless Frontend](LinkedIn2025/2025-05-28-aem-headless-frontend/) | Headless CMS, Frontend | LinkedIn Article |
| 2025-05-25 | [New Hobby Post](LinkedIn2025/2025-05-25-new-hobby-post/) | Personal Development, AI | LinkedIn Post |
| 2025-04-13 | [Vibe Coding on Star Story Generator](LinkedIn2025/2025-04-13-vibe-coding-on-star-story-generator/) | Creative Coding, AI | LinkedIn Post |

*For a complete, up-to-date list, see [LinkedIn2025/list.md](LinkedIn2025/list.md)*

## 🎨 Visual Assets

Each content piece includes:
- **Hero images** sized for social media platforms
- **Diagrams and screenshots** supporting technical concepts
- **Process flows** and architecture diagrams
- **Code snippets** and configuration examples

All images are processed using the included resize utility to ensure consistent, professional presentation across platforms.

## 🔗 Connect & Follow

- **Professional Blog**: [jackzhaojin.github.io/blogs.html](https://jackzhaojin.github.io/blogs.html)
- **LinkedIn**: Content published and cross-posted to LinkedIn
- **GitHub**: [jackzhaojin](https://github.com/jackzhaojin) - Code examples and projects

## 📈 Content Strategy

My content focuses on:

1. **Practical Implementation** - Real-world examples with working code
2. **Learning Journey** - Documenting challenges and solutions
3. **Technology Adoption** - Exploring emerging tools and platforms
4. **Professional Growth** - Sharing insights from career transitions
5. **Community Value** - Creating resources others can use and learn from

## 🤝 Contributing

While this is primarily a personal repository, I welcome:
- **Feedback** on content and technical accuracy
- **Suggestions** for topics or improvements
- **Discussion** about the technologies and practices covered

Feel free to open issues for any questions or discussions!

## 📄 License

Content in this repository is shared for educational and professional development purposes. Please respect copyright and attribution when referencing or sharing.

---

*Last Updated: June 12, 2025*  
*Repository Purpose: Professional content tracking and portfolio documentation*
