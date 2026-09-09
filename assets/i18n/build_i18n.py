# -*- coding: utf-8 -*-
"""Build the translation dictionaries used by assets/lang.js.

Keys are the English innerHTML of leaf text elements exactly as the browser
serialises them (whitespace collapsed, `&` as `&amp;`, SVGs tokenised as {svg0}, …),
plus page titles, lightbox captions and the strings site.js assembles at runtime
(month labels, "views"). Values keep the same inline tags. Anything not listed
stays English on the site: names, paper titles, venues, song titles, tech names.

Run:  conda run -n bcpnn_local python assets/i18n/build_i18n.py
Writes zh-Hans.json, ja.json and zh-Hant.json (OpenCC s2twp from zh-Hans, with
the overrides at the bottom).

To find the keys of a page: serve the site, open the page, run
window.__I18N.collect() in the console (or the headless collector in the skill doc).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZH, JA = {}, {}


def E(en, zh, ja):
    ZH[en] = zh
    JA[en] = ja


# ---------------------------------------------------------------- page titles
E("Heng Zhang | Postdoctoral Researcher", "Heng Zhang | 博士后研究员", "Heng Zhang | 博士研究員")
E("Research | Heng Zhang", "研究 | Heng Zhang", "研究 | Heng Zhang")
E("Developer | Heng Zhang", "开发 | Heng Zhang", "開発 | Heng Zhang")
E("Music | Heng Zhang", "音乐 | Heng Zhang", "音楽 | Heng Zhang")
E("Self-Organizing Dynamical Equations (SODE) | Heng Zhang", "自组织动力学方程（SODE） | Heng Zhang", "自己組織化動力学方程式（SODE） | Heng Zhang")
E("Robust Bio-inspired Vision Systems | Heng Zhang", "鲁棒的类脑视觉系统 | Heng Zhang", "頑健な生物着想型視覚システム | Heng Zhang")
E("Xenovert: Adaptive Distribution Shift | Heng Zhang", "Xenovert：自适应分布偏移 | Heng Zhang", "Xenovert：分布シフトへの適応 | Heng Zhang")
E("Advancing Reservoir Computing | Heng Zhang", "推进储备池计算 | Heng Zhang", "リザバーコンピューティングの発展 | Heng Zhang")
E("Neuro-like Temporal Learning Systems | Heng Zhang", "类神经时序学习系统 | Heng Zhang", "神経系に似た時系列学習システム | Heng Zhang")

# ---------------------------------------------------------------- nav (desktop menus + phone list)
E("About me{svg0}", "关于我{svg0}", "私について{svg0}")
E("About me", "关于我", "私について")
E("Hero", "首页", "トップ")
E("Who I am, at a glance", "一眼看懂我是谁", "ひと目でわかる自己紹介")
E("Background", "背景", "経歴")
E("Bio and skills", "简介与技能", "プロフィールとスキル")
E("Professional Experience", "工作经历", "職歴")
E("Positions held", "任职经历", "これまでの職位")
E("Academic Background", "教育背景", "学歴")
E("Degrees and theses", "学位与论文", "学位と論文")
E("Additional Information", "其他信息", "その他")
E("Languages and teaching", "语言与教学", "語学と教育経験")
E("Get in Touch", "联系我", "お問い合わせ")
E("Email and profiles", "邮箱与个人主页", "メールと各種プロフィール")
E("As a Researcher{svg0}", "研究者{svg0}", "研究者として{svg0}")
E("As a Researcher", "研究者", "研究者として")
E("Activities", "活动", "活動")
E("Posters and talks in pictures", "海报与报告的照片", "ポスターと講演の写真")
E("Research Interests", "研究方向", "研究テーマ")
E("Current directions", "当前的研究方向", "現在の方向性")
E("Selected Works", "代表作", "主な業績")
E("Papers by category", "按类别浏览论文", "カテゴリ別の論文")
E("Presentations", "学术报告", "発表")
E("Talks and posters", "口头报告与海报", "講演とポスター")
E("Funding", "科研经费", "研究資金")
E("Grants and awards", "资助与奖项", "助成金と受賞")
E("As a Developer{svg0}", "开发者{svg0}", "開発者として{svg0}")
E("As a Developer", "开发者", "開発者として")
E("Open-world action game · MiraiX", "开放世界动作游戏 · MiraiX", "オープンワールド・アクションゲーム · MiraiX")
E("SyncMapV2 in Unreal Engine", "Unreal Engine 中的 SyncMapV2", "Unreal Engine の SyncMapV2")
E("A paper as a walkable 3D scene", "把论文做成可以走进去的 3D 场景", "論文を歩ける3Dシーンに")
E("Local AI speaking practice", "本地运行的 AI 口语练习", "ローカルAIで会話練習")
E("As a Music Lover{svg0}", "音乐爱好者{svg0}", "音楽好きとして{svg0}")
E("As a Music Lover", "音乐爱好者", "音楽好きとして")
E("Piano &amp; voice", "钢琴弹唱", "ピアノ弾き語り")
E("Fujii Kaze covers, now playing", "藤井风翻唱，正在播放", "藤井風カバー、再生中")
E("The playlist", "播放列表", "プレイリスト")
E("All 17 covers on Bilibili", "Bilibili 上的全部 17 首翻唱", "Bilibili のカバー全17曲")
E("Favorite artists", "喜欢的音乐人", "好きなアーティスト")
E("Who I keep coming back to", "百听不厌的那些人", "何度も聴き返す人たち")
E("Contact", "联系", "連絡先")

# ---------------------------------------------------------------- hero + doors
E("Postdoctoral Researcher at IRCN, University of Tokyo", "东京大学 IRCN 博士后研究员", "東京大学 IRCN 博士研究員")
E("Developing bio-inspired AI systems for computer vision and NLP through predictive processing and self-organization principles.",
  "基于预测加工与自组织原理，研发面向计算机视觉与自然语言处理的类脑 AI 系统。",
  "予測処理と自己組織化の原理に基づき、コンピュータビジョンと自然言語処理のための生物に着想を得たAIシステムを開発しています。")
E("Research, Paper", "研究 · 论文", "研究・論文")
E("Game, Apps, Engine", "游戏 · 应用 · 引擎", "ゲーム・アプリ・エンジン")
E("Music, Vocal, Arts", "音乐 · 歌声 · 艺术", "音楽・歌・アート")
E("Keep exploring", "继续探索", "もっと見る")
E("More of me", "我的其他面", "ほかの顔も")

# ---------------------------------------------------------------- about
E("About", "关于", "自己紹介")
E("I am a postdoctoral researcher at the International Research Center for Neurointelligence (WPI-IRCN), UTIAS, The University of Tokyo, in collaboration with KTH Royal Institute of Technology. My research develops bio-inspired AI systems for computer vision and natural language processing by drawing on principles of predictive processing and self-organization observed in biological systems.",
  "我是东京大学国际高等研究所神经智能国际研究机构（WPI-IRCN）的博士后研究员，与瑞典皇家理工学院（KTH）合作开展研究。我的研究借鉴生物系统中的预测加工与自组织原理，研发面向计算机视觉与自然语言处理的类脑 AI 系统。",
  "東京大学国際高等研究所ニューロインテリジェンス国際研究機構（WPI-IRCN）の博士研究員として、スウェーデン王立工科大学（KTH）と共同で研究を行っています。生物システムに見られる予測処理と自己組織化の原理を手がかりに、コンピュータビジョンと自然言語処理のための生物に着想を得たAIシステムを開発しています。")
E("I focus on creating adaptive and robust learning frameworks that excel in dynamic, uncertain environments. My work spans unsupervised learning, dynamical systems, neural representations, and sequence learning. Through computational modeling of brain functions—particularly prediction and complex sequence processing—I aim to develop artificial intelligence that reflects the efficiency and resilience of biological cognition.",
  "我致力于构建能在动态、不确定环境中稳定工作的自适应、鲁棒学习框架，研究涵盖无监督学习、动力系统、神经表征与序列学习。通过对大脑功能（尤其是预测与复杂序列加工）的计算建模，我希望发展出兼具生物认知效率与韧性的人工智能。",
  "動的で不確実な環境でも力を発揮する、適応的で頑健な学習フレームワークの構築に取り組んでいます。研究は教師なし学習、力学系、神経表現、系列学習にまたがります。脳機能、とりわけ予測と複雑な系列処理の計算モデリングを通じて、生物の認知が持つ効率性と回復力を備えた人工知能の実現を目指しています。")
E("Specialties", "专长", "専門分野")
E("Deep Learning", "深度学习", "深層学習")
E("Computer Vision", "计算机视觉", "コンピュータビジョン")
E("NLP", "自然语言处理", "自然言語処理")
E("Reservoir Computing", "储备池计算", "リザバーコンピューティング")
E("Self-Organization", "自组织", "自己組織化")
E("Dynamical Systems", "动力系统", "力学系")
E("Unsupervised Learning", "无监督学习", "教師なし学習")
E("Robustness", "鲁棒性", "頑健性")

# ---------------------------------------------------------------- career / education / more
E("Career", "职业", "キャリア")
E("April 2025 — Present", "2025年4月 — 至今", "2025年4月 — 現在")
E("Postdoctoral Researcher", "博士后研究员", "博士研究員")
E("International Research Center for Neurointelligence (WPI-IRCN), UTIAS, The University of Tokyo", "东京大学国际高等研究所 神经智能国际研究机构（WPI-IRCN）", "東京大学国際高等研究所 ニューロインテリジェンス国際研究機構（WPI-IRCN）")
E("Collaborative initiative with KTH Royal Institute of Technology. Computational modeling of brain functions including prediction and complex sequence processing for bio-inspired AI.",
  "与瑞典皇家理工学院（KTH）的合作项目。面向类脑 AI，对预测与复杂序列加工等大脑功能进行计算建模。",
  "スウェーデン王立工科大学（KTH）との共同プロジェクト。生物に着想を得たAIに向けて、予測や複雑な系列処理といった脳機能を計算論的にモデル化しています。")
E("Oct 2024 — Mar 2025", "2024年10月 — 2025年3月", "2024年10月 — 2025年3月")
E("Kyushu University", "九州大学", "九州大学")
E("Developing robust and adaptive machine learning models. Building bio-inspired AI systems resistant to adversarial attacks and noise corruptions.",
  "研发鲁棒且自适应的机器学习模型，构建能抵御对抗攻击与噪声损坏的类脑 AI 系统。",
  "頑健で適応的な機械学習モデルの開発。敵対的攻撃やノイズ劣化に強い、生物に着想を得たAIシステムを構築。")
E("May 2024 — Mar 2025", "2024年5月 — 2025年3月", "2024年5月 — 2025年3月")
E("System Engineer", "系统工程师", "システムエンジニア")
E("3D open-world game development, machine learning engineering, and UI/UX design.",
  "3D 开放世界游戏开发、机器学习工程与 UI/UX 设计。", "3Dオープンワールドゲームの開発、機械学習エンジニアリング、UI/UXデザイン。")
E("June 2022 — Sept 2024", "2022年6月 — 2024年9月", "2022年6月 — 2024年9月")
E("Research Assistant", "研究助理", "リサーチアシスタント")
E("Research assistant for projects in mathematics and information engineering. Lab assistant for stem cell culturing.",
  "参与数学与信息工程方向的研究项目，并担任干细胞培养的实验室助理。", "数学・情報工学分野の研究プロジェクトを補助。幹細胞培養のラボアシスタントも担当。")
E("Education", "教育", "学歴")
E("Oct 2021 — Sept 2024", "2021年10月 — 2024年9月", "2021年10月 — 2024年9月")
E("Ph.D. in Artificial Intelligence &amp; Information Science", "人工智能与信息科学博士", "博士（人工知能・情報科学）")
E('Thesis: "Adaptive and Robust Learning with Self-Organizing and Nonlinear Dynamics." Full-funded by SPRING program from JST.',
  "博士论文：《基于自组织与非线性动力学的自适应鲁棒学习》。获 JST SPRING 项目全额资助。",
  "博士論文「自己組織化と非線形ダイナミクスによる適応的で頑健な学習」。JST SPRING プログラムによる全額支援。")
E("Sept 2019 — Dec 2020", "2019年9月 — 2020年12月", "2019年9月 — 2020年12月")
E("MSc. Communications &amp; Signal Processing", "通信与信号处理硕士", "修士（通信・信号処理）")
E("University of Manchester", "曼彻斯特大学", "マンチェスター大学")
E("First-Class Honours. Outstanding Distinction grade in master's thesis on human gait classification using machine learning.",
  "一等荣誉学位。硕士论文（基于机器学习的人类步态分类）获杰出优异评级。",
  "一級優等学位。機械学習による歩容分類に関する修士論文で最優秀評価。")
E("Sept 2015 — July 2019", "2015年9月 — 2019年7月", "2015年9月 — 2019年7月")
E("BEng. Electronic &amp; Information Engineering", "电子信息工程学士", "学士（電子情報工学）")
E("Shenzhen University", "深圳大学", "深圳大学")
E("Top 10 GPA", "GPA 年级前十", "GPA 上位10名")
E("More", "更多", "その他")
E("Languages", "语言", "言語")
E("English - Highly proficient", "英语 - 熟练", "英語 - 上級")
E("Chinese - Native", "中文 - 母语", "中国語 - 母語")
E("Cantonese - Native", "粤语 - 母语", "広東語 - 母語")
E("Japanese - Limited Conversational", "日语 - 简单会话", "日本語 - 日常会話レベル")
E("Teaching Experience", "教学经历", "教育経験")
_SPAN = '<span style="color: var(--color-text-muted); font-size: 0.9rem;">'
E("<strong>Teaching Assistant</strong><br> Prompt Engineering, Kyushu University<br> " + _SPAN + "Apr 2024 - Sept 2024</span>",
  "<strong>助教</strong><br> 提示工程，九州大学<br> " + _SPAN + "2024年4月 - 2024年9月</span>",
  "<strong>ティーチングアシスタント</strong><br> プロンプトエンジニアリング、九州大学<br> " + _SPAN + "2024年4月 - 2024年9月</span>")
E("<strong>Lecturer</strong><br> Education Career Planning, New Oriental Education &amp; Technology Group<br> " + _SPAN + "Apr 2022 - Sept 2022</span>",
  "<strong>讲师</strong><br> 教育职业规划，新东方教育科技集团<br> " + _SPAN + "2022年4月 - 2022年9月</span>",
  "<strong>講師</strong><br> 教育キャリアプランニング、新東方教育科技集団<br> " + _SPAN + "2022年4月 - 2022年9月</span>")

# ---------------------------------------------------------------- contact / footer
E("Location", "地址", "所在地")
E("Email", "邮箱", "メール")
E("© 2025 Heng Zhang. All rights reserved.", "© 2025 Heng Zhang 版权所有。", "© 2025 Heng Zhang. 無断転載を禁じます。")

# ---------------------------------------------------------------- activities
E("New", "新", "NEW")
E("Interactive site · Paper companion", "交互网站 · 论文伴随站", "インタラクティブサイト · 論文コンパニオン")
E("Companion site for the paper · with Pawel Herman &amp; Zenas C. Chao · Sept 2026",
  "论文伴随网站 · 与 Pawel Herman &amp; Zenas C. Chao 合作 · 2026年9月",
  "論文のコンパニオンサイト · Pawel Herman &amp; Zenas C. Chao と共同 · 2026年9月")
E("Play with the model in your browser: turn the noise knob, watch the rare events come out right. Also in Chinese and Japanese.",
  "在浏览器里把玩这个模型：转动噪声旋钮，看稀有事件的估计变准。另有中文与日文版本。",
  "ブラウザでモデルを動かしてみてください。ノイズのつまみを回すと、稀な事象の推定が正確になっていきます。中国語・日本語版もあります。")
E("Open the site ↗", "打开网站 ↗", "サイトを開く ↗")
E("Poster · NEURO2026", "海报 · NEURO2026", "ポスター · NEURO2026")
E("NEURO2026 · Kobe · Aug 1, 2026", "NEURO2026 · 神户 · 2026年8月1日", "NEURO2026 · 神戸 · 2026年8月1日")
_A = '<a href="https://noise-bcpnn-simulation.pages.dev/" target="_blank" rel="noopener">'
E("Poster 3P-465 at Japan's biggest neuroscience meeting. Try the model yourself on the " + _A + "companion site</a>.",
  "在日本最大的神经科学大会上展示海报（3P-465）。欢迎到" + _A + "伴随网站</a>亲自试试这个模型。",
  "日本最大の神経科学大会でのポスター発表（3P-465）。" + _A + "コンパニオンサイト</a>でモデルを試せます。")
E("Poster · IRCN–NTU Joint Symposium", "海报 · IRCN–NTU 联合研讨会", "ポスター · IRCN–NTU 合同シンポジウム")
E("IRCN–NTU Joint Symposium · Singapore · Feb 3, 2026", "IRCN–NTU 联合研讨会 · 新加坡 · 2026年2月3日", "IRCN–NTU 合同シンポジウム · シンガポール · 2026年2月3日")
E("An early version of the noise-and-rare-events story, shown on the IRCN trip to NTU.",
  "噪声与稀有事件这个故事的早期版本，在 IRCN 访问 NTU 时展示。", "ノイズと稀な事象の研究の初期版。IRCN の NTU 訪問で発表しました。")
E("Talk &amp; Poster · IRCN Retreat", "报告 &amp; 海报 · IRCN Retreat", "講演 &amp; ポスター · IRCN リトリート")
E("IRCN Retreat · Odawara · Oct 23, 2025", "IRCN Retreat · 小田原 · 2025年10月23日", "IRCN リトリート · 小田原 · 2025年10月23日")
E("Talk and poster at the annual retreat: a reservoir plus Hebbian prototypes for robust vision.",
  "年度 Retreat 上的报告与海报：用储备池加 Hebbian 原型实现鲁棒视觉。", "年次リトリートでの講演とポスター。リザバーとヘッブ型プロトタイプによる頑健な視覚。")
E("Poster · Photonic Computing Symposium", "海报 · 光计算研讨会", "ポスター · 光コンピューティングシンポジウム")
E("Photonic Computing Symposium · NICT, Koganei · Dec 17, 2024", "光计算研讨会 · NICT，小金井 · 2024年12月17日", "光コンピューティングシンポジウム · NICT 小金井 · 2024年12月17日")
E("Poster with the Vargas lab on self-organizing dynamics for photonic reservoirs.",
  "与 Vargas 实验室合作的海报：面向光子储备池的自组织动力学。", "Vargas 研究室との共同ポスター。フォトニックリザバーのための自己組織化ダイナミクス。")
E("Talk · AICCC 2022", "报告 · AICCC 2022", "講演 · AICCC 2022")
E("AICCC 2022 · Osaka · Dec 17, 2022", "AICCC 2022 · 大阪 · 2022年12月17日", "AICCC 2022 · 大阪 · 2022年12月17日")
E("My first conference talk, on how SyncMap organizes itself over space and time. Certificate included.",
  "我的第一次会议报告，讲 SyncMap 如何在时空中自组织。附证书一张。", "初めての学会発表。SyncMap が時空間でどう自己組織化するかについて。証明書つき。")
# lightbox captions (data-caption on the photo cards)
E("NEURO2026 poster", "NEURO2026 海报", "NEURO2026 ポスター")
E("Presenting the poster at NEURO2026", "在 NEURO2026 讲解海报", "NEURO2026 でポスター発表")
E("At the NEURO2026 entrance, Kobe", "NEURO2026 会场入口，神户", "NEURO2026 会場入口、神戸")
E("IRCN–NTU symposium poster", "IRCN–NTU 研讨会海报", "IRCN–NTU シンポジウムのポスター")
E("Group photo, NTU–IRCN Joint Workshop 2026, Singapore", "NTU–IRCN 联合研讨会 2026 合影，新加坡", "NTU–IRCN 合同ワークショップ 2026 の集合写真、シンガポール")
E("Presenting the poster at NTU, Singapore", "在新加坡 NTU 讲解海报", "シンガポールの NTU でポスター発表")
E("IRCN Retreat 2025 poster", "IRCN Retreat 2025 海报", "IRCN リトリート 2025 のポスター")
E("At the poster, IRCN Retreat 2025", "海报前，IRCN Retreat 2025", "ポスターの前で、IRCN リトリート 2025")
E("Photonic Computing Symposium 2024 poster", "光计算研讨会 2024 海报", "光コンピューティングシンポジウム 2024 のポスター")
E("At the poster, NICT 2024", "海报前，NICT 2024", "ポスターの前で、NICT 2024")
E("Giving the talk at AICCC 2022, Osaka", "在 AICCC 2022 做报告，大阪", "AICCC 2022 で講演、大阪")
E("Presentation certificate, AICCC 2022", "AICCC 2022 报告证书", "AICCC 2022 の発表証明書")

# ---------------------------------------------------------------- research interests (cards)
E("Research", "研究", "研究")
E("Self-Organizing Dynamical Equations (SODE)", "自组织动力学方程（SODE）", "自己組織化動力学方程式（SODE）")
E("Bio-inspired systems for complex sequential learning using self-organization and nonlinear dynamics. Enables adaptive learning without backpropagation.",
  "利用自组织与非线性动力学进行复杂序列学习的类脑系统，无需反向传播即可自适应学习。",
  "自己組織化と非線形ダイナミクスで複雑な系列を学習する、生物に着想を得たシステム。誤差逆伝播なしで適応学習ができます。")
E("Robust Bio-inspired Vision Systems", "鲁棒的类脑视觉系统", "頑健な生物着想型視覚システム")
E("Unsupervised image segmentation systems that maintain performance under severe noise and corruption, mimicking human visual perception.",
  "在严重噪声与损坏下仍能保持性能的无监督图像分割系统，模仿人类视觉感知。",
  "強いノイズや劣化のもとでも性能を保つ教師なし画像セグメンテーション。人の視覚知覚に倣っています。")
E("Xenovert: Adaptive Distribution Shift", "Xenovert：自适应分布偏移", "Xenovert：分布シフトへの適応")
E("Biologically-inspired algorithm for real-time adaptation to distribution shifts using tree-based mapping structures.",
  "受生物启发的算法，用树状映射结构实时适应分布偏移。", "木構造の写像で分布シフトにリアルタイムに適応する、生物に着想を得たアルゴリズム。")
E("Advancing Reservoir Computing", "推进储备池计算", "リザバーコンピューティングの発展")
E("Bio-inspired sparse recurrent neural networks leveraging high-dimensional dynamics for temporal and spatial processing.",
  "利用高维动力学处理时间与空间信息的类脑稀疏循环神经网络。",
  "高次元ダイナミクスを活かして時間・空間情報を処理する、生物に着想を得た疎な再帰型ニューラルネットワーク。")
E("Neuro-like Temporal Learning Systems", "类神经时序学习系统", "神経系に似た時系列学習システム")
E("BCPNN-based attractor networks for rare-event learning in temporal data streams with modular hypercolumn architecture.",
  "基于 BCPNN 的吸引子网络，采用模块化超柱结构，在时间数据流中学习稀有事件。",
  "モジュール化されたハイパーカラム構造を持つ BCPNN ベースのアトラクターネットワークで、時系列データ中の稀な事象を学習。")

# ---------------------------------------------------------------- publications
E("Publications", "论文", "論文")
E("All", "全部", "すべて")
E("Under Review", "审稿中", "査読中")
E("Journal Articles", "期刊论文", "学術誌論文")
E("Conference Papers", "会议论文", "会議論文")
E("Reviews", "综述", "総説")
E("Soon to Submit", "即将投稿", "投稿予定")
E("Conference", "会议", "会議")
E("Journal Article", "期刊论文", "学術誌論文")
E("Review Article", "综述", "総説")

# ---------------------------------------------------------------- presentations
E("Talks &amp; Posters", "报告与海报", "講演とポスター")
E("Poster", "海报", "ポスター")
E("Talk", "报告", "講演")
E("NEURO2026, the 49th Annual Meeting of the Japan Neuroscience Society (Poster 3P-465), Kobe Convention Center, Kobe, Japan, August 1, 2026",
  "NEURO2026 第49届日本神经科学学会年会（海报 3P-465），神户国际会议中心，神户，日本，2026年8月1日",
  "NEURO2026 第49回日本神経科学大会（ポスター 3P-465）、神戸国際会議場、神戸、2026年8月1日")
E("IRCN Team Salon Talk, IRCN, The University of Tokyo, Japan, May 27, 2026",
  "IRCN Team Salon Talk，IRCN，东京大学，日本，2026年5月27日", "IRCN チームサロントーク、IRCN、東京大学、2026年5月27日")
E("The Third IRCN International Joint Symposium (IRCN-NTU), Lee Kong Chian School of Medicine, Nanyang Technological University, Singapore, February 3, 2026",
  "第三届 IRCN 国际联合研讨会（IRCN-NTU），南洋理工大学李光前医学院，新加坡，2026年2月3日",
  "第3回 IRCN 国際合同シンポジウム（IRCN-NTU）、南洋理工大学リー・コン・チアン医学部、シンガポール、2026年2月3日")
E("IRCN Retreat, Odawara, Japan, October 23, 2025", "IRCN Retreat，小田原，日本，2025年10月23日", "IRCN リトリート、小田原、2025年10月23日")
E("AI Incubator Salon Talk, IRCN, The University of Tokyo, Japan, October 18, 2025",
  "AI Incubator Salon Talk，IRCN，东京大学，日本，2025年10月18日", "AI インキュベーター・サロントーク、IRCN、東京大学、2025年10月18日")
E("Second Open Symposium on Photonic Computing, NICT, Koganei, Japan, December 17, 2024",
  "第二届光计算公开研讨会，NICT，小金井，日本，2024年12月17日", "第2回光コンピューティング公開シンポジウム、NICT、小金井、2024年12月17日")
E("5th Artificial Intelligence and Cloud Computing Conference (AICCC), Osaka, Japan, December 17, 2022",
  "第五届人工智能与云计算会议（AICCC），大阪，日本，2022年12月17日", "第5回人工知能・クラウドコンピューティング会議（AICCC）、大阪、2022年12月17日")

# ---------------------------------------------------------------- funding
E("External Funding Contributions", "外部科研经费", "外部研究資金")
E("Read more", "展开", "詳しく")
E("Show less", "收起", "閉じる")
E("UTokyo Global Activity Support Program for Young Researchers • 2026–2027", "东京大学青年研究者国际活动支援计划 • 2026–2027", "東京大学 若手研究者国際活動支援プログラム • 2026–2027")
E("International research dispatch support to develop global networks and international capabilities through overseas research activities",
  "支持海外研究派遣，以拓展国际网络与国际研究能力", "海外での研究活動を通じて国際的なネットワークと能力を育てるための研究派遣支援")
E("¥570,000 • Awardee", "¥570,000 • 获资助者", "¥570,000 • 採択者")
E("WPI-IRCN Retreat Brainstorming Awards, UTokyo • 2025–2026", "WPI-IRCN Retreat 头脑风暴奖，东京大学 • 2025–2026", "WPI-IRCN リトリート・ブレインストーミング賞、東京大学 • 2025–2026")
E("Intrinsic functionalities of biological networks with multi-reservoir systems", "多储备池系统中生物网络的内在功能", "多重リザバー系による生体ネットワークの内在的機能")
E("¥800,000 • Co-Investigator", "¥800,000 • 共同研究者", "¥800,000 • 研究分担者")
E("The Telecommunications Advancement Foundation • 2025–2026", "电气通信普及财团 • 2025–2026", "電気通信普及財団 • 2025–2026")
E("Improving AI security by developing unsupervised, robust, and adaptive AI systems", "通过研发无监督、鲁棒且自适应的 AI 系统提升 AI 安全性", "教師なしで頑健かつ適応的なAIシステムの開発によるAIセキュリティの向上")
E("¥2,105,000 • Co-Investigator", "¥2,105,000 • 共同研究者", "¥2,105,000 • 研究分担者")
E("JSPS, MEXT Grant-in-Aid for Transformative Research Areas (A) • 2022–2026", "日本学术振兴会 / 文部科学省 学术变革领域研究（A） • 2022–2026", "JSPS・文部科学省 学術変革領域研究（A） • 2022–2026")
E("Creation of photonic computing utilizing the ultimate performance of light", "利用光的极限性能创造光计算", "光の究極性能を活かした光コンピューティングの創成")
E("¥20,000,000 • Research Collaborator", "¥20,000,000 • 研究协作者", "¥20,000,000 • 研究協力者")
E("Leading Company • 2023–2025", "领军企业 • 2023–2025", "リーディング企業 • 2023–2025")
E("Small anomaly detection algorithm for autonomous driving based on Inpainting", "基于图像修复的自动驾驶小型异常检测算法", "インペインティングに基づく自動運転向け微小異常検出アルゴリズム")
E("¥15,000,000 • Research Collaborator", "¥15,000,000 • 研究协作者", "¥15,000,000 • 研究協力者")
E("JSPS, Grant in Aid for Challenging Research (Exploratory) • 2022–2023", "日本学术振兴会 挑战性研究（萌芽） • 2022–2023", "JSPS 挑戦的研究（萌芽） • 2022–2023")
E("Learning based on Self-Organization - Pioneering a Novel Foundation for AI", "基于自组织的学习——开拓 AI 的新基础", "自己組織化に基づく学習 — AIの新しい基盤を拓く")
E("¥5,000,000 • Major Research Collaborator", "¥5,000,000 • 主要研究协作者", "¥5,000,000 • 主要研究協力者")
E("Japan Science and Technology Agency (JST) • 2021–2024", "日本科学技术振兴机构（JST） • 2021–2024", "科学技術振興機構（JST） • 2021–2024")
E("Support for Pioneering Research Initiated by the Next Generation (SPRING)", "次世代研究者挑战性研究计划（SPRING）", "次世代研究者挑戦的研究プログラム（SPRING）")
E("¥8,500,000 • Highly-selected Student", "¥8,500,000 • 入选学生", "¥8,500,000 • 採択学生")

# ---------------------------------------------------------------- developer
E("Projects", "项目", "プロジェクト")
E("Things I build outside the lab, and the research code that grew into something you can run.",
  "实验室之外做的东西，以及从研究代码长成可以跑起来的作品。", "研究室の外で作っているものと、研究コードから育って動くようになったもの。")
E("Trailer: “He Hunts Giants… Until the Dragon Appears”.", "预告片：《He Hunts Giants… Until the Dragon Appears》。", "トレーラー「He Hunts Giants… Until the Dragon Appears」。")
E("Game · MiraiX", "游戏 · MiraiX", "ゲーム · MiraiX")
E("My role: UI &amp; VFX designer · atmospheric open-world action game · in development",
  "我的角色：UI &amp; VFX 设计师 · 氛围感开放世界动作游戏 · 开发中", "担当：UI &amp; VFX デザイナー · 雰囲気重視のオープンワールド・アクション · 開発中")
E("I design the interface and the visual effects for Olden Flames at MiraiX: the HUD and menus you see on screen, and the fire, magic and impact effects you see in the world. The trailer above shows both in action.",
  "我在 MiraiX 负责 Olden Flames 的界面与视觉特效：屏幕上的 HUD 和菜单，以及世界里的火焰、魔法与打击特效。上面的预告片里两者都能看到。",
  "MiraiX で Olden Flames のインターフェースとビジュアルエフェクトを担当しています。画面上の HUD やメニュー、そして世界の中の炎・魔法・ヒットエフェクト。上のトレーラーでどちらも見られます。")
E("YouTube channel ↗", "YouTube 频道 ↗", "YouTube チャンネル ↗")
E("The paper as a walkable exhibition in Unreal Engine: figures on the walls, the dynamics in the room.",
  "把论文做成 Unreal Engine 里可以走动的展厅：图放在墙上，动力学在房间里跑。", "論文を Unreal Engine の歩ける展示室に。図は壁に、ダイナミクスは部屋の中に。")
E("Unreal Engine · Research demo", "Unreal Engine · 研究演示", "Unreal Engine · 研究デモ")
E("My role: concept, level design and build · Unreal Engine 5", "我的角色：构思、关卡设计与制作 · Unreal Engine 5", "担当：構想・レベルデザイン・制作 · Unreal Engine 5")
E("I turned my own paper into a walkable level: figures on the walls, the dynamics running in the room, a character guiding you through. Probably one of the first ML papers presented this way.",
  "我把自己的论文做成了一个可以走进去的关卡：图挂在墙上，动力学在房间里运行，还有一个角色带你逛。大概是最早用这种方式展示机器学习论文的尝试之一。",
  "自分の論文を歩けるレベルにしました。図は壁に、ダイナミクスは部屋で動き、キャラクターが案内してくれます。機械学習の論文をこの形で発表した、たぶん最初期の試みです。")
E("Research topic →", "研究方向 →", "研究テーマ →")
E("Paper (under review) →", "论文（审稿中） →", "論文（査読中） →")
E("Science communication", "科学传播", "サイエンスコミュニケーション")
E("Segmentation", "图像分割", "セグメンテーション")
E("Speak, get corrected, hear the reply. Everything runs on the local machine.",
  "开口说，得到纠正，再听回复。一切都在本地机器上运行。", "話して、直してもらって、返事を聞く。すべてローカルマシンで動きます。")
E("Open source · Local AI app", "开源 · 本地 AI 应用", "オープンソース · ローカルAIアプリ")
E("Self-hosted speaking practice over LAN or Tailscale · alpha", "通过局域网或 Tailscale 自托管的口语练习 · alpha", "LAN や Tailscale で使えるセルフホスト型の会話練習 · アルファ版")
E("You talk in Japanese or English, the app transcribes it, a local language model answers as a tutor with corrections, and the reply is spoken back. Topic starters, adjustable correction intensity, saved history, works from a phone on the home network. No cloud, no API keys.",
  "你用日语或英语说话，应用把它转成文字，本地语言模型以老师的身份回答并纠错，再把回复读出来。有话题提示、可调的纠错强度、历史记录，手机在家庭网络里也能用。不用云，不用 API key。",
  "日本語か英語で話すと、アプリが文字起こしをし、ローカルの言語モデルが先生として添削つきで答え、その返事を音声で読み上げます。話題の提案、添削の強さ調整、履歴の保存に対応し、家庭内ネットワークならスマホからも使えます。クラウドも API キーも不要。")

# ---------------------------------------------------------------- music
E("Now playing", "正在播放", "再生中")
E("Jun 2026 · 5:46 · 760 views", "2026年6月 · 5:46 · 760 次播放", "2026年6月 · 5:46 · 760 回再生")
E("views", "次播放", "回再生")
E("Pick any cover below to play it here. The player streams from Bilibili, so it is fast in China and a little slower elsewhere.",
  "点击下面任意一首，在这里播放。播放器从 Bilibili 拉流，在中国很快，其他地区稍慢。",
  "下のカバーを選ぶとここで再生されます。プレーヤーは Bilibili から配信されるため、中国では速く、それ以外の地域では少し遅めです。")
E("Watch on Bilibili ↗", "在 Bilibili 观看 ↗", "Bilibili で見る ↗")
E("All covers", "全部翻唱", "すべてのカバー")
for _m, _zh in (("Jan", "1"), ("Feb", "2"), ("Mar", "3"), ("Apr", "4"), ("May", "5"), ("Jun", "6"), ("Jul", "7"), ("Aug", "8"), ("Sep", "9"), ("Oct", "10"), ("Nov", "11"), ("Dec", "12")):
    for _y in ("2025", "2026", "2027"):
        E(f"{_m} {_y}", f"{_y}年{_zh}月", f"{_y}年{_zh}月")
E("Ballad ver.", "Ballad 版", "バラード ver.")
E("Ballad ver. · Mar 2026", "Ballad 版 · 2026年3月", "バラード ver. · 2026年3月")
E("“Feelin’ Good” at Nissan Stadium ver.", "“Feelin’ Good” 日产体育场版", "“Feelin’ Good” 日産スタジアム ver.")
E("“Feelin’ Good” at Nissan Stadium ver. · Feb 2026", "“Feelin’ Good” 日产体育场版 · 2026年2月", "“Feelin’ Good” 日産スタジアム ver. · 2026年2月")
E("Live at the IRCN welcome party", "IRCN 迎新会现场", "IRCN 歓迎会でのライブ")
E("Live at the IRCN welcome party · Dec 2025", "IRCN 迎新会现场 · 2025年12月", "IRCN 歓迎会でのライブ · 2025年12月")
E("first take", "初版", "初回テイク")
E("first take · Oct 2025", "初版 · 2025年10月", "初回テイク · 2025年10月")
E("with the 花 intro", "带《花》前奏", "「花」のイントロつき")
E("with the 花 intro · Aug 2025", "带《花》前奏 · 2025年8月", "「花」のイントロつき · 2025年8月")
E("Piano &amp; voice<br>Okayama soul<br>5.5M on YouTube", "钢琴与歌声<br>冈山灵魂乐<br>YouTube 550万订阅", "ピアノと歌<br>岡山発のソウル<br>YouTube 登録者 550万")
E("Singer-songwriter<br>Piano ballads<br>295K on YouTube", "唱作人<br>钢琴抒情曲<br>YouTube 29.5万订阅", "シンガーソングライター<br>ピアノバラード<br>YouTube 登録者 29.5万")
E("Alt-rock trio<br>Shoegaze warmth<br>470K on YouTube", "另类摇滚三人组<br>温暖的 shoegaze<br>YouTube 47万订阅", "オルタナロック・トリオ<br>あたたかなシューゲイズ<br>YouTube 登録者 47万")
E("Singer-songwriter<br>Big ballads<br>1.3M on YouTube", "唱作人<br>大气抒情曲<br>YouTube 126万订阅", "シンガーソングライター<br>壮大なバラード<br>YouTube 登録者 126万")
E("n-buna &amp; suis<br>Literary pop<br>4.0M on YouTube", "n-buna &amp; suis<br>文学感流行乐<br>YouTube 400万订阅", "n-buna &amp; suis<br>文学的なポップ<br>YouTube 登録者 400万")

# ---------------------------------------------------------------- topic pages (shared chrome)
E("← Research interests", "← 研究方向", "← 研究テーマ")
E("Research topic", "研究方向", "研究テーマ")
E("Links to related works", "相关工作链接", "関連する業績")
E("Related works", "相关工作", "関連業績")
E("Paper", "论文", "論文")
E("Scientific Reports, under review", "Scientific Reports，审稿中", "Scientific Reports、査読中")
E("IEEE TPAMI, under review", "IEEE TPAMI，审稿中", "IEEE TPAMI、査読中")
E("In submission, 2025", "投稿中，2025", "投稿中、2025")
E("Manuscript in preparation, 2026 · soon to submit", "撰写中，2026 · 即将投稿", "執筆中、2026 · 投稿予定")
E("Talk · AICCC 2022, Osaka", "报告 · AICCC 2022，大阪", "講演 · AICCC 2022、大阪")
E("IPSJ 86th National Convention, 2024 · with Masato Osugi", "情報処理学会第86回全国大会，2024 · 与 Masato Osugi 合作", "情報処理学会第86回全国大会、2024 · Masato Osugi と共著")
E("Poster · Photonic Computing Symposium, NICT, 2024", "海报 · 光计算研讨会，NICT，2024", "ポスター · 光コンピューティングシンポジウム、NICT、2024")
E("Talk &amp; poster · IRCN Retreat, 2025", "报告 &amp; 海报 · IRCN Retreat，2025", "講演 &amp; ポスター · IRCN リトリート、2025")
E("Poster · NEURO2026, Kobe", "海报 · NEURO2026，神户", "ポスター · NEURO2026、神戸")
E("Talk · IRCN Team Salon, 2026", "报告 · IRCN Team Salon，2026", "講演 · IRCN チームサロン、2026")
E("Poster · IRCN–NTU Joint Symposium, Singapore, 2026", "海报 · IRCN–NTU 联合研讨会，新加坡，2026", "ポスター · IRCN–NTU 合同シンポジウム、シンガポール、2026")
E("Open the interactive companion site ↗", "打开交互式伴随网站 ↗", "インタラクティブなコンパニオンサイトを開く ↗")
E("Run the model in your browser: turn the noise knob and watch the simulated rare-event rate approach the target.",
  "在浏览器里运行模型：转动噪声旋钮，看模拟出的稀有事件率逐渐逼近目标。",
  "ブラウザでモデルを動かす：ノイズのつまみを回すと、シミュレーションの稀な事象の発生率が目標に近づいていきます。")
E("SyncMap: self-organizing chunking of a temporal stream", "SyncMap：对时间流的自组织分块", "SyncMap：時系列ストリームの自己組織化チャンキング")
E("SODE dynamics", "SODE 动力学", "SODE のダイナミクス")
E("Adaptability under changing corruption", "在变化的损坏下的适应能力", "変化する劣化への適応")
E("Xenovert tracking a shifting distribution", "Xenovert 跟踪不断偏移的分布", "分布のシフトを追う Xenovert")

# ---------------------------------------------------------------- topic paragraphs
E("Bio-inspired systems that leverage self-organization and nonlinear dynamical principles for complex sequential learning. SODE employs attractor–repeller dynamics driven by Hebbian and anti-Hebbian rules, so that temporal structure in an input stream is chunked and represented without an objective function or back-propagation. The framework is robust to imbalanced and hierarchical structure and adapts online as the world changes.",
  "利用自组织与非线性动力学原理进行复杂序列学习的类脑系统。SODE 采用由 Hebbian 与反 Hebbian 规则驱动的吸引子–排斥子动力学，使输入流中的时间结构无需目标函数和反向传播即可被分块并表示。该框架对不平衡与层级结构具有鲁棒性，并能随世界的变化在线适应。",
  "自己組織化と非線形力学の原理を活かして複雑な系列を学習する、生物に着想を得たシステムです。SODE はヘッブ則と反ヘッブ則に駆動されるアトラクター・リペラーのダイナミクスを用い、入力ストリーム中の時間構造を目的関数や誤差逆伝播なしにチャンク化して表現します。不均衡な構造や階層構造にも頑健で、世界の変化に合わせてオンラインで適応します。")
E("Extending SODE with random-network feature generation for spatial segmentation. The resulting unsupervised image segmentation system keeps working under severe noise and corruption, in the spirit of human vision and Gestalt principles: regions are grouped by the dynamics of the representation rather than by a trained decoder, so there is nothing to overfit and nothing to retrain when the input distribution changes.",
  "在 SODE 的基础上引入随机网络特征生成，用于空间分割。所得到的无监督图像分割系统在严重噪声与损坏下依然工作，遵循人类视觉与格式塔原则的精神：区域由表征的动力学来分组，而不是由训练出的解码器决定，因此既没有可过拟合的东西，输入分布变化时也无需重新训练。",
  "SODE にランダムネットワークによる特徴生成を組み合わせ、空間的なセグメンテーションに拡張したものです。得られた教師なし画像セグメンテーションは、強いノイズや劣化のもとでも動き続けます。人の視覚やゲシュタルトの原理に倣い、領域は学習済みのデコーダではなく表現のダイナミクスによってまとめられるため、過学習するものがなく、入力分布が変わっても再学習は不要です。")
E("An adaptive algorithm inspired by biological flexibility for online adjustment to distribution shift. Xenovert grows a perfect binary tree that maps a source distribution onto its shifted target while preserving the relationships that downstream operations depend on, so a model trained once keeps working as its inputs drift, without labels and without retraining.",
  "受生物灵活性启发的自适应算法，用于在线应对分布偏移。Xenovert 生长出一棵完美二叉树，把源分布映射到偏移后的目标分布，同时保留下游操作所依赖的关系，因此一次训练好的模型在输入漂移时仍能工作，无需标签，也无需重新训练。",
  "生物の柔軟さに着想を得た、分布シフトにオンラインで対処する適応アルゴリズムです。Xenovert は完全二分木を成長させ、元の分布をシフト後の分布へ写像しながら、下流の処理が依存する関係を保ちます。そのため一度学習したモデルは、入力がずれてもラベルなし・再学習なしで動き続けます。")
E("Comprehensive frameworks for bio-inspired sparse recurrent neural networks. Reservoir computing keeps a fixed, richly nonlinear dynamical system and trains only a readout, which makes it cheap to train and natural to implement in physical substrates such as photonics. My work surveys the field beyond machine learning and replaces the usual linear readout with local Hebbian prototype learning, so the readout self-organizes on top of the reservoir dynamics.",
  "面向类脑稀疏循环神经网络的整体框架。储备池计算保持一个固定而丰富的非线性动力系统，只训练读出层，因此训练成本低，也很自然地能在光子学等物理载体中实现。我的工作综述了该领域在机器学习之外的应用，并用局部 Hebbian 原型学习取代常见的线性读出，让读出层在储备池动力学之上自组织形成。",
  "生物に着想を得た疎な再帰型ニューラルネットワークのための包括的な枠組みです。リザバーコンピューティングは固定された豊かな非線形力学系をそのまま使い、読み出し部だけを学習するため、学習が安価で、フォトニクスなどの物理基板にも自然に実装できます。私の研究では、機械学習の外側まで含めてこの分野を概観し、通常の線形読み出しを局所的なヘッブ型プロトタイプ学習に置き換えて、読み出しがリザバーのダイナミクスの上で自己組織化するようにしました。")
E("How does a brain build a faithful model of the world from limited experience? Sensory input is finite and working memory is bounded, so rare events are sampled far more sparsely than common ones, and a model learned under these conditions inherits biased priors. In collaboration with KTH, I study this with a Bayesian Confidence Propagation Neural Network (BCPNN), a brain-like attractor network with a modular hypercolumn architecture, trained on event sequences from a Markov world with controlled probabilities. Trained on limited samples, the network systematically over- or under-estimates rare events. Injecting a moderate amount of noise into its internal simulation corrects both the unconditional and the transition statistics, and widens the parameter regime in which the internal model stays accurate. The result points to stochastic “mental simulation” as a mechanism by which the brain compensates for biased experience, with neural noise as intrinsic variability and tonic neuromodulation as the control over how fast priors update and how strongly they bias replay.",
  "大脑如何从有限的经验中构建忠实的世界模型？感觉输入是有限的，工作记忆也有上限，因此稀有事件的采样远比常见事件稀疏，在这种条件下学到的模型会继承有偏的先验。我与 KTH 合作，用贝叶斯置信传播神经网络（BCPNN）——一种具有模块化超柱结构的类脑吸引子网络——在概率受控的马尔可夫世界生成的事件序列上研究这个问题。在有限样本上训练后，网络会系统性地高估或低估稀有事件。向其内部模拟注入适量噪声，既能校正无条件统计也能校正转移统计，并拓宽内部模型保持准确的参数区间。这一结果指向随机的“心理模拟”作为大脑补偿有偏经验的一种机制：神经噪声对应内在变异性，而紧张性神经调质则控制先验更新的快慢及其对回放的影响强度。",
  "脳は限られた経験から、どのように忠実な世界モデルを作るのでしょうか。感覚入力は有限で作業記憶にも上限があるため、稀な事象はよくある事象よりはるかにまばらにしか経験されず、その条件で学ばれたモデルは偏った事前分布を受け継ぎます。KTH との共同研究で、モジュール化されたハイパーカラム構造を持つ脳型アトラクターネットワークであるベイズ確信度伝播ニューラルネットワーク（BCPNN）を、確率を制御したマルコフ世界が生成する事象列で学習させ、この問題を調べています。限られたサンプルで学習したネットワークは、稀な事象を系統的に過大または過小に推定します。ところが内部シミュレーションに適度なノイズを加えると、無条件統計と遷移統計の両方が補正され、内部モデルが正確であり続けるパラメータ領域も広がります。この結果は、偏った経験を脳が補う仕組みとしての確率的な「メンタルシミュレーション」を示唆します。神経ノイズは内在的な変動性に、持続性の神経調節は事前分布の更新速度と再生への影響の強さの制御に対応します。")

# ---------------------------------------------------------------- Traditional Chinese: OpenCC (Taiwan phrases) + overrides
from opencc import OpenCC  # noqa: E402
cc = OpenCC("s2twp")
OVERRIDE_HANT = {  # term choices after conversion, TW usage
    "网络": "網路", "信息": "資訊", "数据": "資料", "软件": "軟體", "视频": "影片", "算法": "演算法",
    "概率": "機率", "先验": "先驗", "贝叶斯": "貝氏", "模拟": "模擬", "在线": "線上", "鲁棒": "穩健",
    "参数": "參數", "对抗攻击": "對抗攻擊", "反向传播": "反向傳播", "分布": "分佈", "博士后": "博士後",
    "程序": "程式", "计算机视觉": "電腦視覺", "存储": "儲存", "接口": "介面",
}
ZH_HANT = {}
for k, v in ZH.items():
    t = cc.convert(v)
    for a, b in OVERRIDE_HANT.items():
        t = t.replace(cc.convert(a), b)
    ZH_HANT[k] = t

for name, d in (("zh-Hans", ZH), ("zh-Hant", ZH_HANT), ("ja", JA)):
    (HERE / f"{name}.json").write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")
    print(name, len(d), "entries")
