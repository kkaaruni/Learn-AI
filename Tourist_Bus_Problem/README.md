### Project Description
Problem: Assign tourist groups to buses to produce the optimum number of 70-seater tour buses.

We can easily find what the optimum is:
- Divide the total number of people by the number of seats on the bus

However, it is not as straight-forward to find where the optimum is, i.e. which groups go in which buses.


### How to Install and Run
1. Clone the repository:
    ```bash
    git clone https://github.com/kkaaruni/Learn-AI.git
    cd Learn-AI/Tourist_Bus_Problem
    ```
2. Install PuLP:
    ```bash
    pip install pulp
    ```
3. Run the code:
    ```bash
    python tourist_bus_problem.py
    ```