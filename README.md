# InversityCrownEstate_Team7_BantamBandits
Submission for Team 7 in Inversity's Crown Estate Hackathon

## Background

- The UK Coastline is rich with resources that can be used in a sustainable way to generate power.
- To create a new instance of power creation, requires many stakeholders to be identified and engaged with in a meaningful way.
- Only with high levels of engagement from all stakeholders can we be confident that the idea is good and that it has informed support across those stakeholders.
- Low levels of engagement may deceive us into believing that we have support only to be blocked at a later stage when the nature of the project comes to be more widely understood.
- A key resource that allows stakeholders to understand projects and their impacts is the [Marine Data Exchange](https://www.marinedataexchange.co.uk/).
- This is an extremely rich source of reports and datasets. The sheer volume of the data available makes it quite daunting for non-expert users to find and understand some of the insights contained within.

## Problem Statement

- Create a natural language interface to a specialist Large Language Model such that members of the stakeholder community can easily conduct research to understand and find the relevant resources in the MDE repository. In this way, engagement with projects and issues will be much easier and faster progress will be able to be made.

## Solution

- LLMs have extraordinary capability to understand the intent of large bodies of knowledge and to subsequently synthesize knowledge fragments into a coherent answer to a natural language question.
- We have built a GPT using the no-code tools from OpenAI.
- We incorporated a number of PDFs from the MDE website that explain information about the data contained therein.
- We were hoping to use an API to get a list of all the data sources and the metadata including the summaries from the MDE website but our research indicated that there are no public APIs available.
- We then switched to a “scrape” solution but in the time available were unable to get BeautifulSoup to give us the download URLs and then a `requests.get` to actually download the XML.
- That proved fruitless due to the dynamic nature of the file downloads being handled with JS functions rather than `<a>` tags.
- If we had longer, we could utilize Playwright to achieve it.
- If we were properly engaged, then a private API or some other systematic way of getting the data would be simpler and much faster.
- So we resorted to managing it “old school” with Ctrl+A Ctrl+C Ctrl+V.
- We wanted to build a UI to the GPT but found out...
- Link to GPT [MDEN](https://chatgpt.com/g/g-7V5jpmAFR-marine-data-exchange-ninja)

## PDFs

- **Impact statement 2023**:
  - Outlines the impacts and value of the MDE using case studies.
- **Using industry data for UK marine assessment and reporting**:
  - How maritime industry data is collected and how it informs the MDE.
- **Requirements for providing survey data**:
  - Outlines different sectors of the MDE.
  - The process and requirements for providing the data.
- **Data valuation reports**:
  - Further case studies and more in-depth analysis of the MDE.
