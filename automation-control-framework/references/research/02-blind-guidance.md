# 导盲领域权威论文调研

> 调研日期: 2026-05-19
> 覆盖范围: 电子旅行辅助设备(ETAs)、穿戴式设备、计算机视觉、深度学习、传感器融合、人机交互反馈、定位技术、数据集与评估标准

---

## 综述论文 (Surveys)

1. **Wearable Obstacle Avoidance Electronic Travel Aids for Blind: A Survey** | D. Dakopoulos, N.G. Bourbakis | 2010 | *IEEE Trans. Systems, Man, and Cybernetics -- Part C, 40(1):25-35* | ~490 citations | 该领域引用量最高的基础性综述，建立了穿戴式避障ETA的分类体系，将盲人导航系统分为电子旅行辅助(ETA)、电子定向辅助(EOA)和定位设备(PLD)三类，提出定性定量评估标准。

2. **Navigation Systems for the Blind and Visually Impaired: Past Work, Challenges, and Open Problems** | Santiago Real, Alvaro Araujo | 2019 | *Sensors, 19(15):3404* | ~141 citations | 从历史视角全面回顾盲人导航系统（1940年代声纳设备到现代深度学习），突出智能手机+摄像头平台、SLAM和触觉显示为关键未来方向。

3. **Sensor-Based Assistive Devices for Visually-Impaired People: Current Status, Challenges, and Future Directions** | Wafa Elmannai, Khaled Elleithy | 2017 | *Sensors, 17(3):565* | ~333 citations | 系统性综述传感器类辅助设备（超声波、红外、RFID、视觉、GPS），比较其性能、优缺点和准确度。

4. **Wearable Assistive Devices for Visually Impaired: A State of the Art Survey** | Ruxandra Tapu, Bogdan Mocanu, Titus Zaharia | 2020 | *Pattern Recognition Letters, 137:37-52* | ~157 citations | 聚焦可穿戴形式的现代综述，重点涵盖深度学习在实时助盲系统中的应用，建立了基于盲人社群意见的评估标准。

5. **An Insight into Assistive Technology for the Visually Impaired and Blind People: State-of-the-Art and Future Trends** | Bhowmick, Hazarika | 2017 | *Journal on Multimodal User Interfaces, 11(2):149-172* | 多模态界面辅助技术的综述，建立分类框架并分析未来趋势。

6. **Smartphone-Based Computer Vision Travelling Aids for Blind and Visually Impaired Individuals: A Systematic Review** | Budrionis, Plikynas, Daniušis, Indriulionis | 2022 | *Assistive Technology, 34(2):178-194* | 对智能手机端ETA的PRISMA系统综述，揭示用户需求与学术研发之间的显著错配，指出深度神经网络和触觉界面使用严重不足。

7. **Wearable Obstacle Avoidance Electronic Travel Aids for Blind and Visually Impaired Individuals: A Systematic Review** | Peijie Xu, Gerard A. Kennedy, Fei-Yi Zhao, Wen-Jing Zhang, Ron van Schyndel | 2023 | *IEEE Access, 11:66587-66613* | PRISMA系统综述89篇2020-2023年文章，覆盖超声波、红外、激光、计算机视觉等技术，从硬件成本、用户体验等维度评估。

8. **Assistive Systems for Visually Impaired Persons: Challenges and Opportunities for Navigation Assistance** | Gabriel Iluebe Okolo, Turke Althobaiti, Naeem Ramzan | 2024 | *Sensors, 24(11):3572* | 全面综述AI目标检测、IoT导航和多模态出行方案，涵盖RGB-D、超声波、RFID等多种传感器。

9. **Technological Advancements in Human Navigation for the Visually Impaired: A Systematic Review** | (多位作者) | 2025 | *Sensors, 25(7):2213* | PRISMA 2020方法论系统综述58篇文章(2019-2024)，79%的论文包含实验验证。涵盖智能手机、AI/深度学习、触觉系统和导航算法。

10. **SLAM for Visually Impaired Navigation: A Systematic Literature Review of the Current State of Research** | Marziyeh Bamdad et al. | 2022-2024 | *arXiv (v6, Aug 2024)* | 首篇系统性综述54项基于SLAM的视障导航方案，附有视障人士全球问卷调查。

11. **Multi-Sensor Data Fusion Solutions for Blind and Visually Impaired: Research and Commercial Navigation Applications** | Theodorou P, Tsiligkos K, Meliones A | 2023 | *Sensors, 23(12)* | 比较文献中多传感器融合方案与商业应用(Blindsquare, Lazarillo, Ariadne GPS)，计算机视觉与深度学习为主要发展趋势。

12. **A Survey of Assistive Technologies and Applications for Blind Users on Mobile Platforms** | Csapo, Wersenyi, Nagy, Stockman | 2015 | *Journal on Multimodal User Interfaces, 9(4):275-286* | 奠定移动平台辅助技术研究基础的早期综述。

13. **A Survey on Recent Advances in AI and Vision-Based Methods for Helping and Guiding Visually Impaired People** | Walle, De Runz, Serres et al. | 2022 | *Applied Sciences, 12(5):2308* | 综述CNN等AI视觉方法在视障辅助中的应用和趋势。

14. **Impact of Apps as Assistive Devices for Visually Impaired Persons** | Pundlik, Shivshanker, Luo | 2023 | *Annual Review of Vision Science* | 综述数百款视力辅助移动App，强调手机相对于专用设备的优势：价格低、多功能、普及性高。

15. **A Survey on Outdoor Navigation Applications for People With Visual Impairments** | (NCBI Ireland) | 2023 | *IEEE Access, 11:14647-14666* | 49名视障人士问卷调查表明63%曾在户外导航中受伤，揭示交通灯、十字路口检测等关键缺口。

16. **A Qualitative and Quantitative Analysis of Research in Mobility Technologies for Visually Impaired People (1946-2022)** | (多位作者) | 2023 | *IEEE Access, 11:82496-82520* | 140篇论文大规模综述，75年跨度，光学/声学传感器辅助平均62%性能，多传感器融合最有前景(51%)。

17. **Recent Trends in Computer Vision-Driven Scene Understanding for VI/Blind Users: A Systematic Mapping** | Mohammad Moeen Valipoor, Angelica de Antonio | 2022 | *Universal Access in the Information Society* | 涵盖4.5年进展的系统映射研究，综述目标识别、障碍检测和场景理解前沿。

---

## 经典电子旅行辅助设备 (Classic ETAs)

1. **Ultrasonic Torch (Kay Sonic Torch)** | Leslie Kay | 1959/1965 | 新西兰 | 世界首个电子旅行辅助设备，利用高频超声波脉冲探测环境，将回声转换为可听声信号。奠定了此后所有超声波ETA的基础。

2. **Sonicguide (Binaural Sensory Aid)** | Leslie Kay | 1965-1966 | 眼镜框架式 | 基于超声波Torch的进化版：眼镜中央发射超声波，左右各一个接收器，通过耳机实现双耳空间定位。可感知物体材质/表面纹理，探测距离约5.5米。

3. **C-5 Laser Cane** | Malvern Benjamin | 1966 | Bionic Instruments/Nurion | 世界上首个激光导盲杖，内置三个砷化镓激光束：前向(8ft)、上向(5.5ft)和下向(落差分检测)。三种不同音调区分方向。1989年调查中约10%的ETA用户以其为主设备，目前停产。

4. **Mowat Sensor** | Geof Mowat | 1977 | 新西兰 | 手持式小型超声波障碍检测器，完全以振动输出（无声），特别适合视听双重障碍者。距离越近振动越强，支持1m/4m两种量程。1989年调查中最常用的ETA之一。

5. **Pathsounder** | Lindsay Russell | 1964 | 胸挂式 | 最早期的"通行/停"二进制检测系统，无方向性信息。

6. **Nottingham Obstacle Detector** | 1973 | 英国 | 早期超声波障碍检测器之一。

---

## 商业产品/系统 (Commercial Systems)

1. **NavCog (IBM Research & CMU)** | Ahmetovic, Gleason, Ruan, Kitani, Takagi, Asakawa | 2016-2019 | *MobileHCI 2016; ACM TACCESS 12(3), 2019* | 基于BLE信标的智能手机室内导航系统，每10m部署信标。在大型商场(200+ BLE, 53人)和酒店会议(37人, 280次行程, 30km)中验证。由盲人IBM Fellow Chieko Asakawa领导开发。

2. **CaBot (CMU)** | Guerreiro, Sato, Asakawa, Dong, Kitani, Asakawa | 2019 | *ACM ASSETS 2019* | 自主导航行李箱式机器人，LiDAR(VLP-16)+RealSense摄像头，ROS2+Cartographer+WiFi/BLE定位。用户将其体验评价为可与导盲犬媲美。开源(github.com/CMU-cabot/cabot)。

3. **GuideCopter** | Huppert, Hoelzl, Kranz (Univ. Passau) | 2021 | *ACM CHI 2021* | 基于无人机的触觉导引界面，通过物理系绳传递力度反馈，实现手部物体定位精导，比音频引导更精确。

4. **OrCam MyEye 2 Pro** | (OrCam Technologies, 以色列) | ~$4,250 | 离线智能眼镜，文本阅读(平面文本强，手写体差)，柱状文本阅读能力优异。2025年TVST研究：25名参与者评估，73%无法完成文本任务的参与者在AI辅助下可完成。

5. **Envision Glasses** | (Envision, 荷兰) | ~$2,499 | 基于Google Glass Enterprise Edition 2的智能眼镜，需WiFi用于高级功能。文字阅读和搜索识别能力出色，支持处方镜片集成。

6. **Seeing AI** | (Microsoft) | 免费iOS | 表现最全面的免费方案，2025年研究中的系统可用性评分(SUS)最高。手写识别能力突出。搜索识别场景时90%的参与者获得能力提升。

7. **Google Lookout** | (Google) | 免费Android | Android平台主要方案，文本阅读能力强，但柱状文本和搜索识别能力相对较弱。

8. **Aira** | (Aira Tech Corp) | 商业远程人工辅助服务 | 视障用户通过视频通话连接明眼人代理，获取实时导航和视觉描述。由UConn/USDOT进行学术评估(2023)。

9. **AI Suitcase (Shimizu Version)** | CAAMP Consortium (IBM Japan, Shimizu, Mitsubishi等) | 2023 | *IEEE* | CaBot商用化版本：AI行李箱式导航机器人，支持室内外多种变体。

---

## 穿戴式辅助设备 (Wearable Devices)

1. **SightAid: Deep Learning-Based Intelligent Wearable Vision System** | Talaat Fatma M., Farsi Mohammed, Badawy Mahmoud, Elhosseini Mostafa | 2024 | *Neural Computing & Applications, 36(19):11075-11095* | AR智能眼镜集成七阶段深度学习框架，准确率高达0.9874，AUC-ROC达0.9999，结合音频/触觉反馈，针对KSA地区设计。

2. **SonicGlass: Obstacle Detection & Navigation Using Smartglass-Based Ultrasonic Sensors** | BITS Pilani | 2024 | *IEEE COMSNETS 2024, pp.603-607* | 3D打印智能眼镜配超声波传感器，10人用户研究显示障碍检测F1=84.7%（精确率100%），室内定位误差1.35m。

3. **Multi-Sensory Visual-Auditory Fusion of Wearable Navigation Assistance for People With Impaired Vision** | Song Yang, Lian Zhi, Liu Guoxin, Wang Binglu, Zhu Min, Shi Peng | 2023 | *IEEE Trans. Automation Science and Engineering* | 电子眼镜实现视觉-听觉融合室内导航，结合目标检测、路径规划和神经网络。

4. **Sensing and Navigation of Wearable Assistance Cognitive Systems for the Visually Impaired** | Guoxin Li, Jiaqi Xu, Zhijun Li et al. | 2023 | *IEEE* | 配备RGB-D相机、嵌入式计算机和触觉模块的可穿戴视觉系统，实现室内环境感知。

5. **5G and IoT Collaborate to Improve Smart Glasses for the Visually Impaired** | Abdulqader Faris Abdulqader, Ali Qutaiba Abdulrazzaq et al. | 2024 | *FRUCT 36, pp.159-167* | 探索5G低延迟如何赋能智能眼镜的实时物体识别、文本转语音翻译和导航支持。

6. **Facial Recognition Smart Glasses for Visually Impaired People** | Asha Ghodake et al. | 2023 | *IEEE ICCUBEA 2023* | 智能眼镜实现面部识别社交辅助功能，帮助视障者感知社交环境。

7. **Smart Glass for Visually Impaired Using Mobile App** | Anitha T., Rukkumani V. et al. | 2023 | *Springer LNDE, 131:403-411* | 低成本超声波传感器智能眼镜配云端数据存储和手机App，支持位置追踪和紧急通知。

8. **Smart Vision: A Unified System for Enhanced Navigation and Accessibility** | 2024 | *IEEE ICAC2N, pp.284-288* | 智能眼镜+智能鞋生态系统，含Raspberry Pi、持续图像捕获、距离传感和语音交互。

9. **Smart Obstacle-Detecting Accessory for White Cane** | 2025 | *Journal on Multimodal User Interfaces* | 可附加于传统白杖的智能配件，超声波测距+触觉/听觉反馈。103名墨西哥盲人访谈指导设计，试点研究显示步行速度提升29%，零事故。

10. **A Self-Powered Smart White Cane Using a Triboelectric Nanogenerator (TENG)** | Heewon Song, Swati Panda, Sugato Hajra et al. (DGIST) | 2024 | *Energy Technology, 12(7)* | 自供电(无电池)智能白杖，输出155V/4.5μA，结合机械发光材料实现低光照可见性，数字信号处理实现障碍物识别。

11. **Augmented White Cane with Multimodal Haptic Feedback** | 2024 | *IEEE* | 在传统白杖手柄上附加惯性轮（模拟与远处物体的碰撞脉冲反馈）和三电机振动阵列，可实现头部高度障碍物检测。

12. **SEES: Smart Environment Explorer Stick** | 2024 | *IEEE* | 多传感器上下文感知智能杖，整合有源环境传感，兼具定向和行动辅助功能。

13. **Self-Reported Use of Technology by Orientation and Mobility Clients in Australia and Malaysia** | Lil Deverell, Jahar Bhowmik et al. | 2023 | *British Journal of Visual Impairment, 41(1):33-48* | 发现智能手机已成为标准出行辅助工具，参与者识别出108款用于出行的App。

---

## 计算机视觉方法 (Computer Vision Methods)

1. **YOLO-OD: Obstacle Detection for Visually Impaired Navigation Assistance** | Wei Wang, Bin Jing, Xiaoru Yu et al. | 2024 | *Sensors, 24(23):7621* | 提出Feature Weighting Block (FWB)区分不同尺寸障碍物特征重要性，Adaptive Bottleneck Block (ABB)处理户外杂乱环境，Enhanced Feature Attention Head (EFAH)提升小目标检测，在公开数据集上达到30.02% mAP。

2. **SGBM_YOLO: A High-Precision Obstacle Detection Algorithm Based on Stereo Vision and Spatial Attention Mechanism** | Guoqi Heng, Kexue Sun, Shuo Huang et al. | 2025 | *Applied Soft Computing* | YOLO+双目立体视觉(SGBM)结合实现深度感知障碍检测，提出SPDConv保留通道维度。发布BlindData数据集(8类: 人、自行车、汽车、斑马线、红绿灯、盲道、坑洼)。比YOLOv8m高4.2%，深度测量误差仅3.6%。

3. **Enhanced Footpath Segmentation Using Attention-Integrated UNET For Assistive Urban Navigation** | 2025 | *IEEE* | 改进UNET含空间和通道注意力机制，步道分割IoU达89.82%，高斯噪声/模糊下IoU仍大于85.32%，每帧50ms实时反馈。

4. **AMT-Net: Attention-based Multi-Task Network for Scene Depth and Semantics Prediction in Assistive Navigation** | 2025 | *Neurocomputing* | CNN+Vision Transformer统一单解码器架构，联合语义分割和单目深度估计。提出CSAPP(Cascaded Self-Attention Pyramid Pooling)和RSAB(Residual Self-Attention Bottleneck)两个新模块。在NYUD-v2和TrueSight数据集上达到最先进性能。

5. **CSN: A Compact Semantic Segmentation Network for Visual Scene Perception in Assistive Navigation** | 2026 | *Computer Vision and Image Understanding* | 轻量级分割模型(8.41M参数)，在TrueSight数据集上达到60.99% mIoU，实时推理52.59 FPS，专为移动助盲设备设计。

6. **A Blind Navigation Guide Model for Obstacle Avoidance Using Distance Vision Estimation Based YOLO-V8n** | Ebere Uzoka Chidi, Edward Anoliefo et al. | 2025 | *J. Nigerian Society of Physical Sciences* | YOLO-V8n+WFE(加权特征增强)+Bi-FPN+WIoU损失函数，开发DVE(距离视觉估计算法)实现同步检测和距离测量。

7. **Real-Time Obstacle Recognition for Visually Impaired Using HOG + BoVW** | | *IEEE* | 使用图像网格兴趣点+多尺度Lucas-Kanade跟踪+HOG描述符+词袋模型(BoVW)实现智能手机室内外障碍物分类。

8. **Negative Obstacle Detection (Drop-offs, Curbs, Stairs) Using Stereo Vision** | | *Springer* | 两阶段动态规划(TSDP)计算视差图，专门检测负障碍(坑洞、路缘、向下楼梯)，比随机生长对应种子(GCS)算法快28%。

9. **Pedestrian Detection with Wearable Cameras for the Blind: A Two-way Perspective** | | 2020 | *PMC* | 从穿戴式摄像头视角研究为盲人检测行人，双向视角方法。

10. **Accessing Passersby Proxemic Signals through a Head-Worn Camera: Opportunities and Limitations for the Blind** | | 2022 | *ACM* | 头部穿戴摄像头用于感知路人空间信号的研究，探索社交导航。

11. **All_Aboard: Bus Stop Localization App** | Pundlik S., Shivshanker P., Traut-Savino T., Luo G. | 2024 | *Translational Vision Science & Technology* | 基于深度学习的公交站定位App，24名法定盲人测试：成功率91% vs Google Maps 52%，平均终点距离1.8m vs 7m。解决了"最后30英尺"微导航问题。

---

## 深度学习方案 (Deep Learning)

1. **DEEP-SEE: Joint Object Detection, Tracking and Recognition with Application to Visually Impaired Navigational Assistance** | Tapu, Mocanu, Zaharia | 2017 | *Sensors, 17(11):2473* | 里程碑式论文，演示CNN如何嵌入可穿戴助盲系统实现实时目标检测、跟踪和识别。

2. **Infrastructure Enabled Guided Navigation for Visually Impaired** | 2025 | *IEEE Trans. Intelligent Transportation Systems* | 穿戴式RGB-D+Jetson Orin NX，轻量语义分割CNN(71.2 mIoU Cityscapes, 74.46 mIoU Camvid, 50FPS)+深度解码器。实际视障参与者测试高成功率。

3. **Traffic Sign Detection and Navigation System for Visually Impaired Using AI** | 2025 | *ICISD 2025* | RetrievaNet-43自定义CNN，分类43种交通标志，针对资源受限环境优化实时性能，TTS反馈。

4. **Deep Learning for Assistive Navigation of Vision-Impaired People** | 2023 | *Univ. of Wollongong (博士论文)* | 系统性博士论文研究深度学习在视障导航中的应用。

5. **AI-Driven Navigation with Semantic Segmentation in Virtual Environments** | 2024 | *HAL* | 强化学习+语义分割，数字孪生训练实现94%无碰撞轨迹(vs 基本相机视角56%)。

6. **Efficient Real-Time Pathfinding for Visually Impaired Individuals** | 2025 | *IEEE Access* | 双分支CNN架构，72.6%准确率检测路径、路径物体和路径边界。

7. **Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation** | 2024 | *arXiv:2510.20549* | 集成SuperPoint特征提取+LightGlue特征匹配增强ORB-SLAM3，在挑战性环境中平均提升87.84%。

8. **Deep-Learning-Based Visual Aid for Low Vision** | 2025 | *IEEE* | 基于YOLOv8/v9/v10的头戴显示器(HMD)，Raspberry Pi 5实时目标检测和突出显示，评估准确度-速度-功耗权衡。

---

## 传感器融合方案 (Sensor Fusion -- RGB-D / LiDAR)

1. **NavSense: Real-Time Spatial Awareness for the Visually Impaired Using LiDAR, Depth Cameras, and AI-based Object Detection** | 2025 | *SSRN* | 融合YD LiDAR(360度水平测绘)+两个TF-Luna LiDAR+Intel RealSense D435i深度相机+YOLOv5，识别门、楼梯、出口标志等地标，TTS优先级音频反馈。

2. **多传感器融合导盲杖局部避障性导航方法** | 武汉轻工大学 | 2025 | *中国专利 CN120538538A* | RGB-D深度相机+雷达/LiDAR深度校正+SLAM+八叉树地图(OctoMap)，生成局部避障路径，语音或震动反馈。

3. **MP-SSD: Multi-path Sensory Substitution Device Navigates the Blind and Visually Impaired Individuals** | 2026 | *ScienceDirect* | 从单帧RGB图像进行3D语义场景补全(SSC)，生成稠密体素语义地图，识别关键导航点并规划最短路径，HRTF空间音频传达方向距离。

4. **pRGB-D: 偏振RGB-D框架** | J. Bai et al. | 2024-2025 | 利用偏振信息+RGB-D同时检测可通行区域和水面危险区域，增强户外安全导航。

5. **毫米波雷达 + RGB-D传感器融合** | J. Bai et al. | 2024-2025 | 融合毫米波雷达和RGB-D实现多距离、多角度障碍物检测，兼顾通用性、便携性和成本。

6. **SELM-SLAM3: 深度学习增强型视觉SLAM** | ZHAW/苏黎世大学 | 2025 | *VISIGRAPP 2025* | 基于ORB-SLAM3集成SupperPoint+LightGlue，在TUM RGB-D/ICL-NUIM/TartanAir上评估，相比ORB-SLAM3平均提升87.84%，针对低纹理、动态光照等挑战环境。

7. **Intel RealSense 可通行区域检测** | J. Bai et al. | 2024-2025 | 使用Intel RealSense R200 RGB-D传感器扩展室内外可通行区域检测，结合可穿戴智能眼镜和腰部路径查找器。

8. **Building Semantic Maps for Blind People to Navigate at Home** | 2023 | *IEEE* | 利用RGB-D传感器构建室内语义地图，辅助盲人家庭环境导航。

---

## 感官替代 (Sensory Substitution)

1. **EyeMusic: Introducing a "Visual" Colorful Experience for the Blind Using Auditory Sensory Substitution** | Sami Abboud, Shlomi Hanassy, Shelly Levy-Tzedek, Shachar Maidenbaum, Amir Amedi | 2014 | *Restorative Neurology and Neuroscience, 32(2):247-257* | 首个传递颜色信息的视觉-听觉感官替代设备(SSD)，使用五声音阶和天然乐器音色编码形状和颜色。盲人2-3小时训练后可高准确率解码。

2. **The vOICe** | Peter Meijer | 1992-ongoing | 经典的视觉-听觉SSD设备，将图像转换为"声景"：时间=水平位置，音高=垂直位置，响度=亮度。

3. **BrainPort** | Wicab / Paul Bach-y-Rita | 视觉-触觉SSD，通过舌面电极阵列将图像转换为舌部的电触觉刺激。

---

## 人机交互与反馈 (HCI and Feedback)

1. **Identification of Vibrotactile Patterns Encoding Obstacle Distance Information** | 2024 | *IEEE* | 研究触觉渲染方法（时序、时空、空间/时间/强度变化）传递障碍物距离，发现四指时空振动模式可实现高识别率和低认知负荷。

2. **Fully Digital Audio Haptic Maps for Individuals with Blindness** | Kaplan, Pyayt | 2024 | *Disabilities, 4(1)* | XBOX手柄音频触觉地图，13名盲人成功建立心理地图，训练成本极低，速度个性化对路径跟随至关重要。

3. **Guidance-SSD: Spatial Navigation with Horizontally Spatialized Sounds in Early and Late Blind Individuals** | 2021 | *PLoS ONE, 16(2):e0247448* | 智能手机SSD使用水平空间化声音编码距离(BRR Beep重复率/SFF声音基频/SI声音强度三种声化策略)。12早盲+11晚盲+24明眼蒙眼者测试，盲人导航速度快于明眼人。

4. **Exploiting the Haptic and Audio Channels to Improve Orientation and Mobility Apps for the Visually Impaired** | 2023 | *PMC* | 研究触觉+音频通道在定向与行走(O&M)App中的应用和优化。

5. **Development of an Audio-Haptic Virtual Interface for Navigation of Large-Scale Environments for People Who Are Blind** | 2016 | *Springer LNCS, 9739* | 第三代VE模拟器，使用全3D声音+震动触觉反馈，fMRI证明盲人激活与明眼人相似的空间处理脑网络，空间知识可从虚拟转移到真实世界。

6. **Different Approaches to Aiding Blind Persons in Mobility and Navigation in the "Naviton" and "Sound of Vision" Projects** | Strumillo, P. et al. | 2018 | *Springer* | 结合音频+触觉反馈的多传感器系统：触觉腰带(腹部振动传递障碍物位置)+双耳音效("气泡"声，响度=距离，音高=高度)。

7. **Echolocation as an Accessible Navigation Tool in a Virtual 3D Environment** | 2024 | *ACM ASSETS 2024* | 研究回声定位在虚拟3D环境中的导航辅助应用。

8. **Virtual Worlds Beyond Sight: Designing and Evaluating an Audio-Haptic System for Non-Visual VR Exploration** | 2025 | *ACM CHI 2025* | 结合白杖模拟(触觉纹理渲染)+全向滑台(无限行走)+物理空间化音频(遮挡/衍射/衰减)，500mx250m城市场景，20名蒙眼参与者成功完成复杂导航任务。

9. **Audomni Sensory Supplementation Feedback** | 2024 | *IEEE Access, 12:26222-26241* | 使用便携VR(Parrot-VR)和新型问卷(DoUQ-MoB)评估ETA"Audomni"，76%的视障参与者表示"非常或极有可能"想使用。

---

## 定位技术 (Localization)

1. **The Effectiveness of UWB-Based Indoor Positioning Systems for the Navigation of Visually Impaired Individuals** | Rosiak et al. | 2024 | *Applied Sciences (MDPI)* | 使用MFi认证UWB芯片组+iOS App，比较UWB vs. LiDAR精度。LiDAR动态精度更高，UWB精度足以追踪个体，推荐传感器融合处理NLoS场景。

2. **NavCog3 in the Wild: Large-scale Blind Indoor Navigation Assistant with Semantic Features** | Sato, Oh, Guerreiro, Ahmetovic, Naito, Takagi, Kitani, Asakawa | 2019 | *ACM TACCESS, 12(3), Article 14* | BLE信标指纹定位+语义特征(门、商店、电梯)，大型商场验证，10m间距信标，3-5英尺定位精度。

3. **On Indoor Localization Using WiFi, BLE, UWB, and IMU Technologies** | Leitch et al. | 2023 | *Sensors (MDPI)* | 四种室内定位技术(WiFi, BLE, UWB, IMU)的综合比较综述。

4. **Indoor Positioning Framework for Visually Impaired People Using Internet of Things** | Mahida et al. | 2019 | *Western Sydney University* | 惯性传感器(IMU)+BLE信标融合，解决无信标区域的定位问题，平均位置误差1.5-2m。

5. **An Accessible Indoor Wayfinding Application for Persons With Visual and Mobility Impairments** | Das, Gadatia et al. | 2025 | *IEEE CCWC 2025* | 基于beacon的iOS App，多线程支持多楼层扩展，针对视觉和行动障碍共同设计。

6. **GuideBeacon** | Cheraghi et al. | 2017 | | 基于beacon的室内导路系统，与视障用户实地测试。

7. **StaNavi** | Kim et al. | 2016 | | 部署于东京站(~40万日客流量)，BLE语音逐向导航。

8. **IBeaconMap: Automated Indoor Space Representation for Beacon-Based Wayfinding** | Cheraghi et al. | 2018 | | 从建筑平面图通过CV/ML自动确定最优beacon位置并生成加权连通图。

9. **FindMyWay** | Das et al. | 2024 | *ICCHP 2024* | 含探索+导航功能的iOS App，多楼层支持，并行处理。

10. **All the Way There and Back: Inertial-Based, Phone-in-Pocket Indoor Wayfinding and Backtracking Apps for Blind Travelers** | Tsai, Elyasi et al. | 2023 | | 纯惯性传感器(手机放口袋)室内导航和返程App，无基础设施依赖。

11. **YanAR Evaluation Datasets** | 2023 | *IEEE Dataport* | 多模态AR室内导航数据集，WiFi指纹+PDR轨迹(PDR-only 5.0m vs Hybrid 1.25m平均误差)。10名蒙眼参与者3条路径测试，含SUS可用性评分。

### 定位技术精度对比

| 技术 | 典型精度 | 适用场景 | 优势 | 局限 |
|------|---------|---------|------|------|
| **GPS/北斗** | 3-10m | 室外 | 全球覆盖、无基础设施 | 室内无效、城市峡谷效应 |
| **BLE信标** | 1-3m | 室内 | 低成本、手机支持、易部署 | RSSI波动、多径效应 |
| **UWB** | 10-30cm | 室内 | 高精度、抗多径 | 需专用硬件、成本高 |
| **视觉/VIO** | cm级 | 室内外 | 环境信息丰富、无基础设施 | 光照敏感、计算密集 |
| **传感器融合** | 1-2m | 室内外 | 鲁棒性强、覆盖全面 | 系统复杂度增加 |

---

## 数据集与评估标准 (Datasets)

1. **GuideDog** | 2025 | *arXiv:2503.12844* | 首个真实世界跨洲级视障导航多模态数据集：22K图像-描述对(2K人工验证)，覆盖46个国家183城市。GuideDogQA基准(818道多选题：目标识别435+深度感知383)。基于3项BLV导引标准(S1环境描述/S2障碍信息/S3综述与方向)。GPT-4o等MLLM评估显示深度感知和BLV标准遵循仍具挑战。

2. **mmWalk** | 2025 | *NeurIPS 2025 Datasets & Benchmarks Track* | CARLA模拟器多模态多视图数据集：120条轨迹、62K同步帧、559K全景图像(RGB+深度+语义)、69K VQA三元组(9类别)。覆盖8个BLV死角场景(不平路面、交叉口、窄路、高障碍、死胡同)+18个无障碍地标。所有VLM在风险评估和导航任务上都严重困难。

3. **Eye4B** | 2025 | *arXiv:2502.14883* | 人工验证BLV偏好基准：1.1K策划场景+4,979条请求。8名BLV参与者从5维度(恐惧度/不可行动性/充分性/简洁性/总体)评估6个LVLM。发现当前LVLM产生的回答未能完全反映BLV特定需求。

4. **Crucial Object Recognition Dataset** | 2024 | *BAAI* | 21段BLV个体导航视频、90个关键物体类别(经焦点小组精炼)、31段标注视频片段。发现现代CV数据集仅覆盖一小部分BLV关键物体，SOTA模型存在显著差距。

5. **TrueSight** | | 行人场景辅助导航数据集，支持语义分割和深度估计任务。AMT-Net、CSN等论文的标准评测集。

6. **NYUD-v2** | Silberman et al. | 2012 | 室内RGB-D场景理解基准数据集(语义分割+深度估计)，广泛用于助盲导航系统评估。

7. **Cityscapes** | Cordts et al. | 2016 | 城市街景语义分割标准数据集，用于评估户外导航系统性能。

8. **Camvid** | Brostow et al. | 2008 | 道路交通场景分割数据集，常用于评估穿戴式导航系统的场景理解能力。

9. **BlindData** | Heng et al. | 2025 | 配合SGBM_YOLO发布，8类标注(人、自行车、汽车、斑马线、红绿灯、盲道、坑洼)，专为视障导航设计。

10. **SideGuide / SideWalk** | | Eye4B基准的背景数据集，包含室内外真实场景。

---

## 重要期刊/会议 (Key Venues)

### 期刊 (Journals)

| 期刊名称 | 出版社 | 说明 |
|---------|--------|------|
| **Sensors** | MDPI | 该领域发表量最大的期刊，大量系统性综述和传感器方案 |
| **IEEE Access** | IEEE | 穿戴式设备和导航综述的常见发表平台 |
| **IEEE Trans. Systems, Man, and Cybernetics** | IEEE | 经典ETA综述(Dakopoulos 2010)的发表期刊 |
| **IEEE Trans. Automation Science and Engineering** | IEEE | 穿戴式导航辅助的最新发表期刊 |
| **IEEE Trans. Intelligent Transportation Systems** | IEEE | 基础设施增强导盲导航系统 |
| **Pattern Recognition Letters** | Elsevier | Tapu等(2020)高水平综述发表期刊 |
| **Computer Vision and Image Understanding** | Elsevier | 紧凑语义分割网络CSN等 |
| **Neurocomputing** | Elsevier | AMT-Net等多任务网络 |
| **Applied Soft Computing** | Elsevier | SGBM_YOLO等 |
| **Neural Computing & Applications** | Springer | SightAid等深度学习穿戴式系统 |
| **ACM Trans. Accessible Computing (TACCESS)** | ACM | 无障碍计算顶级期刊，NavCog3等 |
| **Assistive Technology** | Taylor & Francis | 智能手机CV助盲系统综述 |
| **Journal of Visual Impairment & Blindness** | SAGE | 视障康复领域经典期刊，OrCam/Seeing AI评估 |
| **British Journal of Visual Impairment** | SAGE | 视障技术应用评估 |
| **Journal on Multimodal User Interfaces** | Springer | 多模态界面综述和应用 |
| **Universal Access in the Information Society** | Springer | CV场景理解系统映射 |
| **Restorative Neurology and Neuroscience** | IOS Press | 感官替代(EyeMusic) |
| **Annual Review of Vision Science** | Annual Reviews | App辅助设备综述 |
| **Translational Vision Science & Technology** | ARVO | All_Aboard等临床翻译研究 |

### 会议 (Conferences)

| 会议名称 | 说明 |
|---------|------|
| **ACM ASSETS** | 无障碍与辅助技术领域顶级会议，NavCog、CaBot、Echolocation等关键论文 |
| **ACM CHI** | 人机交互顶级会议，GuideCopter、VR导航等交互方案 |
| **NeurIPS (Datasets & Benchmarks Track)** | mmWalk数据集等 |
| **CVPR / ICCV / ECCV** | 底层CV技术(分割、检测、深度估计)的顶级来源 |
| **ICRA / IROS** | 机器人导航辅助的国际顶会 |
| **MobileHCI** | 移动人机交互，NavCog早期版本发表 |
| **IEEE COMSNETS** | SonicGlass等传感器网络方案 |
| **FRUCT** | 5G+IoT智能眼镜等 |
| **VISIGRAPP** | SELM-SLAM3等视觉SLAM方案 |
| **ICCHP** | 计算机辅助人群国际会议，FindMyWay等 |

---

## 关键研究团队 (Key Labs)

| 团队/实验室 | 机构 | 主要贡献 |
|-----------|------|---------|
| **Chieko Asakawa Group** | CMU / IBM Research | NavCog, CaBot, AI Suitcase -- 室内/室外自主导航，开源平台 |
| **Amir Amedi Lab** | Hebrew Univ. of Jerusalem / Reichman Univ. | EyeMusic, vOICe感官替代, 盲人脑神经可塑性研究 |
| **Titus Zaharia Group** | Telecom SudParis / IP Paris | DEEP-SEE, 穿戴式助盲设备深度学习综述 |
| **Leslie Kay (已故)** | 新西兰坎特伯雷大学 | Sonic Torch, Sonicguide, K-Sonar -- ETA奠基人 |
| **Shivkumar Pundlik / Gang Luo** | Harvard / Schepens Eye Research | All_Aboard, 手机App辅助技术综述 |
| **Bourbakis Group** | Wright State University | 穿戴式ETA奠基综述, 辅助技术研究中心 |
| **J. Bai Group** | | pRGB-D, 毫米波雷达+RGB-D, 偏振感知导航 |
| **Bogdan Mocanu Group** | Univ. Politehnica of Bucharest | 穿戴式设备深度学习综述 |
| **Santiago Real / Alvaro Araujo** | Univ. Politecnica de Madrid | VES混合现实平台, 导航综述 |
| **Kris Kitani** | CMU Robotics Institute | NavCog, 第一人称视觉导航 |
| **Syed M. Billah** | Penn State University | 关键物体识别, 视障用户需求研究 |

---

## 技术趋势总结

### 传感器演进路线
超声波(1960s) -> 激光(1970s) -> GPS(1990s) -> RFID/BLE(2000s) -> 视觉/深度学习(2010s) -> RGB-D/LiDAR + SLAM(2020s) -> 多模态融合 + 大语言/视觉模型(2025+)

### 核心挑战
1. **实时性**: 嵌入式和移动端设备的低延迟推理
2. **微导航**: "最后几米"的精确引导(落差分、门口、公交站精确定位)
3. **鲁棒性**: 恶劣光照、遮挡、动态环境下的稳定性能
4. **用户接受度**: 过往ETA采纳率极低（1960年代以来），需以用户为中心设计
5. **认知负荷**: 多感官反馈的平衡，避免信息过载
6. **成本与可及性**: 专用硬件昂贵($2000-$4500)，智能手机App是主流替代方向
7. **评测标准化**: 缺乏统一的基准数据集和评测协议
8. **用户参与不足**: 82%研究未纳入BVI参与者参与设计或评估(ASSETS 2023)

### 未来方向
1. 大语言/视觉模型(LLM/LVLM)赋能自然语言场景描述与环境问答
2. 多模态传感器融合(视觉+LiDAR+IMU+UWB)提升鲁棒性
3. 基础设施协作(V2X/智慧城市集成)实现超视距感知
4. 轻量化网络+边缘计算实现完全离线实时推理
5. 个性化自适应反馈(根据用户偏好和场景动态调整模态和频率)
6. 虚实结合的用户评估框架(VR/模拟+实地长期测试)
7. 从"障碍物检测"到"场景理解与语义导航"的范式升级
