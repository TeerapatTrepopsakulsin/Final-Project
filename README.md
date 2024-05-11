# Road incident deaths

## Description
The GUI application was created using Tkinter and Python to allow users to visualise, analyse, and interact with global road incident deaths in 1990-2019 data to obtain useful knowledge or insights.
The application contains 3 pages, a Storytelling page, a DataExploration page, and a Dataset page.

The data on the Storytelling page will be displayed as descriptive statistics, graphs, and charts, with little interactivity. On the DataExploration page, the user can fully alter the view and interact with graphs to gain their interest information (age, type, year, etc.), which will be displayed differently depending on the filtered parameters after a graph is generated. Lastly, the Dataset page displays the dataset used for calculating and generating the graph for this project. (Road_incident_deaths.csv [Check out my data processing](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Data-Processing)).

## Application UI (MS Windows)
|Page| Application UI  |
|--------|--------------------|
|Storytelling|![Storytelling](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/data/Storytelling.png)|
|DataExploration|![DataExploration](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/DataExploration.png)|
|Dataset|![Dataset page](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/Dataset.png)|

## Interaction
**Storytelling**
   1. Users can select a year to view a histogram and descriptive statistics of road incident death rate data in that year. (It doesn't affect the graph on the right side.)
   2. Users can pick a graph to display from the catalog by pressing the button.
   
**DataExploration**
   1. Users can select (filter) a duration from 1990 to 2019 to show the distribution of that specific duration, for example, starting in 2000 and ending in 2005.
   2. Users can filter the entities they want to include in the graph.
   3. Users can filter the type of death they want to include in the graph, for example, deaths of people between 50-69 years old and children between 0-4 years old, or deaths of people riding a bicycle. (Cannot filter both age and vehicle at the same time)
   4. Users can switch the graph unit between “Total deaths” and “Death rate”, and then the graph will visualise as the users want. “Total death” means that the unit will be people, while “Death rate” means that the unit will be people per 100,000 people.
   5. Users can switch the mode between “Standard” and “Top rankings”, and then the graph will visualise as the users want. “Standard” will show the average deaths under filtered conditions (at most 2 entities), while “Top rankings” will show only each death data of the top 5 countries with the most deaths/death rate.
   6. Users can select the type of graph they want, like a bar graph or a histogram, but some features might be disabled for the histogram.
   7. After selecting all of the wanted attributes, press “GENERATE” to generate the wanted graph.

**Dataset**
   1. Users can view and scroll the dataset as they want.

## Python files
|File| Usage |
|--------|--------------------|
|graph_ui.py|Main UI of the application.|
|pages.py|Page module which contains the frame of all 3 pages.|
|sub_component.py|Components which are used by some pages.|
|controller.py|Controller module which connects the generators to the UI.|
|graph_generator.py|Classes for generating graphs.|
|entity.py|Contains an Enum class of entity lists.|
|main.py|Main block for running the application.|

## Installing the Application
See [How to Install](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Installation) in the project wiki.

## Running the Application
1. Activate the Virtual Environment
   
   MS Windows: 
     ```
     .\env\Scripts\activate
     ```
   Unix or MacOS:
     ```
     . env/bin/activate
     ```
2. Run the command
   ```
   python main.py
   ```
3. Deactivate the Virtual Environment
   ```
   deactivate
   ```
## Project Documents
[Project Proposal](https://docs.google.com/document/d/16FDrOhwlrF2d_EaP7QpTq1581u-YMD_n5A2Fp7wgljw/edit?usp=sharing)

[Development Plan](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Development-Plan)

[UML Diagram](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/UML-Diagram)

[Data Processing](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Data-Processing)

## Source of Data
The datasets used in this project are from [Our World in Data](https://ourworldindata.org/) and [World Health Organization](https://www.who.int//)

1. [Death rate from road injuries, 1990 to 2019](https://ourworldindata.org/grapher/death-rates-road-incidents?tab=table)
2. [Deaths from road incidents, by type, 1990 to 2019](https://ourworldindata.org/grapher/road-deaths-by-type)
3. [Deaths from road incidents, by age, 1990 to 2019](https://ourworldindata.org/grapher/road-incident-deaths-by-age)
4. [Deaths from road injuries, 1990 to 2019](https://ourworldindata.org/grapher/number-of-deaths-from-road-injuries?tab=table)
5. [Population](https://ourworldindata.org/grapher/population?tab=table)
6. [Maximum speed limits by country](https://apps.who.int/gho/data/node.main.A1007?lang=en)
7. [Seat-belt law by country](https://apps.who.int/gho/data/node.main.A1003?lang=en)
