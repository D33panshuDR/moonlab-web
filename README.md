# Moonlab's Website Guide

This repository contains the source code for the Moonlab's website.

## 1. Introduction to Hugo

The website is built using [Hugo](https://gohugo.io/), one of the most popular open-source static site generators. Hugo is written in Go and is incredibly fast, flexible, and allows us to manage content effectively while building the site in milliseconds.

For detailed documentation, refer to the [Official Hugo Documentation](https://gohugo.io/documentation/).

### Installation

To run the site locally, you will need to install Hugo. We use the **Extended** version of Hugo because it includes support for Sass/SCSS processing and advanced image processing features.

You can easily install Hugo Extended on Linux via snap using the following command:

```bash
sudo snap install hugo --channel=extended
```

Once installed, you can start the local development server by running:

```bash
hugo server
```

The site will then be available at `http://localhost:1313/` and will live-reload as you make changes.

## 2. Layout & Content Structure

Hugo uses a strict but logical directory structure to cleanly separate content from layout and configuration. Here is how the site is organized:

### Application Configuration
- `hugo.toml`: This is the main configuration file for the website at the root directory. It contains site-wide settings like the base URL, title, menu structures, taxonomy definitions, and global parameters.

### Content Management
Content is managed using a combination of Markdown and Data files:
- **Markdown (`content/`)**: The `content/` folder holds the bulk of the website's individual pages. Every subfolder (e.g., `content/news`, `content/people`, `content/research`) represents a distinct section of the site. These files are typically written in Markdown (`.md`) and contain a YAML "frontmatter" block at the top. The frontmatter contains metadata (like `title`, `date`, `summary`), while the rest of the file forms the body text.
- **YAML/Data (`data/`)**: The `data/` folder stores structured, tabular information that doesn't necessarily need a dedicated webpage URL but is used to populate lists and templates across the site (e.g., `publications`, `home.yaml`, `nav.yaml`, and `footer.yaml`).

### Layouts & Assets
- **Layouts (`layouts/`)**: The HTML templates that define how the Markdown and YAML data are rendered into web pages are stored here.
- **Static (`static/`)**: Static assets such as images, logos, raw files, and the CMS configuration (`static/admin/`) live here. Everything in this directory is copied exactly as-is to the final built website.

## 3. Sveltia CMS

To make content editing seamless without requiring editors to write Markdown/YAML manually or use Git via terminal, we use [Sveltia CMS](https://sveltiacms.app/). It is a lightweight, Git-based Headless CMS that acts as a modern alternative to Decap/Netlify CMS.

For more details on how the CMS works, refer to the [Sveltia CMS Documentation](https://sveltiacms.app/en/docs/).

### Git-Based Headless Workflow

Sveltia operates entirely inside the browser and interacts directly with the version control system. Here is a brief overview of the workflow:

1. **Accessing the CMS**: You can access the CMS by navigating to `/admin/` on the live website (or locally via `http://localhost:1313/admin/`).
2. **Authentication**: Editors log in using their associated Git provider accounts (e.g., GitHub, GitLab).
3. **Data Mapping**: The CMS interface is generated based on the `static/admin/config.yml` file, which maps user-friendly UI fields to our specific file formats (like the `news` Markdown pages, the `publications` YAML array, or settings pages).
4. **Git Commits**: When an editor creates a new publication, changes the home page text, or uploads a new team member image, the CMS translates these actions into actual code changes.
5. **Direct Synchronization**: Sveltia commits these file modifications and pushes them straight to the connected GitHub repository on the editor's behalf.
6. **Continuous Deployment**: When the repository receives the new commits, the server automatically triggers a new Hugo build process and deploys the updated website!


