// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/assets/pdf/cv.pdf";
          },
        },{id: "post-the-gentle-singularity",
        
          title: "The Gentle Singularity",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/The-gentle-singularity/";
          
        },
      },{id: "post-deepseek-a-more-extreme-story-of-chinese-tech-idealism",
        
          title: "DeepSeek: A More Extreme Story of Chinese Tech Idealism",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/Deep-seek-interview/";
          
        },
      },{id: "post-exploiting-contemporary-ml",
        
          title: "Exploiting Contemporary ML",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2021/Exploiting_Contemporary_ML/";
          
        },
      },{id: "post-tensor-2-einstein-notation-and-maps",
        
          title: "Tensor #2. Einstein Notation and Maps",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2019/tensor_2_einstein_notation_and_maps/";
          
        },
      },{id: "post-tensor-1-elementary-vector-space",
        
          title: "Tensor #1. Elementary Vector Space",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2019/tensor_1_elementary_vector_space/";
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-i-completed-my-m-sc-at-snu-and-joined-kakao",
          title: 'I completed my M.Sc. at SNU and joined Kakao.',
          description: "",
          section: "News",},{id: "news-one-neurips-2019-paper-dynamics-of-attention-for-focus-transition-daft",
          title: 'One NeurIPS-2019 paper: Dynamics of Attention for Focus Transition (DAFT).',
          description: "",
          section: "News",},{id: "news-one-eccv-2020-task-cv-workshop-oral-paper-diversified-mutual-deep-metric-learning-dm2",
          title: 'One ECCV-2020 TASK-CV workshop oral paper: Diversified Mutual Deep Metric Learning (DM2).',
          description: "",
          section: "News",},{id: "news-i-joined-naver-ai-lab",
          title: 'I joined Naver AI Lab.',
          description: "",
          section: "News",},{id: "news-one-icml-2021-oral-paper-vision-and-language-transformers-vilt",
          title: 'One ICML-2021 oral paper: Vision-and-Language Transformers (ViLT).',
          description: "",
          section: "News",},{id: "news-one-neurips-2021-dgm-workshop-paper-fourier-based-decoder-for-periodic-signals",
          title: 'One NeurIPS-2021 DGM workshop paper: Fourier-based Decoder for Periodic Signals.',
          description: "",
          section: "News",},{id: "news-one-chi-2022-paper-speeding-up-inference-with-user-simulators-through-policy-modulation",
          title: 'One CHI-2022 paper: Speeding up Inference with User Simulators through Policy Modulation.',
          description: "",
          section: "News",},{id: "news-one-iclr-2022-paper-vidt-an-efficient-and-effective-fully-transformer-based-object-detector",
          title: 'One ICLR-2022 paper: ViDT: An Efficient and Effective Fully Transformer-based Object Detector.',
          description: "",
          section: "News",},{id: "news-one-eccv-2022-paper-eccv-caption-correcting-false-negatives-by-collecting-machine-and-human-verified-image-caption-associations-for-ms-coco",
          title: 'One ECCV-2022 paper: ECCV Caption: Correcting False Negatives by Collecting Machine-and-Human-verified Image-Caption Associations...',
          description: "",
          section: "News",},{id: "news-one-bmvc-2022-paper-correlation-between-alignment-uniformity-and-performance-of-dense-contrastive-representations",
          title: 'One BMVC-2022 paper: Correlation between Alignment-Uniformity and Performance of Dense Contrastive Representations.',
          description: "",
          section: "News",},{id: "news-one-iclr-2023-paper-what-do-self-supervised-vision-transformers-learn",
          title: 'One ICLR-2023 paper: What Do Self-Supervised Vision Transformers Learn?.',
          description: "",
          section: "News",},{id: "news-one-acl-2023-paper-pivotal-role-of-language-modeling-in-recommender-systems-enriching-task-specific-and-task-agnostic-representation-learning",
          title: 'One ACL-2023 paper: Pivotal Role of Language Modeling in Recommender Systems: Enriching Task-specific...',
          description: "",
          section: "News",},{id: "news-one-icml-2023-artificial-intelligence-amp-amp-human-computer-interaction-workshop-paper-computational-approaches-for-app-to-app-retrieval-and-design-consistency-check",
          title: 'One ICML-2023 Artificial Intelligence &amp;amp;amp; Human Computer Interaction workshop paper: Computational Approaches for...',
          description: "",
          section: "News",},{id: "news-one-iccv-2023-paper-to-appear-seit-storage-efficient-vision-training-with-tokens-using-1-of-pixel-storage",
          title: 'One ICCV-2023 paper to appear: SeiT: Storage-Efficient Vision Training with Tokens Using 1%...',
          description: "",
          section: "News",},{id: "news-one-cvpr-2024-paper-to-appear-language-only-efficient-training-of-zero-shot-composed-image-retrieval",
          title: 'One CVPR-2024 paper to appear: Language-only Efficient Training of Zero-shot Composed Image Retrieval....',
          description: "",
          section: "News",},{id: "news-one-chil-2024-paper-to-appear-vision-language-generative-model-for-view-specific-chest-x-ray-generation",
          title: 'One CHIL-2024 paper to appear: Vision-Language Generative Model for View-Specific Chest X-ray Generation....',
          description: "",
          section: "News",},{id: "news-one-cvpr-2024-synthetic-data-for-computer-vision-workshop-paper-compodiff-versatile-composed-image-retrieval-with-latent-diffusion",
          title: 'One CVPR-2024 Synthetic Data for Computer Vision workshop paper: CompoDiff: Versatile Composed Image...',
          description: "",
          section: "News",},{id: "news-one-icml-2024-paper-to-appear-stella-continual-audio-video-pre-training-with-spatio-temporal-localized-alignment",
          title: 'One ICML-2024 paper to appear: STELLA: Continual Audio-Video Pre-training with Spatio-Temporal Localized Alignment....',
          description: "",
          section: "News",},{id: "news-one-tmlr-paper-compodiff-versatile-composed-image-retrieval-with-latent-diffusion",
          title: 'One TMLR paper: CompoDiff: Versatile Composed Image Retrieval With Latent Diffusion',
          description: "",
          section: "News",},{id: "news-one-eccv-2024-oral-paper-to-appear-hype-hyperbolic-entailment-filtering-for-underspecified-images-and-texts",
          title: 'One ECCV-2024 oral paper to appear: HYPE: Hyperbolic Entailment Filtering for Underspecified Images...',
          description: "",
          section: "News",},{id: "news-one-aaai-2025-paper-to-appear-extract-free-dense-misalignment-from-clip",
          title: 'One AAAI-2025 paper to appear: Extract Free Dense Misalignment from CLIP.',
          description: "",
          section: "News",},{id: "news-one-iclr-2025-paper-to-appear-probabilistic-language-image-pre-training",
          title: 'One ICLR-2025 paper to appear: Probabilistic Language-Image Pre-Training.',
          description: "",
          section: "News",},{id: "news-i-ve-started-a-new-chapter-at-twelvelabs",
          title: 'I’ve started a new chapter at TwelveLabs!',
          description: "",
          section: "News",},{id: "news-one-cvpr-2025-eval-fomo-2-workshop-paper-emergence-of-text-readability-in-vision-language-models",
          title: 'One CVPR-2025 EVAL-FoMo 2 Workshop paper: Emergence of Text Readability in Vision Language...',
          description: "",
          section: "News",},{id: "news-one-iccv-2025-paper-to-appear-an-efficient-post-hoc-framework-for-reducing-task-discrepancy-of-text-encoders-for-composed-image-retrieval",
          title: 'One ICCV-2025 paper to appear: An Efficient Post-hoc Framework for Reducing Task Discrepancy...',
          description: "",
          section: "News",},{id: "news-twelvelabs-releases-marengo-3-0-a-new-standard-for-foundation-models-that-understand-the-world-in-all-its-complexity",
          title: 'TwelveLabs releases Marengo 3.0, a new standard for foundation models that understand the...',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/cv.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%63%6F%6E%74%61%63%74@%77%6F%6E%6A%61%65.%6B%69%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/dandelin", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/wjk", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=UpZ41EwAAAAJ", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/dandelin_kim", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
