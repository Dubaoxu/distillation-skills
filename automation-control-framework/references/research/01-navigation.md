# 导航领域权威论文调研

> 调研日期: 2026-05-19
> 涵盖范围: SLAM、路径规划、传感器融合、障碍物避障、学习驱动导航
> 时间跨度: 经典基础论文 (~1987-) 至前沿研究 (2025-2026)

---

## 综述论文 (Surveys)

### 综合导航综述

1. **A Survey on Autonomous Navigation for Mobile Robots: From Traditional Techniques to Deep Learning and Large Language Models** | Khawaja et al. | 2025 | *Autonomous Robots* (Springer) | 综述了从 A*/Dijkstra 到强化学习再到大语言模型的完整导航技术演进路线。

2. **A Comprehensive Review on Autonomous Navigation** | 多位作者 | 2025 | *ACM Computing Surveys* | ~新发 | 覆盖传感器类型、机器人平台、仿真工具、路径规划/跟踪、传感器融合、避障与SLAM，强调深度学习的角色。

3. **A Comprehensive Survey on SLAM and Machine Learning Approaches for Indoor Autonomous Navigation of Mobile Robots** | 多位作者 | 2025 | *Machine Vision and Applications* (Springer) | 室内自主导航的SLAM + 机器学习方法综述，含性能评价指标。

4. **Advancing Mobile Robot Navigation with DRL and Heuristic Rewards: A Comprehensive Review** | 多位作者 | 2025 | *Neurocomputing* (Elsevier) | 深度强化学习与启发式搜索融合方法的全面综述。

### SLAM 综述

5. **Deep Learning for Visual Localization and Mapping: A Survey** | Chen et al. | 2024 | *IEEE Trans. Neural Networks and Learning Systems* | 提出基于深度学习的定位与建图分类法，覆盖学习型VO、全局重定位、建图及完整SLAM系统。

6. **How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey** | Tosi, Zhang, Gong et al. | 2024 (updated 2025) | arXiv:2402.13255 | 首篇全面综述 NeRF 与 3DGS 如何变革 SLAM，追踪从手工方法到深度学习再到隐式神经表示的演进。

7. **Monocular Visual SLAM: (R)Evolution from Geometry to Deep Learning-Based Pipelines** | 多位作者 | 2024 | *IEEE Trans. Artificial Intelligence* | 综述单目视觉 SLAM 从经典几何方法到端到端深度学习管线的变革。

8. **SLAM Meets NeRF: A Survey of Implicit SLAM Methods** | 多位作者 | 2024 | *World Electric Vehicle Journal* (MDPI) | 分析约30个基于NeRF的SLAM工作，涵盖隐式神经表示联合优化相机位姿与场景网络。

9. **A Survey of Visual SLAM in Dynamic Environment: The Evolution From Geometric to Semantic Approaches** | Wang Yanan, Tian Yaobin et al. (北航) | 2024 | *IEEE Trans. Instrumentation and Measurement* | 全面梳理从几何SLAM到语义SLAM的演进，含多传感器融合策略。

10. **Semantic Visual Simultaneous Localization and Mapping: A Survey** | 多位作者 | 2024 | arXiv:2510.00783 | 最新语义SLAM综述，涵盖定位、语义特征、建图、数据关联、回环检测、LLM集成等。

11. **A Survey of SLAM with an Envision in 6G Wireless Networks** | 武汉大学 & NTU Singapore | 2024 | arXiv | 覆盖LiDAR SLAM、视觉SLAM、传感器融合及深度学习模块，展望6G时代SLAM。

### 路径规划综述

12. **Sampling-based Path Planning Algorithms: A Survey** | Choudhary A. | 2023 | arXiv:2304.14839 | 全面综述 PRM, RRT, PRM*, RRT* 等采样规划方法及其优化变体。

13. **A Review of Path Planning Algorithms for Automated Driving Vehicles** | Zhang Yu, Li Wanlin | 2024 | *SID Symposium Digest* | 分类图搜索法(Dijkstra, A*)与采样法(PRM, RRT)，介绍Apollo算法及新兴方法。

14. **Obstacle Avoidance and Path Planning Methods for Autonomous Navigation of Mobile Robot** | Katona et al. | 2024 | *Sensors* (MDPI) | 综述移动机器人自主导航的避障与路径规划方法。

15. **The Emergence of Deep Reinforcement Learning for Path Planning** | Nguyen, Nahavandi et al. | 2025 | arXiv:2507.15469 | 从传统方法到DRL的路径规划全面概述，覆盖UAV、自动驾驶、机器人。

16. **ROS-Based Navigation and Obstacle Avoidance: A Study of Architectures, Methods, and Trends** | 多位作者 | 2025 | *Sensors* (MDPI) | ROS导航栈架构综述，DWA/TEB规划器对比，深度学习集成。

---

## SLAM (同步定位与建图)

### 经典基础方法 (1987-2007)

1. **Estimating Uncertain Spatial Relationships in Robotics** | R. Smith, M. Self, P. Cheeseman | 1987 | *IEEE ICRA* | ~3,000+ | SLAM 问题的奠基性论文，首次用 EKF 框架建模机器人定位与建图。

2. **A Solution to the Simultaneous Localisation and Map Building (SLAM) Problem** | M.W.M.G. Dissanayake, P. Newman, S. Clark, H.F. Durrant-Whyte, M. Csorba | 2001 | *IEEE Trans. Robotics and Automation* | ~4,500+ | 证明了 EKF-SLAM 的收敛性，表明路标估计会变得完全相关。

3. **Simultaneous Localisation and Mapping (SLAM): Part I & II** | H. Durrant-Whyte, T. Bailey | 2006 | *IEEE Robotics & Automation Magazine* | ~5,000+ | SLAM 领域最经典的教程，系统综述了 EKF-SLAM 及核心求解方法。

4. **FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem** | M. Montemerlo, S. Thrun, D. Koller, B. Wegbreit | 2002 | *AAAI* | ~3,500+ | 开创性论文，利用 Rao-Blackwellized 粒子滤波将 SLAM 后验分解为机器人路径 + 独立路标估计。

5. **FastSLAM 2.0** | M. Montemerlo, S. Thrun | 2003 | *ICRA* | ~1,200+ | 改进版 FastSLAM，引入已知数据关联下的更优提议分布，解决 FastSLAM 1.0 的粒子退化问题。

6. **Improved Techniques for Grid Mapping with Rao-Blackwellized Particle Filters** | G. Grisetti, C. Stachniss, W. Burgard | 2007 | *IEEE TRO* | ~4,000+ | 著名的 **GMapping** 算法奠基论文，引入自适应提议分布和选择性重采样。

### 直接法视觉 SLAM

7. **DTAM: Dense Tracking and Mapping in Real-Time** | R.A. Newcombe, S.J. Lovegrove, A.J. Davison | 2011 | *ICCV* | ~2,600+ | 首个实时全稠密单目 SLAM 系统，利用 GPU 实现逐像素对齐，无特征提取。

8. **LSD-SLAM: Large-Scale Direct Monocular SLAM** | J. Engel, T. Schops, D. Cremers | 2014 | *ECCV* (Oral) | ~2,500+ | 半稠密直接法单目 SLAM，CPU 实时运行，sim(3) 显式处理尺度漂移，获 ECCV 2024 Koenderink 时间考验奖。

9. **Large-Scale Direct SLAM with Stereo Cameras** | J. Engel, J. Stuckler, D. Cremers | 2015 | *IROS* | ~520+ | LSD-SLAM 的双目扩展，融合静态立体与多视图立体消除尺度漂移。

10. **Direct Sparse Odometry** | J. Engel, V. Koltun, D. Cremers | 2018 | *IEEE TPAMI* | ~2,000+ | 稀疏直接法 VO，全光度标定，联合优化几何+运动参数，超越当时所有直接法和间接法。

11. **Stereo DSO: Large-Scale Direct Sparse Visual Odometry with Stereo Cameras** | R. Wang, M. Schwoerer, D. Cremers | 2017 | *ICCV* | ~500+ | DSO 的双目扩展，通过耦合因子集成静态立体约束，KITTI 上超越立体 LSD-SLAM 和特征法。

12. **LDSO: Direct Sparse Odometry with Loop Closure** | X. Gao (高翔), R. Wang, N. Demmel, D. Cremers | 2018 | *IROS* | ~400+ | 将 DSO 扩展为完整单目 SLAM，加入 BOW 回环检测和 Sim(3) 位姿图优化。

### 特征法视觉 SLAM (ORB-SLAM 系列)

13. **ORB-SLAM: A Versatile and Accurate Monocular SLAM System** | R. Mur-Artal, J.M.M. Montiel, J.D. Tardos | 2015 | *IEEE TRO* | ~6,000+ | ORB 特征驱动的现代 SLAM 标杆，引入三线程架构(跟踪/局部建图/回环)，全景 BA。

14. **ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras** | R. Mur-Artal, J.D. Tardos | 2017 | *IEEE TRO* | ~7,000+ | 支持单目/双目/RGB-D 的开源 SLAM 系统，引入局部 BA 和重定位，SLAM 领域引用最高的论文之一。

15. **ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM** | C. Campos, R. Elvira, J.J. Gomez, J.M.M. Montiel, J.D. Tardos | 2021 | *IEEE TRO* | ~950+ | ORB-SLAM 系列巅峰之作。首个统一纯视觉/视觉惯性/多地图 SLAM 系统。紧耦合 VI-SLAM 基于 MAP 估计，三步快速初始化(2秒达5%尺度误差)。Atlas 多地图系统支持跟踪丢失后自动创建新地图、重访时无缝合并。精度比 VINS-Mono 高 2 倍以上。支持针孔/鱼眼相机。

### 视觉惯性 SLAM (VIO / VI-SLAM)

16. **VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator** | T. Qin, P. Li, S. Shen (沈劭劼, HKUST) | 2018 | *IEEE TRO* | ~3,000+ | 鲁棒紧耦合单目视觉惯性里程计，包含鲁棒初始化、在线外参标定、回环检测、4-DOF 全局位姿图优化。无人机自主飞行的标杆系统。

17. **VINS-Fusion** | T. Qin, S. Shen (HKUST) | 2019 | GitHub 开源 | ~1,000+ | VINS-Mono 的多传感器扩展：支持单目+IMU / 双目+IMU / 纯双目 / GPS 融合。

18. **GVINS: Tightly-Coupled GNSS-Visual-Inertial Fusion for Smooth and Consistent State Estimation** | S. Cao, X. Lu, S. Shen | 2022 | *IEEE TRO* | ~300+ | 紧耦合 GNSS-视觉-惯性融合系统，在 GNSS 可用时消除 VIO 累积漂移。

19. **OpenVINS** | P. Geneva, K. Eckenhoff, W. Lee, Y. Yang, G. Huang | 2020 | *IEEE TRO* | ~500+ | 开放研究平台，覆盖多种 VINS 算法实现(MSCKF, 滑动窗口等)，用于视觉惯性估计的教学与研究。

### LiDAR SLAM

20. **LOAM: Lidar Odometry and Mapping in Real-time** | J. Zhang, S. Singh | 2014 | *RSS* | ~3,500+ | LiDAR SLAM 开创性框架：高频里程计(10Hz) + 低频建图(1Hz)双线程架构，边缘/平面特征点匹配。

21. **LeGO-LOAM: Lightweight and Ground-Optimized Lidar Odometry and Mapping on Variable Terrain** | T. Shan, B. Englot | 2018 | *IROS* | ~2,000+ | LOAM 改进版：地面点分离、两步位姿优化、轻量级回环检测，专为地面车辆设计。

22. **LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping** | T. Shan, B. Englot, D. Meyers et al. | 2020 | *IROS* | ~2,000+ | 因子图优化的紧耦合激光-惯性里程计，GTSAM 统一优化 LiDAR/IMU/GPS/回环，滑动窗口。

23. **LVI-SAM: Tightly-coupled Lidar-Visual-Inertial Odometry via Smoothing and Mapping** | T. Shan, B. Englot, C. Ratti, D. Rus | 2021 | *ICRA* | ~800+ | 激光-视觉-惯性三传感器紧耦合，两子系统互初始化冗余，退化环境鲁棒性最强。

24. **FAST-LIO: A Fast, Robust LiDAR-inertial Odometry Package by Tightly-Coupled Iterated Kalman Filter** | W. Xu, F. Zhang | 2021 | *IEEE RA-L* | ~1,200+ | 基于误差状态迭代卡尔曼滤波(ES-IEKF)的紧耦合 LIO，无需图优化，计算效率极高。

25. **FAST-LIO2: Fast Direct LiDAR-inertial Odometry** | W. Xu, Y. Cai, D. He, J. Lin, F. Zhang (HKU) | 2022 | *IEEE TRO* | ~800+ | 抛弃特征提取，直接配准原始点云，ikd-Tree 动态数据结构保证效率，支持 1000 deg/s 高速旋转。

26. **Faster-LIO: Lightweight Tightly Coupled Lidar-inertial Odometry** | C. Bai, T. Xiao, Y. Chen et al. | 2023 | *IEEE TRO* | 将 ikd-Tree 替换为 iVox(增量体素哈希)，固态激光雷达可达 1-2kHz。

### 语义SLAM与动态环境SLAM

27. **DynaSLAM: Tracking, Mapping and Inpainting in Dynamic Scenes** | B. Bescos, J.M. Facil, J. Civera, J. Neira | 2018 | *IEEE RA-L* | ~1,500+ | 将 Mask R-CNN 集成到 ORB-SLAM2，利用实例分割检测动态物体并剔除，同时对被遮挡背景进行图像修补。

28. **DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments** | C. Yu, Z. Liu, X. Liu et al. | 2018 | *IROS* | ~1,200+ | 结合 SegNet 语义分割与光流检测动态物体，在 TUM RGB-D 数据集上显著提升动态场景定位精度。

### NeRF / 3DGS SLAM (前沿方向)

29. **LSG-SLAM: Large-Scale Gaussian Splatting SLAM** | 多位作者 | 2025 | *ICRA 2025* | 首个基于 3DGS 的大规模室外双目视觉 SLAM，连续 Gaussian Splatting 子图处理无限场景，含回环检测。

30. **DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior** | 多位作者 | 2025 | *IEEE TVCG* | 首个结合 NeRF 与 3DGS 优势的 SLAM 系统，NeRF 先验初始化基元以稠密填充地图。

31. **DINO-SLAM** | Gong, Li, Tosi et al. | 2025 | arXiv:2507.19474 | 利用 DINO 特征增强 NeRF 和 3DGS SLAM 表达，Scene Structure Encoder 捕捉层次化场景元素。

---

## 路径规划 (Path Planning)

### 经典图搜索方法

1. **A Formal Basis for the Heuristic Determination of Minimum Cost Paths** | P.E. Hart, N.J. Nilsson, B. Raphael | 1968 | *IEEE Trans. Systems Science and Cybernetics* | ~20,000+ | **A\* 算法**的提出论文，启发式搜索的里程碑，为自动驾驶全局路径规划奠定基础。

2. **A Note on Two Problems in Connexion with Graphs** | E.W. Dijkstra | 1959 | *Numerische Mathematik* | ~50,000+ | **Dijkstra 算法**的原始论文，最短路径搜索的基础。

3. **Optimal and Efficient Path Planning for Partially-Known Environments** | A. Stentz | 1994 | *ICRA* | ~3,000+ | **D\* 算法**论文，专为部分已知/动态环境设计的高效重规划算法，火星漫游车曾使用。

4. **The Focused D* Algorithm for Real-Time Replanning** | A. Stentz | 1995 | *IJCAI* | ~2,000+ | D\* 的改进版，引入启发式聚焦搜索，进一步提升重规划效率。

### 采样法规划

5. **Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces** | L.E. Kavraki, P. Svestka, J.C. Latombe, M.H. Overmars | 1996 | *IEEE TRO* | ~8,000+ | **PRM** 算法的提出论文，通过随机采样构造路线图，解决高维空间路径规划问题。

6. **Rapidly-Exploring Random Trees: A New Tool for Path Planning** | S.M. LaValle | 1998 | Technical Report | ~12,000+ | **RRT** 算法奠基论文，基于随机采样的快速探索随机树，处理高维连续空间的路径规划。

7. **Sampling-based Algorithms for Optimal Motion Planning** | S. Karaman, E. Frazzoli | 2011 | *IJRR* | ~5,500+ | **RRT\*** 与 **PRM\*** 论文，证明了渐进最优性的理论基础，引入重连接（rewiring）机制。

8. **RRT-Connect: An Efficient Approach to Single-Query Path Planning** | J.J. Kuffner, S.M. LaValle | 2000 | *ICRA* | ~4,000+ | 双向 RRT 扩展的并行算法，显著提升采样效率，路径长度更优。

### 局部规划与避障

9. **The Dynamic Window Approach to Collision Avoidance** | D. Fox, W. Burgard, S. Thrun | 1997 | *IEEE Robotics & Automation Magazine* | ~5,000+ | **DWA** 经典论文，基于速度空间的动态窗口避障方法，在 ROS navigation stack 中广泛应用。

10. **Time Elastic Band (TEB) Local Planner** | C. Roesmann, W. Feiten, T. Woesch et al. | 2012 | *ROBOTIK* | ~1,200+ | 基于图优化的局部规划器，考虑动力学约束和时间最优，ROS 导航的主要局部规划器之一。

### 学习驱动规划

11. **Deep Reinforcement Learning with Dynamic Window Approach Based Collision Avoidance Path Planning for Maritime Autonomous Surface Ships** | Dong et al. | 2023 | *Ocean Engineering* | 将 DWA 的评估函数引入 PPO 奖励设计，解决稀疏奖励问题。

12. **Recent Progress, Challenges and Future Prospects of Applied Deep Reinforcement Learning in Path Planning** | 多位作者 | 2024 | *Neurocomputing* (Elsevier) | 综述 DRL 路径规划 8 类训练效率提升方法。

---

## 传感器融合 (Sensor Fusion)

### 视觉-惯性融合

1. **MSCKF: A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation** | A.I. Mourikis, S.I. Roumeliotis | 2007 | *ICRA* | ~3,000+ | 多状态约束卡尔曼滤波，视觉-惯性融合的重要基础方法，维护滑动窗口内的相机位姿状态。

2. **OKVIS: Keyframe-Based Visual-Inertial SLAM Using Nonlinear Optimization** | S. Leutenegger, S. Lynen, M. Bosse et al. | 2015 | *IJRR* | ~1,800+ | 基于关键帧的非线性优化紧耦合 VIO，将视觉和惯性测量联合优化。

3. **VINS-Mono** (见 SLAM 部分 #16) | T. Qin, P. Li, S. Shen | 2018 | *IEEE TRO* | ~3,000+ | 紧耦合非线性优化 VIO，鲁棒初始化，在线外参标定，回环检测。

4. **GVINS: Tightly-Coupled GNSS-Visual-Inertial Fusion** (见 SLAM 部分 #18) | S. Cao et al. | 2022 | *IEEE TRO* | 将 GNSS 原始测量紧耦合到视觉-惯性优化框架中。

### 多传感器融合

5. **Multi-Sensor Fusion in Automated Driving: A Survey** | Wang et al. | 2020 | *IEEE Access* | ~800+ | 自动驾驶多传感器融合综述，覆盖数据级、特征级、决策级融合。

6. **LVI-SAM** (见 SLAM 部分 #23) | T. Shan et al. | 2021 | *ICRA* | ~800+ | 激光-视觉-惯性三传感器紧耦合，退化环境鲁棒性最强。

7. **Advancements in Perception System with Multi-Sensor Fusion for Embodied Agents** | H. Du, L. Ren et al. | 2024 | *Information Fusion* (Elsevier) | 多传感器融合感知综述，覆盖SLAM、3D目标检测、语义/实例/全景分割。

### 其他融合范式

8. **P3-VINS: Tightly-Coupled PPP/INS/Visual SLAM** | Li et al. | 2022 | *IEEE RA-L* | 精密单点定位+惯性+视觉 SLAM 紧耦合，室外大场景建图。

9. **R3LIVE: A Robust, Real-time, RGB-colored, LiDAR-Inertial-Visual tightly-coupled Estimation and Mapping System** | J. Lin, F. Zhang | 2022 | *ICRA* | 实时 RGB 着色建图的激光-惯性-视觉融合系统。

10. **检测优先的激光-视觉-惯性紧耦合 SLAM** (Detection-first tightly-coupled LiDAR-Visual-Inertial SLAM) | 多位作者 | 2024 | *Measurement* | 将目标检测融入SLAM前端，动态场景 RMSE 降低 44.56%。

---

## 学习驱动导航 (Learning-based Navigation)

### 端到端导航

1. **End-to-End Learning for Self-Driving Cars** | M. Bojarski, D. Del Testa, D. Dworakowski et al. (NVIDIA) | 2016 | arXiv:1604.07316 | ~3,500+ | NVIDIA PilotNet: 端到端 CNN 将前向摄像头图像直接映射为方向盘转角，引领端到端自动驾驶。

2. **End-to-end Autonomous Driving using Deep Learning: A Systematic Review** | A. Singh (CMU) | 2023 | arXiv:2311.18636 | 系统综述端到端全可微 RL 与深度学习方法，含模仿学习、RL、师生范式等。

3. **A Comprehensive Review on Deep Learning-Based Motion Planning and End-To-End Learning for Self-Driving Vehicle** | Ganesan et al. | 2024 | *IEEE Access* | 综述行为规划、轨迹规划与端到端学习，含 IL、RL 技术及数据集。

### 强化学习导航

4. **Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning** | Y. Zhu, R. Mottaghi, E. Kolve et al. | 2017 | *ICRA* | ~1,500+ | AI2-THOR 环境中的目标驱动视觉导航，A3C 算法，开创视觉-语言导航范式。

5. **Learning to Navigate in Complex Environments** | P. Mirowski, R. Pascanu, F. Viola et al. | 2017 | *ICLR* | ~1,200+ | DeepMind 导航研究，结合辅助任务(深度预测+回环检测)的 A3C 导航策略。

6. **深度强化学习求解移动机器人端到端导航问题的研究综述** | 何力, 姚嘉诚, 廖育新 等 | 2024 | 《计算机工程与应用》 | ~中文综述 | DRL 端到端导航综述，将挑战分为感知能力差、学习效率低、泛化能力弱三类。涵盖 VLN、多智能体协同导航、可解释导航等前沿方向。

7. **Probabilistic Mapping and Navigation: A Survey of Bayesian Meta-Learning for Autonomous Robots** | 多位作者 | 2025 | *J. Intelligent & Robotic Systems* (Springer) | 贝叶斯元学习在概率建图与导航中的应用。

### 模仿学习

8. **ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst** | M. Bansal, A. Krizhevsky, A. Ogale | 2018 | arXiv:1812.03079 | ~700+ | Waymo 的模仿学习驾驶框架，通过合成最差场景增强泛化性。

9. **Conditional Imitation Learning for End-to-End Driving** | F. Codevilla, M. Mueller, A. Lopez, V. Koltun, A. Dosovitskiy | 2018 | *ICRA* | ~800+ | CIDNN: 条件模仿学习，根据导航指令在不同驾驶行为间切换。

---

## 重要开源项目与数据集

### 核心数据集

| 数据集 | 传感器 | 场景 | 年份 | 用途 |
|---|---|---|---|---|
| **KITTI** | 双目 RGB + 64线LiDAR + GPS/IMU | 城市道路/高速 | 2012 (CVPR) | VO/3D检测/跟踪/立体 |
| **KITTI-360** | 全向相机 + LiDAR + GPS/IMU | 城郊大范围 | 2022 | 全景场景理解 |
| **EuRoC MAV** | 双目 RGB + IMU (Vicon真值) | 工业室内 | 2016 (IJRR) | VI-SLAM/VIO 标准评测 |
| **TUM RGB-D** | RGB-D (Kinect) | 室内办公 | 2012 | RGB-D SLAM |
| **TUM VI** | 鱼眼 RGB + IMU | 室内手持 | 2018 (IROS) | VIO/VI-SLAM |
| **TUM monoVO** | 鱼眼单目 | 室内/室外 | 2016 | 单目VO |
| **nuScenes** | 6相机 + 5毫米波 + 1 LiDAR + GPS/IMU | 城市道路(波士顿/新加坡) | 2019 (CVPR) | 3D检测/跟踪/预测 |
| **Waymo Open Dataset** | 5 LiDAR + 5 相机 + 雷达 | 城市道路(美国多城) | 2020 (CVPR) | 规模最大的自动驾驶数据集 |
| **Argoverse 2** | 7相机 + 2 LiDAR + 6 毫米波 | 城市道路 | 2023 | 运动预测/检测/跟踪 |
| **Replica** | RGB-D 室内场景重建 | 室内合成 | 2019 | 语义SLAM/NeRF建图 |
| **ScanNet** | RGB-D | 室内真实 | 2017 | 3D重建/语义SLAM |

### 核心开源项目

| 项目 | 类别 | 语言 | GitHub Stars | 说明 |
|---|---|---|---|---|
| **ORB-SLAM3** | 视觉/视觉惯性 SLAM | C++ | ~7k | 最完整的功能SLAM，单目/双目/RGB-D/IMU |
| **VINS-Mono** | 视觉惯性里程计 | C++ | ~5k | 无人机自主飞行标杆 |
| **VINS-Fusion** | 多传感器融合 | C++ | ~4k | VINS-Mono 多传感器扩展 |
| **FAST-LIO2** | 激光惯性里程计 | C++ | ~3k | 最快LIO，直接点云配准 |
| **LIO-SAM** | 激光惯性 SLAM | C++ | ~3.5k | 因子图优化LIO |
| **LVI-SAM** | 激光-视觉-惯性 SLAM | C++ | ~2.5k | 三传感器紧耦合 |
| **DynaSLAM** | 动态环境 SLAM | C++ | ~1.5k | ORB-SLAM2 + Mask R-CNN |
| **DSO** | 直接稀疏 VO | C++ | ~2.5k | 直接法VO标杆 |
| **evo** | SLAM评测工具 | Python | ~4k | 轨迹评估/APE/RPE |
| **Cartographer** | 2D/3D 激光 SLAM | C++ | ~7.5k | Google 出品，实时建图 |
| **Apollo** | 全栈自动驾驶 | C++ | ~25k | 百度自动驾驶开放平台 |
| **Autoware** | 全栈自动驾驶 | C++ | ~10k | ROS2 自动驾驶开源框架 |
| **CARLA** | 自动驾驶仿真 | C++/Python | ~12k | 基于UE4/5的开源仿真器 |
| **ROS Navigation Stack** | 通用导航 | C++ | ~2.5k | ROS 标准导航框架(DWA/TEB) |

---

## 关键期刊/会议

### 顶级期刊 (Journals)

| 期刊 | 简称 | 影响因子 | 说明 |
|---|---|---|---|
| **IEEE Transactions on Robotics** | IEEE TRO | ~7.0 | 机器人领域顶刊，SLAM 核心论文首选 |
| **International Journal of Robotics Research** | IJRR | ~5.5 | 机器人领域最权威期刊之一 |
| **IEEE Robotics and Automation Letters** | IEEE RA-L | ~5.0 | 短周期快发(6页)，含 ICRA/IROS 附带选项 |
| **IEEE Transactions on Intelligent Vehicles** | IEEE TIV | ~5.0 | 智能车辆专刊 |
| **IEEE Transactions on Intelligent Transportation Systems** | IEEE TITS | ~8.5 | 智能交通系统 |
| **IEEE Transactions on Pattern Analysis and Machine Intelligence** | IEEE TPAMI | ~24.0 | CV/AI 顶刊，SLAM 视觉部分发布地 |
| **International Journal of Computer Vision** | IJCV | ~12.0 | CV 顶刊 |
| **Field Robotics** | - | 新刊 | 2021 创刊，实地机器人系统 |
| **Science Robotics** | - | ~25.0 | 机器人顶级综合期刊 |

### 顶级会议 (Conferences)

| 会议 | 领域 | 说明 |
|---|---|---|
| **ICRA** (IEEE International Conference on Robotics and Automation) | 机器人 | 机器人领域最大/最重要会议 |
| **IROS** (IEEE/RSJ International Conference on Intelligent Robots and Systems) | 机器人 | 第二大规模机器人会议 |
| **RSS** (Robotics: Science and Systems) | 机器人 | 高水平精品会议 |
| **CVPR** (Computer Vision and Pattern Recognition) | CV | AI/CV 旗舰会议，SLAM CNN/ViT 部分 |
| **ICCV** (International Conference on Computer Vision) | CV | CV 顶会，直接法SLAM |
| **ECCV** (European Conference on Computer Vision) | CV | CV 顶会 |
| **NeurIPS** | AI | DRL 导航/规划 |
| **ICLR** | AI | 学习驱动导航 |
| **CoRL** (Conference on Robot Learning) | 机器人+ML | 机器人学习交叉领域 |
| **ITSC** (IEEE Intelligent Transportation Systems Conference) | 智能交通 | 自动驾驶导航/规划/控制 |

---

## 研究趋势总结 (2025-2026)

1. **NeRF / 3DGS SLAM**: 隐式和显式神经辐射场正在重塑建图方式，3DGS 路线兼顾逼真渲染和高效推理。
2. **语义SLAM**: 融入目标检测/分割/LLM 的语义级场景理解，是动态环境鲁棒SLAM的关键。
3. **紧耦合多传感器融合**: 激光-视觉-惯性-IMU-GPS 五重融合成为自动驾驶主流。
4. **Foundation Model + 导航**: 大语言模型(LLM)与视觉语言模型(VLM)用于自然语言导航指令理解。
5. **Sim-to-Real**: CARLA, Isaac Sim 等仿真器推动的策略迁移到真实机器人。
6. **滤波路线 vs. 图优化路线**: FAST-LIO 系列(滤波)追求极致实时性，LIO-SAM 系列(图优化)追求全局一致性，两者并存。
7. **3D 占用网络(OCC)**: 替代传统3D框检测的 BEV 感知范式，nuScenes/Occ3D 推动。
8. **可解释端到端导航**: 从黑盒走向可解释，注意力机制和因果推理融入导航决策。
