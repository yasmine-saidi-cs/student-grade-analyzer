# 📊 Student Grade Analyzer (Advanced Edition)

A robust Python-based application equipped with an interactive Graphical User Interface (GUI) that empowers students to analyze academic grades, track progress, visualize performance, and store records efficiently.

## 🚀 Project Overview
Student Grade Analyzer is an intermediate-level Python application designed to make academic performance tracking seamless and data-driven. Moving beyond basic scripting, this version integrates dynamic widgets, relational data visualization, persistent local storage, and automated verification systems.

This project represents a major milestone in my self-taught software engineering journey, showcasing clean code architecture and practical data implementation.

## ✨ Advanced Features
- **Dynamic Graphical User Interface (GUI):** Built utilizing `ipywidgets` for a smooth, interactive input flow directly inside Jupyter environments.
- **Weighted Average Calculations:** Accounts for distinct subject coefficients using precision mathematics.
- **Persistent Local Database (CSV):** Automatically stores structures of student records over time for historic analysis.
- **Advanced Statistical Analytics:** Computes the Mean and Median of grades, while dynamically identifying data extremes (Highest/Lowest benchmarks).
- **Automated Algorithmic Sorting:** Employs custom lambda sorting algorithms to rank subjects from top performance to lowest.
- **Interactive Visualizations:** Renders crisp, color-coded bar charts for subject grades and line charts for historical tracking via `Matplotlib`.
- **Smart Insights & Rule-Based Advice:** Uses predictive conditional structures to identify the highest coefficient priorities and provide personalized study suggestions.
- **Automated Unit Testing Framework:** Includes built-in self-testing protocols (PASS/FAIL logs) ensuring programmatic reliability before final outputs.

## 🛠️ Technologies & Libraries Used
- **Language:** Python 3
- **Data Visualizations:** Matplotlib
- **Interactive GUI Framework:** IPyWidgets / IPython Display
- **Statistical Engineering:** Python `statistics`, `math`, `csv`, and `os` modules.
- **Version Control:** Git & GitHub

## 🧠 Software Architecture & Workflow
1. **Dynamic Initialization:** The user inputs their profile name, subject count, and optional historic average benchmarks.
2. **Dynamic Field Generation:** The GUI renders structural sub-containers matching the requested subject volume.
3. **Data Verification Pipeline:** Inputs are instantly evaluated through defensive logic checks (ensuring non-empty fields, positive coefficients, and grades strictly constrained between `0` and `20`).
4. **Relational Analysis Execution:** The core calculations compute statistics, map subject ranking positions, and process historical progress differences.
5. **Data Visualization & Export:** Results are appended seamlessly to a local `.csv` file, followed by immediate mathematical chart renderings.
6. **Built-in System Unit Test Verification:** Automated verification confirms system core metrics return accurate boolean matches.

## 🎯 Architectural Concepts Learned
Through engineering this comprehensive application, I mastered:
- Advanced function modularity and data decoupling (Separation of Concerns).
- Array manipulations, multi-list zipping, and data indexing.
- Custom lambda logic handling within standard python sorting utilities.
- Object state management and dynamic layouts using interface boxes (`VBox` containers).
- Data persistence structures using file Input/Output protocols (`File I/O`).
- Implementation of automated software unit testing principles.

## 🔮 Future Roadmaps
- Transitioning the notebook interface into a fully standalone desktop app using `Tkinter` or `PyQt`.
- Integrating an advanced web application wrapper utilizing `Flask` or `Streamlit`.
- Implementing predictive Machine Learning models to forecast final national exam scores based on early continuous assessment inputs.

## 👩‍‍💻 Author
**Yasmine Saidi**  
*High school student specializing in Experimental Sciences (Sciences Expérimentales), deeply passionate about Computer Science, Artificial Intelligence, and Data Engineering.*  

*This project stands as a proud cornerstone of my computer science application portfolio.*  

⭐ *More interdisciplinary tech projects bridging computer science and scientific concepts will be continuously shipped.*
