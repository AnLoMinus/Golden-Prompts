const prompts = [
  {
    category: "Blog Writing",
    title: "Understanding [Term] - A Comprehensive Guide",
    content:
      "Please show me the answer but in md style and highlighting titles, headers, sub headers and subtitles, so that it will be perfect for presentation in a blog post",
  },
  {
    category: "Blog Writing",
    title: "[Topic] Checklist: Steps to Follow for Success",
    content:
      "Please provide me with a checklist of steps to follow for success in [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "SEO Optimization",
    title: "Guide to SEO Content Optimization",
    content:
      "Recommend me a category and sub category for labeling the post, and some tags, and meta description up to 136 characters, and Get related keyphrases and Synonyms, and Focus keyword and suggestion title for this post give 3 examples",
  },
  {
    category: "Blog Writing",
    title: "Exploring [Term] - An In-Depth Look",
    content:
      "What Is [Term]? Please show me the answer but in md style and highlighting titles, headers, sub headers and subtitles, and add Subtopics, so that it will be perfect for presentation in a blog post",
  },
  {
    category: "Blog Writing",
    title: "Everything You Need to Know About [Term]",
    content:
      "Please show me the answer but in md style and highlighting titles, headers, sub headers and subtitles, and add Subtopics, so that it will be perfect for presentation in a blog post, At the end, please recommend me a category for labeling the post, and some tags",
  },
  {
    category: "Content Optimization",
    title: "Comprehensive Blog Post Formatting and Optimization",
    content:
      "Please show me the answer but in md style and highlighting titles, headers, sub headers and subtitles, Topics and Subtopics, so that it will be perfect for presentation in a blog post, At the end, please add Overview and recommend me a category and sub category for labeling the post, and some tags, and meta description up to 136 characters, and Get related keyphrases and Synonyms, and Focus keyword",
  },
  {
    category: "Branding",
    title: "Unique Brand Name Suggestions",
    content:
      "Please give me some unique brand name for Topic: {put-here-topic}, please add little description for each and Please show me the answer but in md style and highlighting titles, headers, sub headers and subtitles, so that it will be perfect for presentation in a document for print",
  },
  {
    category: "Blog Writing",
    title: "[Topic] Explained: A Comprehensive Overview",
    content:
      "Please provide me with a detailed explanation of [Topic], formatted in Markdown style with headers, subheaders, and subtopics, for use in a blog post.",
  },
  {
    category: "Technical Writing",
    title: "Deep Dive into [Topic]",
    content:
      "Please show me the answer to 'what is [Topic]?' in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Marketing",
    title: "Marketing Strategy Development",
    content:
      "Description of the Target Audience, Pain Points of the Target Audience, Desires of the Target Audience, Marketing Copy, Script for Social Media Video Ad, Email Marketing Campaign, List of Social Media Influencers, List of Keywords for SEO",
  },
  {
    category: "Product Documentation",
    title: "Product Page Creation Guide",
    content:
      "Create comprehensive product documentation including: Brief description, Benefits, USP, Features list, Specifications, Customer Reviews, Pricing and Availability, FAQs",
  },
  {
    category: "Web Development",
    title: "Technical Support Services Guide",
    content:
      "Service Overview, Service Descriptions, Service Process, Service Tiers, Service Offerings, Service packages, Service Features, Service Benefits, Service options, Price list and Pricing models, Payment options, Customer Reviews, Contact information",
  },
  {
    category: "Case Studies",
    title: "[Topic] Case Studies: Real-Life Examples",
    content:
      "Please provide me with real-life examples and lessons learned from case studies about [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Future Trends",
    title: "The Future of [Topic]: Predictions and Trends",
    content:
      "Please provide me with predictions and trends about the future of [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Educational",
    title: "[Topic] Myths Debunked",
    content:
      "Please provide me with a debunking of common myths and misconceptions about [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Resources",
    title: "[Topic] Tools and Resources Guide",
    content:
      "Please provide me with a list of the best tools and resources for [Topic], including descriptions and recommendations, formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Glossary",
    title: "[Topic] Glossary: Key Terms and Definitions",
    content:
      "Please provide me with a glossary of key terms and definitions related to [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Q&A",
    title: "[Topic] Q&A: Expert Answers",
    content:
      "Please provide me with expert answers to commonly asked questions about [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Infographics",
    title: "[Topic] Infographic Creation",
    content:
      "Please provide me with an infographic that visualizes the key facts and figures about [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Blog Writing",
    title: "[Topic] for Beginners: An Introduction",
    content:
      "Please provide me with a beginner's guide to [Topic], including an overview, definitions, and explanations, formatted in Markdown style with headings, subheadings, and subtopics.",
  },
  {
    category: "Quick Guides",
    title: "[Topic] 101: A Quick Guide",
    content:
      "Please provide me with a quick guide to [Topic], formatted in Markdown style with headings, subheadings, and subtopics, including an overview, definitions, and explanations.",
  },
  {
    category: "Advanced Guides",
    title: "A Step-by-Step Guide to [Topic]: From Basics to Advanced",
    content:
      "Please provide me with a step-by-step guide to [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Advanced Guides",
    title: "Mastering [Topic]: Advanced Techniques",
    content:
      "Please provide me with advanced techniques and strategies for mastering [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Expert Guides",
    title: "[Topic] Demystified: An Expert Guide",
    content:
      "Please provide me with an expert guide to [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, including recommended categories, tags, and meta descriptions for use in a blog post.",
  },
  {
    category: "Expert Tips",
    title: "[Topic] Uncovered: Secrets and Insider Tips",
    content:
      "Please provide me with insider tips and secrets for [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Comparative Analysis",
    title: "[Topic] vs [Topic]: A Comparative Analysis",
    content:
      "Please provide me with a comparative analysis of [Topic] and [Topic], formatted in Markdown style with headings, subheadings, subtopics, and subcategories, including recommended categories, tags, and meta descriptions for use in a blog post.",
  },
  {
    category: "Trends",
    title: "[Topic] Trends: What You Need to Know in [Current Year]",
    content:
      "Please provide me with the latest trends and updates about [Topic] for the current year, formatted in Markdown style with headings, subheadings, subtopics, and subcategories, for use in a blog post.",
  },
  {
    category: "Historical Analysis",
    title: "The History of [Topic]: From Origins to Modern Day",
    content:
      "Please provide me with a comprehensive history of [Topic], including its origins and evolution over time, formatted in Markdown style with headings, subheadings, and subtopics, for use in a blog post.",
  },
  {
    category: "Marketing",
    title: "Marketing Copy Development",
    content:
      "Please help create marketing copy including: Description of Target Audience, Pain Points, Desires, Marketing Copy, Social Media Video Script, Email Campaign, Influencer List, and SEO Keywords.",
  },
  {
    category: "Web Development",
    title: "Web Page Content Creation",
    content:
      "Create comprehensive web page content including: Marketing Copy, Email Marketing Campaign, Target Audience Analysis, Social Media Strategy, SEO Keywords, and Meta Descriptions.",
  },
  {
    category: "Drawing Prompts",
    title: "AI Art Generation Prompts",
    content:
      "Create prompts for generating AI art, including style specifications, themes, and technical parameters. Example: 'Draw a futuristic or sci-fi concept art for a technology brand'",
  },
  {
    category: "Task Management",
    title: "Project Task Breakdown",
    content:
      "Please create: 1. Outline of business plan, 2. Prioritized Task List, 3. Grouped Task List, 4. Divided Task List, 5. Task List with Broken Down Tasks, 6. Task List with Outsourced Tasks, 7. Task List with Established Routine",
  },
  {
    category: "Service Pages",
    title: "Service Page Content Development",
    content:
      "Create comprehensive service page content including: Service Overview, Descriptions, Process, Tiers, Offerings, Packages, Features, Benefits, Options, Pricing, Payment Options, Reviews, Contact Information",
  },
];
