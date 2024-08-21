# Systematic Program Design

## What is this repo?

The repository **promoha90/UBC-SPD** showcases my ongoing work in the **Systematic Program Design** series of courses from the University of British Columbia (UBC) on edX. As I continue to progress through the course, I'll be uploading exercises and updates to reflect my learning journey.

## The courses are:

- [SPD1x](https://courses.edx.org/courses/course-v1:UBCx+SPD1x+2T2015/course/)
- [SPD2x](https://courses.edx.org/courses/course-v1:UBCx+SPD2x+2T2015/course/)
- [SPD3x](https://courses.edx.org/courses/course-v1:UBCx+SPD3x+3T2015/course/)

These courses were offered in 2015 and are now archived. While course materials remain accessible, support from course staff and official certificates are no longer available.

## Contents of the Repository

In this repository, you will find:

- Homework problems solutions (staff solution is included too)
- **ALL** extra problems solutions (staff solution is included too)
- Quizzes (multiple-choice quizzes in PDF format)
- Exams   (design quizzes with code and staff solution)
- Handwritten notes

### The courses include:

- 18 weeks
- 101 lectures
- 44 homework exercises
- 194 extra exercises
- 144 quizzes (ranging from short, one-lecture-worth quizzes to a full-week quiz)
- 6 exams (comprehensive exercises where the whole unit's knowledge is implemented)  
- 1 final project (a comprehensive project utilizing several weeks of course knowledge)  
- ***104-130 hours for completion (without extra exercises)***

**COMPLETION OF ALL COURSE MATERIALS:**  

I programmed this [script](count.py) with python to add together all the exercises estimated time in [Problem-Bank.pdf]("Problem-Bank.pdf"), we have 194 extra exercises and the script returned 3586 minutes.

- **Math:**
  ```
  3586 / 194 = 18.48 minutes per exercise
  194 * 0.30 = 58.20 hours for all exercises
  104 + 58.2 = 162.2 hours for all exercises + minimum staff's estimated time
  130 + 58.2 = 188.2 hours for all exercises + maximum staff's estimated time
  ```

- **TOTAL:** **162.2-188.2 hours**


<br>

The functional programming language used throughout these courses is Racket (a Lisp dialect), and DrRacket (IDE) is required for code preview. Some details might be missing from text-only exports due to DrRacket's image capabilities, but code is fully readable.

Feel free to browse the material if you're interested in exploring the courses content or studying functional programming with Racket.


### Folder Structure:  
- **_1\. (problem name)-starter.rkt_** :: My solution  
- **_2\. (problem name).txt_** :: My solution in text  
- **_3\. (problem name)-solution.rkt_** :: Official (from course staff) solution  
- **_4\. (problem name)-starter.bak_** :: DrRacket temporary file (ignore)  

<br><br>

# What will I learn in this course series?

## Part 1: Systematic Program Design - The Fundamentals

### Learning Objectives
- **Function Design**: Master the systematic approach to designing functions, including writing precise contracts, creating examples, and utilizing design templates.
- **Domain Analysis**: Understand how to analyze and represent different data domains, which is critical for designing functions that handle data effectively.
- **Design Recipes**: Learn the step-by-step process known as the "Design Recipe," which guides the development of programs from problem statement to solution.
- **Basic Data Types**: Work with basic data types (e.g., numbers, strings, booleans) and structures (e.g., lists) to create programs that solve simple problems.

### Key Concepts
- *Contracts*: Define the expected input and output for functions.
- *Examples*: Illustrate how functions should behave with specific inputs.
- *Templates*: Develop reusable patterns to guide function creation.
- *Testing*: Implement tests to ensure that functions behave as expected.

## Part 2: Systematic Program Design - Designing Functions

### Learning Objectives
- **Complex Data Structures**: Extend your understanding to more complex data types, including compound data (e.g., structures) and mixed data types.
- **Data-Driven Design**: Learn how the shape and structure of data influence the design of your functions.
- **Recursive Data and Functions**: Develop the ability to design functions that operate on recursive data structures, such as lists and trees.
- **Accumulative Functions**: Understand how to design functions that accumulate results as they process data.

### Key Concepts
- *Compound Data*: Design and use custom data structures.
- *Recursion*: Implement recursive functions that handle self-referential data.
- *Accumulation*: Create functions that accumulate results (e.g., summing elements of a list).

## Part 3: Systematic Program Design - Abstraction and Reuse

### Learning Objectives
- **Abstraction Principles**: Learn to abstract common patterns in your programs, which leads to code that is easier to maintain and reuse.
- **Higher-Order Functions**: Master the use of higher-order functions that take other functions as inputs or return functions as outputs.
- **Parameterization**: Develop functions that are more general by parameterizing over data and behavior.
- **Modularity**: Understand the importance of modular design in creating scalable and maintainable software systems.

### Key Concepts
- *Abstraction*: Identify and encapsulate patterns to reduce code duplication.
- *Higher-Order Functions*: Use functions like `map`, `filter`, and `fold` to operate on data structures in a generic way.
- *Reuse*: Promote code reuse by designing more abstract and flexible functions.
- *Modularity*: Structure your code into modules to enhance maintainability.

<br><br>

# Syllabus:

## Part 1

<table>
  <tr>
    <th>Week</th>
    <th width=25%>Module Name</th>
    <th>Lectures</th>  
    <th>Time to complete</th>  
    <th>Homework Problems</th>
    <th>Extra Problems</th> 
    <th width=14%>Quiz</th>
  </tr>
  <tr>
  <th colspan="1">
  </th> 
  <th colspan="6">Overall learning goal</th> 
  </tr>

  <tr>
    <td rowspan="2">1</td>
    <td><strong>Beginning Student Language</strong></td>
    <td>8</td>
    <td>5-8 Hours</td>
    <td>4</td>
    <td>16</td>
    <td><i>none</i></td>
  </tr>

  <tr>
  <td colspan="6">Learn to program with the core of the programming language used throughout the course.</td>
  </tr>

  <tr>
    <td rowspan="2">2</td>
    <td><strong>How to Design Functions (HtDF) Recipe</strong></td>
    <td>6</td>
    <td>4-7 Hours</td>
    <td>3</td>
    <td>13</td>
    <td>Self-Assessed Design Quiz</td>
  </tr>
  
  <tr>
  <td colspan="6">Learn to use the HtDF recipe to design functions that consume simple primitive data.</td>
    
  
  <tr>
    <td rowspan="2">3</td>
    <td><strong>How to Design Data (HtDD) Recipe</strong></td>
    <td>12</td>
    <td>5-8 Hours</td>
    <td>3</td>
    <td>17</td>
    <td>Self-Assessed Design Quiz</td>
  </tr>
  
  <tr>	
  <td colspan="6">Learn to use the HtDD recipe to design data definitions for atomic data.</td>
    
 
  <tr>
    <td rowspan="3">4</td>
    <td><strong>How to Design Worlds (HtDW) Recipe</strong></td>
    <td>7</td>
    <td>3-5 Hours</td>
    <td>1</td>
    <td>4</td>
    <td><i>none</i></td>
  </tr>
  
  <tr>
    <td><strong>Compound Data</strong></td>
    <td>3</td>
    <td>4-6 Hours</td>
    <td>3</td>
    <td>11</td>
    <td>Peer-Assessed Final Project</td>
  </tr>
  
  <tr>		
  <td colspan="6">Learn to use the HtDW recipe to design interactive programs with atomic and then compound world state.</td>
  </tr>
</table>

<br>

## Part 2

<table>
<tbody>
<tr>
  <th rowspan="2">Week</th>
  <th width="25%">Module Name</th>
  <th>Lectures</th>
  <th>Time to complete</th>
  <th>Homework Problems</th>
  <th>Extra Problems</th>
  <th>Quiz</th>
</tr>
<tr>
  <th colspan="6">Overall learning goal</th>
</tr>

<tr>
  <td rowspan="4">5</td>
  <td><strong>Self-Reference</strong></td>
  <td>7</td>
  <td>5-7 Hours</td>
  <td>4</td>
  <td>6</td>
  <td rowspan ="4"><i>Multiple Choice Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn how to use well-formed self-referential data definitions to represent arbitrary sized data.</td>
</tr>
<tr>
  <td><strong>Reference</strong></td>
  <td>3</td>
  <td>4-6 Hours</td>
  <td>2</td>
  <td>6</td>
</tr>
<tr>
 <td colspan="5">Learn to predict and identify the correspondence between references in a data definition and helper function calls in functions that operate on the data.</td>
</tr>

<tr>
  <td rowspan="4">6</td>
  <td><strong>Naturals</strong></td>
  <td>2</td>
  <td>3-4 Hours</td>
  <td>2</td>
  <td>6</td>
  <td rowspan ="4"><i>Self-Assessed Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Design an alternate data definition for the natural numbers, and learn to write functions using this new data definition.</td>
</tr>
<tr>
  <td><strong>Helpers</strong></td>
  <td>6</td>
  <td>6-9 Hours</td>
  <td>1</td>
  <td>9</td>
</tr>
<tr>
  <td colspan="5">Learn a set of rules for designing functions with helper functions.</td>
</tr>

<tr>
  <td rowspan="4">7</td>
  <td><strong>Binary Search Trees</strong></td>
  <td>6</td>
  <td>5-6 Hours</td>
  <td>3</td>
  <td>12</td>
  <td rowspan ="4"><i>Multiple Choice Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Design a data definition for Binary Search Trees, and learn to write functions operating on BSTs.</td>
</tr>
<tr>
  <td><strong>Mutual Reference</strong></td>
  <td>5</td>
  <td>6-7 Hours</td>
  <td>1</td>
  <td>12</td>
</tr>
<tr>
  <td colspan="5">Learn to design with mutually referential data.</td>
</tr>

<tr>
  <td rowspan="4">8</td>
  <td><strong>Two One-Of Types</strong></td>
  <td>2</td>
  <td>3-5 Hours</td>
  <td>2</td>
  <td>6</td>
  <td rowspan ="4"><i>Self-Assessd Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn to use a cross-product of type templates table to design functions operating on two complex pieces of data.</td>
</tr>
<tr>
  <td><strong>Local</strong></td>
  <td>6</td>
  <td>8-10 Hours</td>
  <td>4</td>
  <td>10</td>
</tr>
<tr>
  <td colspan="5">Learn to use local expressions in your function designs.</td>
</tr>

</tbody>
</table>

<br>

## Part 3

<table>
<tbody>
<tr>
  <th rowspan="2">Week</th>
  <th width="25%">Module Name</th>
  <th>Lectures</th>
  <th>Time to complete</th>
  <th>Homework Problems</th>
  <th>Extra Problems</th>
  <th>Quiz</th>
</tr>
<tr>
  <th colspan="6">Overall learning goal</th>
</tr>
<tr>
  <td rowspan="2">9</td>
  <td><strong>Abstraction</strong></td>
  <td>7</td>
  <td>8-12 Hours</td>
  <td>3</td>
  <td>22</td>
  <td rowspan ="2"><i>Multiple Choice Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn how to design functions that are more general and versatile using abstraction.</td>
</tr>
<tr>
  <td rowspan="4">10</td>
  <td><strong>Generative Recursion</strong></td>
  <td>3</td>
  <td>5-6 Hours</td>
  <td>2</td>
  <td>10</td>
  <td rowspan ="4"><i>Multiple Choice Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn how to use generative recursion to create fractals.</td>
</tr>
<tr>
  <td><strong>Search</strong></td>
  <td>9</td>
  <td>8-9 Hours</td>
  <td>0</td>
  <td>8</td>
</tr>
<tr>
  <td colspan="5">Expand on generative recursion to solve search problems, such as Sudoku.</td>
</tr>
<tr>
  <td rowspan="2">11</td>
  <td><strong>Accumulators</strong></td>
  <td>5</td>
  <td>9-10 Hours</td>
  <td>3</td>
  <td>22</td>
  <td rowspan ="2"><i>Multiple Choice Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn how and when to use accumulators in several ways.</td>
</tr>
<tr>
  <td rowspan="3">12</td>
  <td><strong>Graphs</strong></td>
  <td>4</td>
  <td>7-8 Hours</td>
  <td>3</td>
  <td>12</td>
  <td rowspan ="2"><i>Multiple Choice Design Quiz</i></td>
</tr>
<tr>
  <td colspan="5">Learn to identify when information naturally forms a graph, and learn to write functions operating on such data.</td>
</tr>

</tbody>
</table>

<br><br>

# Installation and Usage
1. **Install DrRacket:**
   - Download from [Racket's official website](https://racket-lang.org/)
2. **Open and Explore Files:**
   - Use DrRacket to open and view `.rkt` files.
3. **Running Code:**
   - Follow the course materials to execute and test the code.

<br>

# Course Progress
As of [here I'll put the date when i'm finished], I have completed 100% of the content, including additional exercises, for the Systematic Program Design series on edX.  

<br>

# Contributing
Contributions are not accepted as this repository is intended solely to showcase my efforts in the course, which no longer offers certification.

<br>

# Acknowledgements
Special thanks to the University of British Columbia and the course instructors Gregor Kiczales and Erika Thompson for providing such valuable material.

<img src="images/ubc.png" alt="University of British Columbia Logo" width="250"/>

<br>

# Resources
- [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia)
- [What is Systematic Problem Design?](https://en.wikipedia.org/wiki/Systemic_design)
- [What is Racket?](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Racket Instalation](https://download.racket-lang.org/)
- [Racket Documentation](https://docs.racket-lang.org/)
