# ProductVibe Roadmap

_Source: `roadmap.csv` — 233 ideas exported from Jira_

_Generated: 2026-04-29_

## Overview

- **Total ideas:** 233
- **Project:** ProductVibe (`PROD`)
- **Project lead:** Tyler Carty

### By status

| Status | Count |
|---|---:|
| Parking lot | 159 |
| Done | 24 |
| Now | 20 |
| Later | 8 |
| Product Intake | 7 |
| Delivery | 6 |
| Planned | 5 |
| Next | 2 |
| Discovery | 1 |
| Ready for delivery | 1 |

### By initiative

| Initiative | Count |
|---|---:|
| Connect | 19 |
| ION | 19 |
| Virtual Coordinator | 18 |
| Prescriber | 11 |
| Concierge | 9 |
| Ascend Multi-Channel Roadmap | 9 |
| Pulse Runner Improvements | 8 |
| Growing Onc. Segment | 7 |
| RCS | 6 |
| Independent Initiatives | 6 |
| Response Monitoring | 5 |
| App User Expierience | 5 |
| App Retention | 5 |
| RightChannel | 4 |
| Web Chatbot | 3 |
| Ascend Integrations | 3 |
| Sample Integrations | 3 |
| Inventory Scheduling | 3 |
| IM AI Automation | 2 |
| Agentic Field Force Platform | 2 |
| Reporting | 1 |
| Persona | 1 |
| Security and Compliance | 1 |
| Channels - Intelligent Media | 1 |
| Concierge: Sample Request Automation | 1 |
| Content Affinity | 1 |
| HCP Journeys | 1 |
| Internal Automation | 1 |
| Network Coverage | 1 |
| AI Voice Survey | 1 |
| IQVIA Data | 1 |
| _(no initiative)_ | 75 |

---

## Ideas by status

## Now (20)

### [PROD-201](https://impiricus.atlassian.net/browse/PROD-201) — Connect - HCP Inbound via QR Code v1 (Intelligent Media)

- **Initiative:** Connect
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 24/Sep/25 9:54 AM
- **Updated:** 15/Apr/26 10:42 AM

**Description**

#### Overview

- Currently we only can initiate Rep Connect HCP-Rep convos by sending an Ascend Pulse message to HCPs and HCPs replying rep (Outbound requests only)
- However, this limits the amount of HCPs we could ultimately target, so we want to explore Direct Outreach or HCP Inbound (also requested by Axsome).
- Goal is that we could have a QR code or number to text on any brand website, collateral, banner ad, etc. and say if you’d like to speak to a rep, text here.
  - can also be other Pharma roles, such as MSL, FRM, etc
- This person texting for a connection could be either an HCP in our network, HCP not in our network, office staff or some random person.
- We want to create a small NPI validation workflow to validate an HCP, and will determine best use cases for storing non HCPs. 
- Once we validate this person, then we will work with the client (Axsome) on how they want these direct outreachs connected to their Reps. 
  - First client to use this will be Axsome

#### Value for our Business

- Direct outreach drives engagement
- Direct outreach foundation for Connect can be used for other channels
  - MSL Direct Outreach
  - VC Direct Outreach

#### Value for our Customers

- similar to ours, it drives engagement 

#### What’s In Scope

- Ability for a person to scan a QR code or text a regular number
- Ability for HCP (someone with NPI) or Office Staff to be connected
- NPI validation 
  - For HCPs, the NPI provided by them is validated and we pull info from NPPES registry to pass on to the rep via Rep Connect
*** we pull NPI zip to map them to a Rep
  - For Office Staff, we will only pass on the information provided
*** we ask them for a zip code to map them to a Rep
- Zip to Terr mapping
  - per Axsome provided sheet, we will map HCPs / Office Staff based on the zip code of the HCP/ Office Staff
  - all Axsome digital reps (DSAMS) are assigned to Territorities, which are mapped to zip codes
- Connect to Rep via Rep Connect
  - HCP / Office Staff will then be connected directly to Rep 
  - Rep will receive SMS notification of conversation
  - conversation will continue with Rep using Rep Connect portal
- Also in scope, potentially connecting HCPs to Reps whenever an HCP fills out the Request a Rep on HCP brand website

#### What’s Out of Scope

- Short code texting - not in scope
  - requires ongoing costs and setup process
*** determine if there is a business need before pursuing
- Direct Outreach connected to other channels besides SMS
  - starting with direct outreach available via QR code
  - will also add to chatbot in 2026 

----

*Update as of 10/31/25:*

- Direct outreach flow has been high-level reviewed by Axsome (supporting HCPs & Office Staff)
- On track to complete initial direct outreach flow by Q4 2025
- Initial scoping complete, divided into 3 parts
- Left to do
  - Part 1 - Anna coordinate bandwidth short code (ability to text “rep” to 53455 and get connected to Axsome Auvelity rep) [https://impiricus.atlassian.net/browse/AS-408](https://impiricus.atlassian.net/browse/AS-408|smart-link) 
*** done [https://impiricus.atlassian.net/browse/AS-224](https://impiricus.atlassian.net/browse/AS-224|smart-link) 
  - Part 2 - NPI validation [https://impiricus.atlassian.net/browse/AS-252](https://impiricus.atlassian.net/browse/AS-252|smart-link) 
  - Part 3 - Zip code to Ter mapping [https://impiricus.atlassian.net/browse/AS-386](https://impiricus.atlassian.net/browse/AS-386|smart-link) 
  - Misc - 
*** UI improvements to tag direct outreach in Rep Connnect
*** backlog - manually map HCP outreach to Rep Connect 
- Axsome direct outreach to do
  - get direct outreach MLR approved
  - provide any MLR specific language or T&Cs
  - final QA on workflow

----

Currently we only can initiate Rep Connect HCP-Rep convos by sending an Ascend Pulse message to HCPs and HCPs replying rep.
However, this limits the amount of HCPs we could ultimately target, so we want to explore Direct Outreach (also requested by Axsome).

Goal is that we could have a QR code or text “rep” on any brand website, collateral, banner ad, etc. and say if you’d like to speak to a rep, text here.

This person texting could be either an HCP in our network, HCP not in our network, office staff or some random person.

We want to create a small NPI validation workflow to validate an HCP, and will determine best use cases for storing non HCPs. 

Once we validate this person, then we will work with the client (Axsome) on how they want these direct outreachs connected to their Reps. 

####


### [PROD-152](https://impiricus.atlassian.net/browse/PROD-152) — Mine New Numbers for Oncologists from Clay

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-08-01","end":"2025-08-01"}
- **Project target:** {"start":"2025-11-28","end":"2025-11-28"}
- **Created:** 25/Aug/25 11:52 AM
- **Updated:** 20/Nov/25 4:02 PM

**Description**

Continue finding new numbers for Oncs via Clay:

- Prioritize previously nuclear opted out Oncs as part of [https://impiricus.atlassian.net/browse/DT-318](https://impiricus.atlassian.net/browse/DT-318|smart-link)


### [PROD-110](https://impiricus.atlassian.net/browse/PROD-110) — Marketing HCP Responsiveness Prediction Capabilities

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Innovation
- **Project start:** {"start":"2025-09-02","end":"2025-09-02"}
- **Project target:** {"start":"2025-12-26","end":"2025-12-26"}
- **Created:** 15/Aug/25 4:14 PM
- **Updated:** 10/Dec/25 7:32 AM

**Description**

The plan is to drum up excitement around ION in Q4 2025 by publishing the “Predicting HCP Responsiveness” paper to arxiv.org & submitting it to an academic journal.

*Update (11.24.25):*

- We published on arxiv.org ([here](https://arxiv.org/abs/2511.17658))
- We submitted to the “[Computer Methods and Programs in Biomedicine](https://www.sciencedirect.com/journal/computer-methods-and-programs-in-biomedicine)” (submission attached)

Overview of broader epic can be found in [https://impiricus.atlassian.net/browse/INT-2590](https://impiricus.atlassian.net/browse/INT-2590|smart-link).


### [PROD-156](https://impiricus.atlassian.net/browse/PROD-156) — ION Infrastructure Strategy & Implementation

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Innovation, Operational Efficiency
- **Project start:** {"start":"2025-08-01","end":"2025-08-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 25/Aug/25 12:12 PM
- **Updated:** 04/Mar/26 10:04 AM

**Description**

#### Overview

This initiative focuses on establishing the end-to-end ION delivery workflow, including defining inputs, outputs, and integration points with the existing PulseRunner system. It covers determining the implementation strategy and standing up infrastructure needed to support ION-based delivery.

#### Value for our Business

Scalable infrastructure enables faster algorithm iteration, cleaner integration, and reduced future engineering overhead. It creates the foundation required to operationalize ION and accelerate optimization testing across campaigns.

*Business Drivers:* Scalable, Operational Efficiency, Innovation

#### Value for our Customers

Customers benefit from a more stable, predictable, and scalable delivery system that supports future optimization improvements. This foundation ensures campaigns continue to run smoothly while enabling more advanced delivery behaviors over time. This helps us hold true to our ethos of stopping the spam and delivering meaningful messaging to the right HCPs.

#### What’s In Scope

- Defining the ION workflow architecture
- Establishing required inputs/outputs
- Mapping interactions with PulseRunner services
- Building the infrastructure to support ION-driven delivery

#### What’s Out of Scope

- The optimization algorithm itself
- Any advanced pacing, scheduling, or optimization enhancements


### [PROD-251](https://impiricus.atlassian.net/browse/PROD-251) — ION Algorithm v1

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Innovation, Network Health, Operational Efficiency
- **Project start:** {"start":"2025-08-01","end":"2025-08-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 10/Dec/25 6:49 AM
- **Updated:** 04/Mar/26 10:04 AM

**Description**

#### Overview

This initiative focuses on implementing the ION algorithm to achieve full parity with current PulseRunner scheduling, pacing, and delivery logic. The goal is to ensure ION can replicate existing performance and decision making behaviors before introducing new optimizations.

#### Value for our Business

Algorithmic parity ensures a safe migration path to ION while maintaining reliability and performance expectations. It also provides a controlled baseline from which we can introduce and measure future optimizations.

*Business Drivers:* Scalable, Operational Efficiency, Innovation

#### Value for our Customers

Customers maintain confidence that campaign delivery remains consistent while benefiting from a more flexible and scalable algorithmic engine. Establishing parity ensures no disruption to pacing, impression delivery, or target fulfillment when transitioning to ION.

Customers shouldn’t be aware of any changes when we switch over to the ION algorithm.

#### What’s In Scope

- Inventory forecasting, scheduling, pacing, and delivery logic inside the ION algorithm
- Confirming parity in performance through testing

#### What’s Out of Scope

- New optimization strategies, dynamic tuning experiments, or A/B testing beyond achieving baseline parity are excluded


### [PROD-83](https://impiricus.atlassian.net/browse/PROD-83) — ION: Intelligently Optimized Network

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Innovation, Network Health, Operational Efficiency
- **Created:** 23/Jul/25 10:46 AM
- **Updated:** 03/Mar/26 9:19 AM

**Description**

#### Overview

This initiative establishes ION as Impiricus next generation intelligent delivery network. We’re unifying infrastructure, algorithmic optimization, research insights, and new campaign structures to deliver smarter, more flexible, and more precise HCP engagement. It represents the end to end transformation of how Pulses/Sparks are scheduled, paced, and optimized across their lifecycle.

#### Value for our Business

ION unlocks a scalable, data-driven delivery engine that increases campaign efficiency, accelerates experimentation, and supports multi-month flighted campaigns with improved inventory flexibility. It positions Impiricus to continuously incorporate new variables, signals, and optimization techniques that drive long-term differentiation.

*Business Drivers:* Operational Efficiency, Network Health, Business Growth, & Innovation

#### Value for our Customers

Customers receive more accurate, timely, and context aware HCP engagement through an algorithm that intelligently adapts delivery to performance and behavioral patterns. The system improves pacing reliability, enhances message relevance, and supports extended campaign durations that better align with brand needs.

#### What’s In Scope

- Building the foundational ION infrastructure
- Developing Algorithm v1 to achieve PulseRunner parity
- Incorporating marketing and research insights into the optimization model
- Enabling flighted campaigns that span multiple months
- Establishing frameworks for future optimization layers that leverage new variables and data signals

#### What’s Out of Scope

- h1. Optimized Pacing Enhancements:

This initiative is focused on enhancing how PulseRunner schedules, delivers, and paces Pulses/Sparks by leveraging a proprietary optimized delivery algorithm.

### Duration Framework:

This initiative is part of the broader Message Frameworks Optimization revamp.

We likely won’t roll out changes until Q1 2026 since we want to unlock as much incremental budget as possible in Q4.

*Update 7/28/25:*

- Todd had a call with the brand lead from Daralex around budget for the rest of year budget & raised longer flighting
  - "Can go from planned pulses on a defined timeline to a longer timeline to hit higher performance due  to system optimizations"
*** They really liked this selling point
*** But Todd thinks the key is that we're still giving them the option between the 2 duration choices
- Majority of these conversations will take place in Q1 of next year
  - Todd expects the majority of them will be longer duration but the top campaigns still need to be on expedited time
  - Todd thinks it will be a 70/30 breakdown around during longer flights v. not
- We need to sync internally and put together a process for recommended timing, reporting, etc.
  - Todd's goal is 200k over a 3 month

*Notes from Product Summit on 8/18/25:*

- Is there concern with having 3-month pacing rolled out before ION is released?

### Marketing ION Capabilities

Publications, reports, AI Papers etc. are very important to the overall ION strategy. As we roll out enhancements to our delivery optimizations and capabilities with ION, we want to ensure we’re marketing these competitive advantages.

The “Impiricus Research Group” composed of Alan, Daanish, Or, Phil, & Rafay meets on a regular basis to discuss findings and research that we can eventually turn into blog posts or formal research papers.

This is an _evergreen initiative_ but the plan is to drum up excitment around ION by submiting the “[Predicting HCP Responsiveness](https://docs.google.com/document/d/1NRSV5CJfgOhJHkkkfVVWfQJdAH4-3kibPW97vj4HReI/edit?tab=t.0)” paper in Q4 of 2025.

Other ideas include potentially patenting ION technology & expanding our “Impiricus Research Group” to outside members. Daanish has been reaching out to some members of the research community with the below information to see if they’re interested:

- Impiricus Research Group advances applied AI and behavior analytics in healthcare by developing interpretable, trustworthy, and domain-grounded language technologies to improve how healthcare providers exchange, comprehend, and utilize critical information.
- “adaptive fine-tuning for trustful HCP messaging” where we selectively fine-tune LLM input encoding layers to try and improve consistency and credibility of generating HCP messages
- “compositional interpretation of clinical directives in HCP engagement” where we probe LLMs to see whether they can maintain correct relational interpretation (in this case, medical interactions or dosing regimens) by analyzing the compositional understandings. We can a similar approach to a CLIP concept binding evaluations


### [PROD-84](https://impiricus.atlassian.net/browse/PROD-84) — Campaign Flight Commercialization

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health, Operational Efficiency
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 23/Jul/25 10:48 AM
- **Updated:** 03/Mar/26 9:19 AM

**Description**

#### Overview

This epic focuses on enabling multimonth campaign flights that give ION greater flexibility in inventory scheduling and delivery optimization. It also establishes a repeatable workflow for CS and Sales to position, sell, and manage duration based campaign structures.

#### Value for our Business

Commercializing flighted campaigns unlocks improved delivery efficiency across inventory. A standardized workflow ensures consistent messaging, smoother execution, and scalable rollout of this new offering.

*Business Drivers:* Operational Efficiency, Network Health

#### Value for our Customers

Customers benefit from increased performance when we have more flexibility to ensure all of their delivery goals are being met against high performing inventory. Clear guidance on timing, reporting, and planning helps brands understand how to best leverage longer flight durations.

#### What’s In Scope

- Defining the operational workflow for CS and Sales to sell and manage multi-month flights
- Including recommended campaign timing
- Establishing internal alignment, documentation, and enablement materials needed to support commercialization

#### What’s Out of Scope

- Technical enhancements to the algorithm or infrastructure beyond what is necessary to support flighted campaigns are excluded


### [PROD-192](https://impiricus.atlassian.net/browse/PROD-192) — Spark Portal Improvements

- **Initiative:** Pulse Runner Improvements
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 15/Sep/25 12:59 PM
- **Updated:** 04/Mar/26 8:51 AM

**Description**

#### *Overview*

This epic focuses on updating the Spark Configuration Portal in PulseRunner to streamline the pulse setup process and reduce manual work for Implementation Managers. The goal is to simplify workflows, improve usability, and eliminate repetitive configuration tasks.

#### *Value for our Business*

Workflow simplification improves operational efficiency, reduces setup time, and minimizes manual errors. These improvements increase team scalability and free bandwidth for higher-value tasks.

*Business Drivers:* Operational Efficiency, Platform Integrity

#### *Value for our Customers*

Customers benefit from faster onboarding and more reliable campaign configuration, improving delivery accuracy and reducing time to launch for initial integration.

#### *What’s In Scope*

- UI/UX improvements to the portal, automating repetitive setup steps, introducing data validation, refining form logic, and consolidating configuration fields

#### *What’s Out of Scope*

- Full redesign of PulseRunner’s architecture


### [PROD-193](https://impiricus.atlassian.net/browse/PROD-193) — Reporting Improvements in PR

- **Initiative:** Pulse Runner Improvements
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Operational Efficiency
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 15/Sep/25 1:07 PM
- **Updated:** 04/Mar/26 8:51 AM

**Description**

#### *Overview*

This epic enhances PulseRunner’s reporting capabilities by improving report ingestion reliability, enhancing report set ups, and providing greater visibility issues with reports that cause them to not process.

#### *Value for our Business*

Improved reporting pipelines reduce operational overhead, minimize data discrepancies, and increase trust in our analytics. Enhanced PLD visibility empowers internal teams and supports stronger insights for continuous optimization.

*Business Drivers:* Operational Efficiency, Customer Engagement

#### *Value for our Customers*

Customers receive more timely, accurate, and comprehensive reporting on campaign activity, improving overall satisfaction. Reliable ingestion ensures KPIs and performance metrics are always up to date.

#### *What’s In Scope*

- Strengthening ingestion pipelines, improving monitoring and alerting, enhancing PLD reporting fields and access, and implementing data quality checks

#### *What’s Out of Scope*

- New external dashboards or client-facing analytics revamps


### [PROD-233](https://impiricus.atlassian.net/browse/PROD-233) — PulseRunner Improvements

- **Initiative:** Pulse Runner Improvements
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2027-12-01","end":"2027-12-31"}
- **Created:** 01/Dec/25 4:12 PM
- **Updated:** 03/Mar/26 9:15 AM

**Description**

#### *Overview*

This evergreen epic captures ongoing improvements to PulseRunner focused on increasing efficiency, reducing manual work, maintaining system reliability, and ensuring long-term scalability. It includes continuous enhancements that keep the platform stable & evolving with our business needs.

#### *Value for our Business*

Sustained investment in core infrastructure and workflows prevents technical debt, enhances uptime, and ensures PulseRunner remains scalable as volume and complexity grow. These improvements reduce operational load and help maintain high product quality.

*Business Drivers:* Operational Efficiency, Platform Integrity

#### *Value for our Customers*

Customers experience more reliable delivery, fewer disruptions, and overall stronger performance as the platform becomes more automated and efficient. Gradual improvements result in smoother campaign operations and more consistent results.

#### *What’s In Scope*

- Maintenance tasks, workflow optimizations, automation improvements, bug fixes, tech debt reduction, minor enhancements, and performance tuning

#### *What’s Out of Scope*

- Large feature builds, major architectural changes, or strategic investments tied to new product lines


### [PROD-346](https://impiricus.atlassian.net/browse/PROD-346) — Pulse & Spark Alerting (Short Term)

- **Initiative:** Pulse Runner Improvements
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 04/Mar/26 8:39 AM
- **Updated:** 04/Mar/26 8:43 AM

**Description**

#### Overview

This initiative focuses on improving alerting and visibility around *Pulse and Spark lifecycle events* within PulseRunner and Customer Success workflows.

Today, limited alerting and monitoring capabilities create operational blind spots when campaigns launch, pacing milestones are reached, or delivery goals are completed. This can lead to delayed awareness, manual monitoring, and inconsistent communication across internal teams.

This initiative will implement short-term alerting improvements to ensure teams receive timely notifications when important campaign events occur. The work will be designed to remain compatible with the longer-term infrastructure and notification systems currently being developed by the Unified Platform team.

#### Value for our Business

Improved alerting reduces operational friction and ensures internal teams have timely visibility into campaign activity and delivery milestones.

By proactively notifying stakeholders when key events occur, we reduce manual monitoring overhead, improve responsiveness to delivery issues, and strengthen internal coordination across Product, Operations, and Customer Success.

This also provides immediate operational improvements while maintaining alignment with future Unified Platform notification frameworks.

##### Business Drivers

Operational Efficiency & Platform Integrity

#### Value for our Customers

Customers benefit from faster awareness and response when campaigns launch, hit delivery milestones, or require adjustments.

Improved internal visibility allows Customer Success teams to provide more proactive support, maintain tighter pacing oversight, and ensure campaign execution aligns with expectations.

#### What’s In Scope

- Implementing alerts for Pulse and Spark launch events
- Creating notifications when key delivery milestones or goals are reached
- Enabling visibility for Customer Success teams when campaigns change status
- Improving internal monitoring of active campaign delivery events
- Designing alerting mechanisms that remain compatible with Unified Platform roadmap work
- Reducing reliance on manual campaign monitoring processes

#### What’s Out of Scope

- Full rebuild of the notification or alerting infrastructure
- Long-term platform notification architecture owned by the Unified Platform team
- Client-facing alerting or reporting features
- Major changes to PulseRunner core delivery systems


### [PROD-142](https://impiricus.atlassian.net/browse/PROD-142) — RCS Data Tracking

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-11-01","end":"2025-11-30"}
- **Project target:** {"start":"2026-03-01","end":"2026-03-31"}
- **Created:** 25/Aug/25 9:11 AM
- **Updated:** 04/Mar/26 8:51 AM

**Description**

#### Overview

This epic focuses on updating our internal data pipelines and database logic to correctly track RCS message events, especially given that all RCS messages originate from a single number per brand/sender. It ensures accuracy in attribution, reporting, engagement scoring, and historical analytics.

#### Value for our Business

Accurate data modeling is foundational for reliable reporting, attribution, and ION optimization down the road. It reduces risk of misclassification and ensures system integrity as RCS becomes a scaled channel.

#### Value for our Customers

Customers receive accurate reporting of RCS performance and can trust that engagement metrics reflect HCP behavior despite RCS leveraging a unified phone number.

*Business Driver:* Customer Engagement, Innovation

#### What’s In Scope

- Properly logging this messaging flow in the db
- Updating schemas to handle channel specific identifiers

#### What’s Out of Scope

- Cross channel sentiment scoring changes


### [PROD-144](https://impiricus.atlassian.net/browse/PROD-144) — Build RCS Configuration into Pulse Runner

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-10-01","end":"2025-10-31"}
- **Project target:** {"start":"2026-03-01","end":"2026-03-31"}
- **Created:** 25/Aug/25 9:15 AM
- **Updated:** 04/Mar/26 8:51 AM

**Description**

#### Overview

This epic covers the end to end technical integration with Bandwidth’s RCS API and the platform updates required to send and receive RCS messages. It includes messaging flow development, feature toggles, and compatibility checks to ensure seamless RCS support alongside SMS.

#### Value for our Business

Completing this integration enables us to modernize our messaging offering and support emerging channel standards, expanding our product’s relevance and competitive positioning.

#### Value for our Customers

Clients benefit from enhanced messaging capabilities such as rich media, branded sender verification, and improved message delivery. This will lead to more engaging user interactions.

*Business Driver:* Customer Engagement, Innovation

#### What’s In Scope

- Bandwidth RCS API integration
- Fallback logic to SMS when RCS is not supported
- Error handling
- Platform toggles for enabling RCS

#### What’s Out of Scope

- Twilio RCS integration

*NOTES from 12/10/25:*

- Let’s leverage the Bandwidth RCS Tool in order to use the “json” workflow currently in PR


### [PROD-214](https://impiricus.atlassian.net/browse/PROD-214) — RCS Client Implementation Pilot

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 31/Oct/25 9:02 AM
- **Updated:** 04/Mar/26 8:52 AM

**Description**

#### *Overview*

This epic manages the rollout of RCS messaging to a small set of pilot clients as part of a controlled Beta program. It validates performance, ensures operational readiness, and gathers feedback to inform general availability plans.

#### *Value for our Business*

A structured Beta reduces risk, strengthens our case for commercialization, and provides real world performance insights to refine the product. It also builds early client champions for RCS.

*Business Drivers:* Customer Engagement, Innovation

#### *Value for our Customers*

Pilot clients gain early access to RCS capabilities and receive enhanced messaging experiences that may improve engagement and campaign outcomes.

#### *What’s In Scope*

- Selecting a pilot client(s)
- Configuring RCS for their campaigns
- Establishing success metrics, monitoring performance, gathering customer feedback, and providing post-Beta recommendations

#### *What’s Out of Scope*

- Full-scale rollout


### [PROD-82](https://impiricus.atlassian.net/browse/PROD-82) — Response Scoring Cleanup

- **Initiative:** Response Monitoring
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Roadmap bucket:** Scopt-then-refine
- **Project start:** {"start":"2025-07-01","end":"2025-07-31"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 23/Jul/25 10:41 AM
- **Updated:** 04/Mar/26 9:03 AM

**Description**

This initiative is focused on ensuring the logic associated with scoring provider sentiment is accurate to ensure that we’re growing & protecting our Network.

Focus areas include:

- Cleaning up prompt scoring in ResponseActions table
- Re-engaging HCPs from incorrect scoring or strong negative responses

This will become an evergreen initiative but we’re aiming to have a lot of clean up efforts completed by the end of Q4 2025.

Spreadsheet where we’re keeping track of items changed in {{ResponseActions}} is [here](https://docs.google.com/spreadsheets/d/1L8Hja8dRHoQtG5JoHhcyd-mvRBe_NL-A3XD7QjAjU9g/edit?gid=305704777#gid=305704777).

*Notes from Product Summit on 8/18/25:*

- Keep track of the updates & impact these changes are having
- Spring cleaning can go to Phil’s team


### [PROD-112](https://impiricus.atlassian.net/browse/PROD-112) — VC Reporting v1

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Mike Gelber
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-09-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-12-01","end":"2025-12-31"}
- **Created:** 20/Aug/25 10:12 AM
- **Updated:** 18/Dec/25 5:19 PM

**Description**

#### Overview

This work is focused on internal and external reporting that we do for our Virtual Coordinators (VCs). We leverage dashboards, reporting, metrics and PLD to monitor VC performance and success. 

#### Value for our Business

Proper reporting and dashboards allows us to monitor VC performance and report on the interactions we are seeing via the VC. This, in turn, allows us to articulate the value prop for our customers both in the sales and delivery phases of our client programs. 

Finding a way to facilitate VC reporting that is robust and easy to configure allows us to scale quickly while maintaining detailed oversight of HCP <> VC engagement. The reporting in scope for this work allows our CS teams to generate comprehensive and detailed VC program read outs. 

Additionally, PLD reporting is typically a standard contractual requirement that we must meet to satisfy the terms of our client contracts. 

#### Value for our Customers

Customers want to know what they get out of the VC program, and our ability to report on HCP <> VC interactions provides visibility into the ways in which a VC enhances HCP engagement. Customers will be able to see trends in what HCPs are asking for, which brand content is most popular / relevant and rates of engagement. 

#### What’s In Scope

- A json PLD reporting template for our VCs, which can be re-used as a foundation / standard PLD format and modified (via json) as needed for every VC that is delivered
- The ability to generate the PLD from Pulse Runner > Reports
- A standard Sigma dashboard that can be built for each brand VC, with the help of our data team

#### What’s Out of Scope

- External-facing (i.e. directly accessible by clients) reporting tools
- Tools that allow our non-technical team members (e.g. project managers, sales team, etc.) to generate custom VC reports as desired


### [PROD-118](https://impiricus.atlassian.net/browse/PROD-118) — VC Studio v1

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Mike Gelber
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-10-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 20/Aug/25 10:19 AM
- **Updated:** 25/Feb/26 4:43 PM

**Description**

#### Overview

This work is focused on point-and-click internal tooling for the creation, configuration and deployment of brand-specific Virtual Coordinators (VCs). 

Currently, each brand VC is built by Impiricus Product and Engineering teams; with this work, we want to enable less technical teammates (e.g. CS, Sales, etc.) in building their own VCs with intuitive and easy-to-use interfaces. 

#### Value for our Business

Scalability. It currently takes our Product / Engineering teams 4-6 weeks to deliver each VC - a pace which isn’t scalable and won’t allow our company to grow in the way we need to reach future sales and profit goals. 

The goal with this work is to:

- Take VC build from weeks to hours
- Remove the need for technical expertise (developers)  to deliver each VC

#### Value for our Customers

Customers will realize faster implementation timelines and more flexibility in what gets built. With our current technical builds today, it can be hard to change certain VC functionality as we get close to deployment; as we move away from technical team delivery and rely more on point-and-click tooling, we will have more flexibility to make adjustments faster. 

#### What’s In Scope

- An internal admin portal where Impiricus team members can create, configure, test and deploy VCs
- The ability to view summary metrics for each manufacturer / brand / VC
- SMS as the only supported channel for one-click deployment 

#### What’s Out of Scope

- Impiricus user-management interfaces
- External (SaaS) capabilities
- Automated MLR content generation via scraping brand websites
- Ability to deploy to multiple channels (e.g. web chatbot, email, voice, etc.) with one click


### [PROD-197](https://impiricus.atlassian.net/browse/PROD-197) — Brand-Specific VC Builds (Manual)

- **Initiative:** Virtual Coordinator
- **Priority:** Low
- **Assignee:** Sam Thomas
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2025-10-01","end":"2025-10-31"}
- **Project target:** {"start":"2026-02-13","end":"2026-02-13"}
- **Created:** 17/Sep/25 3:22 PM
- **Updated:** 23/Feb/26 10:11 AM

**Description**

#### Overview

This work is focused on supporting our client commitments for Ascend contracts. While we work to expand our internal tooling capabilities, brand-specific Virtual Coordinator (VC) programs need to be built by our product and development teams.

Future state: there is easy-to-use tooling available for non-technical team members (CS, sales, etc.) to spin up and deploy VCs as desired, as well as a potential SaaS option where clients can manage their own VC build with ease. 

#### Value for our Business

We need to deliver on what we sell; dedicating technical resources to delivering on sold VC programs ensures we meet our client and sales commitments. 

By managing the first batch of VC builds with the technical team we can better understand what it takes to deliver a VC, identify opportunities for improvement and implement lessons learned along the way. This will give us a better understanding of how to build robust admin / tooling features for our teams.

#### Value for our Customers

Customers receive the VC programs that they purchased with Impiricus.

#### What’s In Scope

For each brand VC project:

- A Virtual Coordinator that responds to HCP messages with MLR-approved content
- Internal tools (e.g. Slack) where we can monitor and track HCP <> VC interactions / messages
- Proactive notifications via Slack, email and SMS to our Product and CS teams for things like Adverse Events, requests for MSL, etc
- A Sigma dashboard that shows VC metrics / performance
- PLD reporting

#### What’s Out of Scope

- “Intelligent” VCs that can:
  - Respond to and handle context (i.e. our current VCs are a one message in / one message out model where HCPs will receive a VC response for every message they send; future state, we’d like to implement a more robust VC that can wait for complete thoughts / multiple messages that come from HCPs and handle accordingly)
  - Handle HCP-specific request (e.g. wallet cards based on the HCP’s location, handling questions specific to the HCP’s region, etc.)
- Impiricus admin portals / tooling features - these are being built via other roadmap initiatives
- Rep Connect / Samples integrations - these are being built via other roadmap initiatives


### [PROD-277](https://impiricus.atlassian.net/browse/PROD-277) — VC Orchestrator v1

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Reporter:** Sam Thomas
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 18/Dec/25 3:39 PM
- **Updated:** 18/Dec/25 5:20 PM

**Description**

#### Overview

This work is focused on the backend infrastructure for a more scalable and sustainable Virtual Coordinator program in the future. The VC Orchestrator will be the handler for all things VC, including plug ins to other integrations like samples integrations. 

The VC Orchestrator will intake HCP messages and:

- Interpret the ask
- Route the message to the correct agent / handler, including things like:
  - A brand-specific VC
  - Samples integration workflows
  - Connect workflows (Rep / FRM / MSL Connect)

It will also be able to handle incoming messages from all of our Ascend channels as we add them to our ecosystem, including SMS and web chatbot in the shorter term.

#### Value for our Business

This allows us to scale our VC work and have a more intentional architecture for VC efforts. 

#### Value for our Customers

We will be able to deliver faster and more scalable. 

#### What’s In Scope

- Routing to VCs
- Notifications
- DB Schema
- VC Classifications
- Message handling
- Web Chatbot handling

#### What’s Out of Scope

- TBD


### [PROD-120](https://impiricus.atlassian.net/browse/PROD-120) — Web Chatbot v1

- **Initiative:** Web Chatbot
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2025-09-16","end":"2025-09-16"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 20/Aug/25 10:21 AM
- **Updated:** 25/Feb/26 4:44 PM

**Description**

#### Overview

The goal if this work is to expand our approach to omnichannel  by offering a web chatbot for brand websites. The web chatbot will be powered by the brand’s Virtual Coordinator (VC) and we will have the ability to surface additional resources on the web chatbot menu in case the brand team wants to allow quick-click access to certain materials. 

#### Value for our Business

Expanding our offering via web chatbot strengthens our position against competitor offerings like [Ostro](https://www.ostrohealth.com/) and is the starting point for achieving a connected ecosystem where HCPs can engage with our products in their preferred style of communication / modality. 

#### Value for our Customers

Our customers will continue to choose Impiricus as their preferred partner as they will no longer need to contract with other offerings just to receive the web chatbot functionality (e.g. Axsome, who was using Impiricus for SMS and Ostro for web chatbot; they are now getting rid of Ostro and committing 100% to Impiricus). Building out our omnichannel presence expands the brand reach and interaction points with HCPs. 

#### What’s In Scope

- Ability to set branding information for the chatbot, including:
  - A brand-specific header
  - Configuration over color schemes - ability to set up to three brand-specific colors
- Two-way conversations between a HCP and the chatbot, powered by a brand-specific VC
- NPI validation - ask the HCP to enter their NPI so we know who we’re talking to
  - Note - for v1, the NPI validation is more of a regex check to confirm 10 digits / numeric only
  - For v2+, we will consider NPI validation against the NPPES database
- Link to Popular Resources (actual resources to be customized with client)
  - The following items will be configurable:
*** Resource categories
*** Resource names
*** Resource placeholder text
*** Resource URLs
- Link to Important Safety Information (if relevant to brand)
- Link to Impiricus terms & conditions and privacy policy
- Reporting (where possible - we may not be able to capture clicks on resource tiles if the HCP is not engaging with the chatbot first)
- JSON-based configuration options for resource cards / tiles

#### What’s Out of Scope

- NPI validation via NPPES
- Integrations:
  - IQVIA AIM
  - Rep Connect
  - Samples
- Continuous conversations (e.g. starting in web and moving to SMS or vice versa)
- Admin portal / configuration tools
- Human in the loop / human override for a web chatbot convo


## Next (2)

### [PROD-206](https://impiricus.atlassian.net/browse/PROD-206) — Automated SigText (eprescribe enhancement)

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Value drivers:** Customer Engagement, Platform Integrity
- **Project start:** {"start":"2026-04-01","end":"2026-04-30"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 08/Oct/25 12:13 PM
- **Updated:** 04/Mar/26 10:08 AM

**Description**

#### *Overview*

This initiative delivers a set of critical enhancements to the ePrescribing experience that were deferred from the initial launch due to time constraints. These improvements bring DocUpdate closer to modern EMR standards, increase Surescripts reliability, and reduce prescribing errors and downstream pharmacy friction.

#### *Value for Our Business*

- Strengthens DocUpdate’s competitive positioning against modern EMRs.
- Improves Surescripts success rates and operational reliability.
- Reduces support burden caused by Sig validation errors
- Increases prescriber trust and long-term platform adoption.
- Closes key functional gaps identified post-launch.

#### *Value for Our Customers*

- Faster and more accurate prescription entry through automated Sig generation.
- Fewer Surescripts rejections due to validation errors.
- Clearer dosing display for medications.
- A more modern, EMR-like prescribing experience.

#### *What’s In Scope*

- *Automated SIG Builder* – Generates patient directions based on prescription details entered by the prescriber.
- Full QA validation against Surescripts and pharmacy acceptance.

#### *What’s Out of Scope*

- Net-new ePrescribing feature categories beyond the listed enhancements.
- Changes to Surescripts network relationships or certification scope.
- Pharmacy inventory, pricing, or prior authorization tooling.
- Major prescribing UI redesign beyond what is required to support these upgrades.


### [PROD-210](https://impiricus.atlassian.net/browse/PROD-210) — Enable users to add "favorites" list of medications

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2027-07-01","end":"2027-07-31"}
- **Created:** 24/Oct/25 11:36 AM
- **Updated:** 14/Apr/26 4:30 PM

**Description**

#### *Overview*

Introduce a Medication Favorites feature that allows users to save frequently prescribed medications with all associated prescription details as reusable “favorites.” Users can create, manage, and select favorite medications, which will automatically populate the prescription entry fields. The clinician still reviews, signs, and sends each prescription, but the data entry burden is significantly reduced.

----

#### *Value for our Business*

- Increases user efficiency and satisfaction, boosting long-term retention and daily usage.
- Differentiates DocUpdate as a prescribing tool optimized for real clinical workflows.
- Strengthens product stickiness by becoming the default place clinicians write frequent prescriptions.
- Reduces cognitive load for users, reinforcing trust and habitual usage patterns.
- Creates a natural platform for future enhancements (favorite sets, templates, specialty workflows).

----

#### *Value to our Users*

- Dramatically reduces time and effort required to prescribe commonly used medications.
- Minimizes repetitive data entry, especially for clinicians who frequently prescribe the same treatment regimens.
- Supports faster patient care by streamlining the prescription process.
- Maintains safety—users still review and sign every prescription, but with much less manual input.
- Provides a customizable workflow tailored to each clinician’s prescribing habits.

----

#### *What’s in Scope*

- Ability for users to create medication favorites that store all prescription details
- UI for creating, editing, and deleting favorites.
- Ability to select a favorite and auto-populate the prescription form with stored details.
- Ensuring full review and signature flow remains compliant and unchanged.

----

#### *What’s Out of Scope*

- Auto-sending prescriptions without user review or signature.
- Advanced templating systems (e.g., bundled medication sets, specialty protocols) beyond basic favorites.


## Later (8)

### [PROD-189](https://impiricus.atlassian.net/browse/PROD-189) — ION Algorithmic Optimizations

- **Initiative:** ION
- **Priority:** Low
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health, Operational Efficiency
- **Project start:** {"start":"2026-10-01","end":"2026-10-31"}
- **Project target:** {"start":"2027-06-01","end":"2027-06-30"}
- **Created:** 15/Sep/25 9:08 AM
- **Updated:** 05/Mar/26 4:29 PM

**Description**

#### Overview

This epic focuses on advancing the ION algorithm beyond its initial version by incorporating new variables, historical performance insights, and additional signals that improve optimization quality. It serves as the umbrella for ongoing refinement and iterative enhancement of ION’s decisioning engine.

#### Value for our Business

Leveraging historical data allows us to systematically improve ION’s accuracy, efficiency, and predictive power. Continuous optimization ensures that the algorithm becomes smarter over time, driving better results with minimal incremental operational cost.

*Business Drivers:* Operational Efficiency, Network Health

#### Value for our Customers

Customers benefit from improved campaign performance driven by data-backed enhancements. Campaigns will deliver more personalized and effective HCP engagement by incorporating insights such as content length, content type, and historical engagement trends.

#### What’s In Scope

- Identifying and integrating new variables and performance signals based on historical data
- Running experiments to validate accuracy of data signals
- Refining algorithmic logic to improve scheduling, pacing, and delivery decisions

#### What’s Out of Scope

- Large scale changes to ION’s behavior


### [PROD-181](https://impiricus.atlassian.net/browse/PROD-181) — Controlled Substances

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Business Growth
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2027-10-01","end":"2027-12-31"}
- **Created:** 05/Sep/25 5:05 PM
- **Updated:** 02/Mar/26 8:54 AM

**Description**

#### Overview

Adding support for EPCS (eprescribe controlled substances) to DocUpdate.

#### Value For our Business

The value for the business is that this will continue to increase physician love and loyalty if we’re able to provide the value they are looking for 

#### Value to our Users

Our users want to be able to prescribe everything available to them on their EMR or within their practice. Enabling EPCS will remove blockers for eligible users to send CS medications. 

Note: Last time data was pulled before CS prescribing was turned off showed 1.1% of users had sent CS medications

#### What’s in Scope

- Enabling EPCS with surescripts 
- Full audit by FDA approved auditor
- Data update to include CS in the search for eligible users 

#### What’s out of Scope

TBD


### [PROD-194](https://impiricus.atlassian.net/browse/PROD-194) — PR Roles & Permissions Granularity

- **Initiative:** Pulse Runner Improvements
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency, Platform Integrity
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 15/Sep/25 1:10 PM
- **Updated:** 04/Mar/26 8:53 AM

**Description**

#### *Overview*

This epic introduces a formal role and permissions system within PulseRunner to ensure internal users have appropriate access levels aligned with their responsibilities. The goal is to improve system security, reduce operational risk, and support scalable team workflows.

#### *Value for our Business*

A structured permissions framework reduces accidental configuration changes and supports future roles based product extensions. It also enables PulseRunner to scale across larger teams with clearer guardrails.

*Business Drivers:* Operational Efficiency, Platform Integrity

#### *Value for our Customers*

Customers benefit from improved reliability and consistency in campaign setup and operations, reducing risk of errors due to incorrect access. This helps ensure smoother execution and higher-quality deliverables.

#### *What’s In Scope*

- Defining user roles, mapping required permissions, implementing authorization logic, updating UI controls, and creating audit logging for sensitive actions. Includes documentation and internal onboarding.

#### *What’s Out of Scope*

- Major UX redesigns or creation of a full RBAC self-service admin console. SSO enhancements or identity provider integrations are not included at this stage


### [PROD-182](https://impiricus.atlassian.net/browse/PROD-182) — Reporting - Establish Sigma as source of truth

- **Initiative:** Reporting
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-07-16","end":"2025-07-16"}
- **Project target:** {"start":"2026-01-15","end":"2026-01-15"}
- **Created:** 05/Sep/25 5:14 PM
- **Updated:** 11/Dec/25 3:19 PM

**Description**

#### *Overview*

The goal of this initiative is to centralize all key DocUpdate metrics within Sigma, eliminating reliance on manually maintained spreadsheets. By creating a single, real-time source of truth for performance data, we will improve visibility, accuracy, and trust in our reporting across teams.

#### *Value for Our Business*

- Eliminates manual data maintenance and associated operational overhead.
- Reduces risk of reporting errors and conflicting numbers across teams.
- Improves decision-making speed and confidence at the leadership level.
- Enables scalable reporting as DocUpdate continues to grow.

#### *What’s In Scope*

- All data in metrics doc: [https://docs.google.com/spreadsheets/d/1TGHYJ8msxMB9RzF1iFWw7TvX29XtIiawqD3_JUiXD4M/edit?pli=1&gid=1889318441#gid=1889318441](https://docs.google.com/spreadsheets/d/1TGHYJ8msxMB9RzF1iFWw7TvX29XtIiawqD3_JUiXD4M/edit?pli=1&gid=1889318441#gid=1889318441|smart-link) 
- User signup data
- Prescription activity data
- Concierge metrics
- CAC data pulled from Android/IOS

#### *What’s Out of Scope*

- Data from Appsflyer
- Organic vs paid 
- Mixpanel metrics
- Ad spend outside of Meta


### [PROD-102](https://impiricus.atlassian.net/browse/PROD-102) — AI Call Center

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Won't do
- **Project start:** {"start":"2025-01-01","end":"2025-03-31"}
- **Project target:** {"start":"2025-07-01","end":"2025-07-31"}
- **Created:** 04/Aug/25 2:49 PM
- **Updated:** 05/Sep/25 4:51 PM


### [PROD-179](https://impiricus.atlassian.net/browse/PROD-179) — Emailing sending capabilities 

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Created:** 05/Sep/25 4:45 PM
- **Updated:** 11/Sep/25 3:15 PM

**Description**

This may end up being fully marketing owned (no engineering involvement. Using a tool like beehiiv)


### [PROD-180](https://impiricus.atlassian.net/browse/PROD-180) — Persona enhancements (workflow automations)

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Project start:** {"start":"2025-07-16","end":"2025-07-16"}
- **Project target:** {"start":"2025-09-15","end":"2025-09-15"}
- **Created:** 05/Sep/25 4:52 PM
- **Updated:** 11/Sep/25 3:03 PM

**Description**

Add workflow enhancements to the Persona verification process to reduce the manually intervention that is required by Shylee and Angela’s team


### [PROD-96](https://impiricus.atlassian.net/browse/PROD-96) — Journal Summaries - PDF download (web only)

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Won't do
- **Project start:** {"start":"2025-05-01","end":"2025-05-31"}
- **Project target:** {"start":"2025-04-01","end":"2025-06-30"}
- **Created:** 04/Aug/25 2:45 PM
- **Updated:** 05/Sep/25 4:42 PM


## Planned (5)

### [PROD-145](https://impiricus.atlassian.net/browse/PROD-145) — Implementation Manager - AI Automation

- **Initiative:** IM AI Automation
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency
- **Created:** 25/Aug/25 9:18 AM
- **Updated:** 04/Mar/26 8:53 AM

**Description**

Update as of 11/3/25

- Roadmap work ongoing; this larger initiative has a few smaller components as well
  - kicked off research for Automate Pulse Creation (separate roadmap item)
  - Q4 initiative to start on reporting overhaul (separate roadmap item)
  - PR overhaul to support ION
- IM documented current responsibilities and areas of improvement here [https://docs.google.com/document/d/1GoA4lrE0Yu7Uw6ilzUfyVXP944rBmI-BuvvM_KlZYc0/edit?tab=t.0](https://docs.google.com/document/d/1GoA4lrE0Yu7Uw6ilzUfyVXP944rBmI-BuvvM_KlZYc0/edit?tab=t.0|smart-link) 

----

A longer term initiative to scale IM capabilities via automation and/ or general PR improvements. IM team scope continues to grow

- Pulse and Spark message creation, testing and monitoring
- PLD Reporting for Pulse and Spark
- Spark configuration setups
- DWC creation

In November, Dev/ IM/ Product are meeting pre-F2F for a planning sessions.

A few other improvements that have been requested:

- DWC improvements - ability to view preview of DWC in PR while making them


### [PROD-121](https://impiricus.atlassian.net/browse/PROD-121) — Channels - Web Chatbot GA

- **Initiative:** Web Chatbot
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 20/Aug/25 10:22 AM
- **Updated:** 10/Dec/25 5:17 PM

**Description**

see Channels - Web Chatbot Beta - the goal of this ticket is to develop and release go live


### [PROD-311](https://impiricus.atlassian.net/browse/PROD-311) — Automated Pulse Monitoring & Alerting

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-10-16","end":"2026-10-16"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 24/Feb/26 2:20 PM
- **Updated:** 24/Apr/26 5:21 PM

**Description**

#### Problem(s) We Are Solving

IMs manually check every active pulse 3x per day to look at error logs and make sure we're not exceeding thresholds

#### Solution Approach

Implement monitoring of errors on per pulse basis for active pulses, and alert the IM teammember in a new slack channel if the pulse error logs exceed a certain threshold.

Two types of errors

1. Immediate alert if exceeded (rows 1 & 2)
1. Don’t alert until reached certain volume (80% of guaranteed deliveries?)

See errors and thresholds below.

#### Future considerations

Predictive analytics - knowing at 30% delivery if we’re trending towards values being off at 80% deliveries.

#### Errors & Thresholds

Pulse Manual Monitoring Checks

||Error||Meaning/Intuition||Threshold||Action Item||
|Required Related Messages Not Delivered|Failed because pre-req not delivered|Can expect 3-4% per each previous pulse in journey, i.e if M3, would expect no more than 8-10% -- otherwse a flag to look into. Always an off chance that is expected based on delivery of M1/M2|If super high and discovered to be unexpected: pulse needs to be paused, need support of data team to dive into non-deliveries so far and to revise TL based on that, new pulse needs to be created with updated TL / prereq structure if needed|
|No Phonenumber To Use|Someone is nuclear opted out in our system, via 'stop' or 'unsubscribe'|Usually won't see this over 3%|If super high like 8-10%, indication to reach out to data team for insights on TL|
|Other Bandwidth Error Detected|Twilio or Bandwidth Phone number for some reason wasn't able to get delivery on x% of people|Usually won't see this over 3%|If higher like 5+%, indication to try to manually reprocess failures and see if we can get delivery -- otherwise typically out of luck|
|Permission To Send Failed By Sp|Stored Proc for permission to send is a multitude of things, but usually due to a providers daysbetweenmessages|Common error, if above 3.6% typically an indication of Daysbetween issues|We pull a list of providers who failed for daysbetween specifically and update them to 1|
|Min Demeanor|Someoens dD is below our pulse's set threshold|Usually won't see this over 4-5%|If super high like 6+%, indication to reach out to data team for insights on TL|
|Min Believability|Someoens Believability is below our pulse's set threshold|Usually won't see this over 4-5%|If super high like 6+%, indication to reach out to data team for insights on TL|


### [PROD-312](https://impiricus.atlassian.net/browse/PROD-312) — AI Report Builder

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-05-04","end":"2026-05-04"}
- **Project target:** {"start":"2026-06-08","end":"2026-06-08"}
- **Created:** 24/Feb/26 2:38 PM
- **Updated:** 24/Apr/26 5:15 PM

**Description**

#### Problem(s) We Are Solving

*Client impact*

- Current SLA = 30-45 days
- Q4 '25 / Q1 '26 - Failed compliance at 60% when needed to be at 90% because we did not adhere to a rule to send to empty reports when no data. Not charged by CMI yet.

*Operational lift*

- Basit (how long to set up a custom report): 
  - existing: 1-2.5hrs, prolonged if pending items from CS/client
  - net new: between 2-5hrs, prolonged by understanding unique requirements, pending items from CS/client, dev deployment if needed
  - 65% setting up, 35% documenting, clarifying, etc
  - [pain points documented here](https://docs.google.com/spreadsheets/d/1lzk7wtswTge79yASxM3YbOj7Sm7QCTuds7-tl4v4clA/edit?gid=0#gid=0)
- Sam 
  - Manually combed through 5k+ rows of PLD data by hand to filter certain values and prep it for client
  - Addressed with a new stored procedure for VC, but concerns around scalability for multi-product campaigns

#### Solution Approach (experimental)

Add agentic AI support to the FIA process to accelerate setup with higher confidence by:

1. Ingesting FIA spec and supporting docs as inputs
1. Auto-generate outputs
   1. report rules file
   1. report table structure (output fields, field format, required vs. optional, source)
   1. expected values
1. Validate it’s own outputs, comparing against sample values from client & stored procedure values from DB
1. Support guided review & finalization by IMs
1. Provide a cross-functionally useful report overview that is easy for CS, QA, IMs, Product / Dev to understand

_(image: image-20260225-140243.png)_


### [PROD-362](https://impiricus.atlassian.net/browse/PROD-362) — Post Launch: AI Report Builder

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-06-16","end":"2026-06-16"}
- **Project target:** {"start":"2026-07-17","end":"2026-07-17"}
- **Created:** 24/Apr/26 5:15 PM
- **Updated:** 24/Apr/26 5:18 PM

**Description**

#### Problem(s) We Are Solving

*Client impact*

- Current SLA = 30-45 days
- Q4 '25 / Q1 '26 - Failed compliance at 60% when needed to be at 90% because we did not adhere to a rule to send to empty reports when no data. Not charged by CMI yet.

*Operational lift*

- Basit (how long to set up a custom report): 
  - existing: 1-2.5hrs, prolonged if pending items from CS/client
  - net new: between 2-5hrs, prolonged by understanding unique requirements, pending items from CS/client, dev deployment if needed
  - 65% setting up, 35% documenting, clarifying, etc
  - [pain points documented here](https://docs.google.com/spreadsheets/d/1lzk7wtswTge79yASxM3YbOj7Sm7QCTuds7-tl4v4clA/edit?gid=0#gid=0)
- Sam 
  - Manually combed through 5k+ rows of PLD data by hand to filter certain values and prep it for client
  - Addressed with a new stored procedure for VC, but concerns around scalability for multi-product campaigns

#### Solution Approach (experimental)

Add agentic AI support to the FIA process to accelerate setup with higher confidence by:

1. Ingesting FIA spec and supporting docs as inputs
1. Auto-generate outputs
   1. report rules file
   1. report table structure (output fields, field format, required vs. optional, source)
   1. expected values
1. Validate it’s own outputs, comparing against sample values from client & stored procedure values from DB
1. Support guided review & finalization by IMs
1. Provide a cross-functionally useful report overview that is easy for CS, QA, IMs, Product / Dev to understand

_(image: image-20260225-140243.png)_


## Discovery (1)

### [PROD-222](https://impiricus.atlassian.net/browse/PROD-222) — RightChannel Sentiment Scoring

- **Initiative:** RightChannel
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Customer Engagement, Network Health
- **Project start:** {"start":"2026-04-01","end":"2026-04-30"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 24/Nov/25 11:21 AM
- **Updated:** 03/Mar/26 11:29 AM

**Description**

#### Overview

This initiative focuses on designing and implementing a unified framework for sentiment scoring across multiple communication channels beyond SMS, such as Direct Outreach, VC, Rep Connect, Web Chatbot, Email, and DocUpdate. The effort includes determining how sentiment should be captured per channel and whether an overarching, cross-channel sentiment score is needed to inform ION’s optimization and routing logic.

#### Value for our Business

A multi-channel sentiment framework strengthens our ability to tailor engagement strategies, improves routing and optimization decisions, and positions Impiricus to support multichannel programs. Establishing a consistent sentiment model across channels future-proofs the platform and enhances ION’s ability to make holistic, context-aware decisions.

*Business Driver:* Network Health, Customer Engagement

#### Value for our Customers

Customers receive more relevant engagement across channels due to better understanding of HCP preferences and sentiment. A unified scoring approach creates more accurate personalization, higher engagement quality, and improved campaign outcomes.

#### What’s In Scope

- Evaluating whether existing Believability (B) and Demonstrated Demeanor (dD) scores should be extended to new channels
- Designing channel specific scoring logic (e.g., disposition toward email vs SMS)
- Determining whether an overall crosschannel score should exist

#### What’s Out of Scope

- Launching new channels themselves


## Delivery (6)

### [PROD-105](https://impiricus.atlassian.net/browse/PROD-105) — Independent Initiatives - AI-Powered Phone Surveys NEEDS DETAIL

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement, Innovation
- **Created:** 14/Aug/25 3:26 PM
- **Updated:** 10/Dec/25 1:16 PM

**Description**

##### *Summary*

The AI Phone Call HCP Insight Surveys product will allow healthcare professionals to participate in qualitative insight surveys via either an *AI-driven phone call* or an *online portal experience*.

The system will automate outreach, scheduling, question delivery, recording of responses, and (when applicable) immediate connection to a human representative or delivery of MLR-approved follow-up materials.

The goal is to replace or supplement manual 1:1 interviews and post-event surveys with scalable, convenient, and cost-effective automated options that maintain high-quality insight capture.

##### *Core Functionality Requirements*

###### *Phase 1 (MVP)*

1. *Survey Delivery Methods*

###* *AI Phone Call*

###** Simulates human interviewer style.
###** Delivers one question at a time, waits for complete response, then continues.
###** Live monitoring for support and fallback to human interviewer if AI fails.
1. 1. *Recruitment & Scheduling*

###* SMS invitations with incentive offer.
###* Link to select preferred survey format (phone call or portal).
###* Link to choose available time slots for phone calls.
###* Automated reminders for incomplete surveys (configurable, e.g., 3 hours / 8 hours).
1. 1. *In-Survey Experience*

###* Ability to incorporate short MLR-approved educational elements (e.g., 30–60 sec video or trial summary) before related questions.
###* Branching logic for follow-up questions based on responses.
###* Optional request during survey to connect with a pharma rep or MSL after completion.
###* Follow-up materials sent via SMS/email (MLR-approved content only).
1. 1. *Post-Survey*

###* Store and transcribe audio/video responses.
###* Tag responses for thematic analysis.
###* Trigger immediate post-survey action if requested (e.g., notify rep).

###### *Phase 2 (Enhancements)*

1. *Survey Delivery Methods*
   1. *Add Web/Portal Guided Survey*
##### HCP sees question text and hears AI read it.
##### User records answer and presses “Next” to proceed.
##### QR code link from invite to portal.
1. *Pause & Resume*
###* For web/portal surveys, allow HCP to pause mid-survey and resume later.
###* For phone call format, enable “hang up and call back later” continuation from last question.
1. *Expanded Follow-Up Options*
###* Warm transfer from AI survey directly to available rep/MSL.
###* On-demand educational resource navigation during survey.
1. *Additional Survey Formats*
###* Live human interview option as part of survey format selection.
###* Traditional form survey option for non-AI users.
1. *Gamification & CME*
###* CME credit eligibility integration.
###* Gamified elements (progress indicators, completion badges, optional leaderboards).
1. *Group/Focus Group Mode*
###* Enable multiple HCPs to join same AI-moderated session for collaborative insights.

##### *3. Acceptance Criteria*

###### *Phase 1 ACs*

- *AI Phone Call*
  - Given an HCP schedules a call, when the call starts, the AI must deliver the first question within 3 seconds.
  - AI must pause until HCP stops speaking, then deliver the next question.
  - If AI fails to recognize input after 2 attempts, system routes to human fallback.
- *Web/Portal Survey*
  - Given HCP accesses via QR code or link, when they start survey, question text and audio must display simultaneously.
  - “Next” button only enabled after answer is recorded.
- *Recruitment*
  - SMS invitation must contain: survey description, incentive, format selection link.
  - Reminder messages only sent if survey incomplete after configured time.
- *Educational Component*
  - If educational material is included, it must display before related question(s) and be fully skippable if client chooses.
- *Follow-Up Request*
  - If HCP requests follow-up, system sends MLR-approved materials or rep contact info within 60 seconds after survey completion.
- h4. *Phase 2 ACs*

- *Pause & Resume*
  - Web/Portal: Resume from last unanswered question when returning within 48 hours.
  - Phone: Resume call from last unanswered question when HCP calls back from same number.
- *Warm Transfer*
  - Upon HCP request, system connects to available rep/MSL within 60 seconds post-survey.
- *Gamification/CME*
  - If CME integrated, completion must trigger CME credit record within partner system.
  - Gamification elements must be optional and client-configurable.


### [PROD-276](https://impiricus.atlassian.net/browse/PROD-276) — VC - Short-Term Tooling

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Reporter:** Sam Thomas
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-11-01","end":"2025-11-30"}
- **Project target:** {"start":"2026-01-01","end":"2026-01-31"}
- **Created:** 17/Dec/25 2:50 PM
- **Updated:** 18/Dec/25 5:20 PM

**Description**

#### Overview

This work is focused on short-term internal tooling that can expedite parts of the Virtual Coordinator (VC) build / delivery process while we wait for VC Studio v1 that is scheduled for the end of Q1. 

#### Value for our Business

- Faster, more scalable delivery timelines
- Frees up our developers and technical experts to focus on true development work

#### Value for our Customers

- Faster delivery timelines

#### What’s In Scope

- Internal Impiricus users only
- Tools to automate the creation and testing of Virtual Coordinators

#### What’s Out of Scope

- VC Studio / a polished and robust internal admin portal
- Deployment tooling
- Ability to build VC notifications
- Automation for Slack channels
- Tools to create MLR content
- Removing the need for Twilio flows


### [PROD-169](https://impiricus.atlassian.net/browse/PROD-169) — Referral program

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-07-16","end":"2025-07-16"}
- **Project target:** {"start":"2025-09-15","end":"2025-09-15"}
- **Created:** 05/Sep/25 3:23 PM
- **Updated:** 11/Sep/25 3:00 PM


### [PROD-310](https://impiricus.atlassian.net/browse/PROD-310) — AI Campaign Builder V1 - Pulse campaigns

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-01-28","end":"2026-01-28"}
- **Project target:** {"start":"2026-03-11","end":"2026-03-11"}
- **Created:** 24/Feb/26 2:00 PM
- **Updated:** 24/Apr/26 5:13 PM

**Description**

#### Problems We Are Solving

Campaign setup is a time intensive, manual process today that presents scaling challenges for 3x volume expected YoY in '26.

Goals:

1. Reduce CS work by making campaign set up fast and directly within our system
1. Reduce IM work by eliminating Jira->PR copy/paste for campaign setup

#### Solution Approach

AI-assist CS in entering campaign details directly within our platform. Speeds up campaign setup by

1. Integrate with Asana to pull key campaign details
1. Ingest MLR approved submission doc to pull message contents exactly or choose to add messages manually
1. Allow CS to review & adjust content
1. Automatically creates Jira campaign epic & tickets to support existing crossfunctional workflows
1. Allow IMs to review & finalize campaign implementation after initial setup
1. Allow QA to test against up-to-date source of truth for campaign information

#### Scope

V1 of this project will support pulse-only campaigns but be designed to scale to the full portfolio. Future versions will add support for Spark, Virtual Coordinator, Connect, WebChatbot, etc.

[more info here](https://impiricus.atlassian.net/wiki/spaces/SD/pages/1320615937/AI+Campaign+Builder)


### [PROD-361](https://impiricus.atlassian.net/browse/PROD-361) — Post Launch: AI Campaign Builder Hardening

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-03-16","end":"2026-03-16"}
- **Project target:** {"start":"2026-04-29","end":"2026-04-29"}
- **Created:** 24/Apr/26 4:43 PM
- **Updated:** 24/Apr/26 5:14 PM

**Description**

#### Goals

Add edit / update loop

Test with a live campaign, get feedback, enhance the product for improved usability and future proofing.


### [PROD-76](https://impiricus.atlassian.net/browse/PROD-76) — SureScripts ePrescribing Integration

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-04-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-07-01","end":"2025-09-30"}
- **Created:** 18/Jul/25 1:16 PM
- **Updated:** 11/Sep/25 2:58 PM

**Description**

ya ya


## Ready for delivery (1)

### [PROD-89](https://impiricus.atlassian.net/browse/PROD-89) — New branding - consistent UI/UX across app and website

- **Initiative:** App User Expierience
- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Value drivers:** Customer Engagement
- **Roadmap bucket:** design
- **Project start:** {"start":"2025-10-15","end":"2025-10-15"}
- **Project target:** {"start":"2025-12-15","end":"2025-12-15"}
- **Created:** 04/Aug/25 2:40 PM
- **Updated:** 12/Dec/25 5:54 PM

**Description**

#### *Overview*

Update DocUpdate brand themes from the website into the app experience. Alongside the visual refresh, this epic will also improve core user interface workflows for adding patients, viewing recent patients, and adding and managing pharmacies.

#### *Value for Our Business*

- Aligns the app with DocUpdate’s updated brand identity.
- Creates a more cohesive and professional end-to-end brand experience.
- Strengthens market perception and product quality.
- Enables future marketing and growth initiatives with a consistent visual foundation.

#### *Value for Our Customers*

- A more modern, polished, and intuitive app experience.
- Faster and easier patient and pharmacy management.
- Reduced friction in high-frequency daily workflows.
- Improved trust and confidence in the product through a refined UI.

#### *What’s In Scope*

- Application of new DocUpdate brand themes to the mobile app.
- UI enhancements for:
  - Prescriber
  - Translator
  - Concierge
- Flow enhancements to 
  - Adding patients
  - Viewing and managing recent patients
  - Adding and managing pharmacies
- Updates to colors, typography, and core UI components to match the website.
- UX validation and usability testing for the updated workflows.

#### *What’s Out of Scope*

- Changes to core app logic or backend systems.


## Product Intake (7)

### [PROD-100](https://impiricus.atlassian.net/browse/PROD-100) — Live Chat Support

- **Initiative:** App Retention
- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Value drivers:** Operational Efficiency
- **Roadmap bucket:** Later
- **Project start:** {"start":"2028-01-01","end":"2028-03-31"}
- **Project target:** {"start":"2028-03-15","end":"2028-03-15"}
- **Created:** 04/Aug/25 2:47 PM
- **Updated:** 13/Mar/26 7:56 AM

**Description**

#### *Overview*

Introduce real-time, in-app live chat support that allows users to get immediate assistance for urgent or complex issues—particularly those related to prescribing, account access, or workflow blockers. This feature will provide synchronous communication with support staff, enabling faster resolution than traditional ticket-based systems.

----

#### *Value for our Business*

- Increases user satisfaction and retention by reducing friction during critical moments in the prescribing or documentation workflow.
- Helps prevent user churn by resolving issues before they escalate.
- Strengthens DocUpdate’s brand perception as a responsive, high-touch, clinician-centric platform.
- Provides valuable qualitative insights from live conversations that can inform product improvements and roadmap prioritization.
- Can reduce repeated support tickets by solving problems in real time and capturing context immediately.

----

#### *Value to our Users*

- Allows clinicians to get fast, real-time help during clinical tasks where delays can impact patient care.
- Eliminates the frustration of waiting for email responses or navigating support portals.
- Provides a safety net that builds user confidence when adopting new features or workflows.
- Ensures urgent prescribing issues are addressed quickly, minimizing disruptions to care delivery.

----

#### *What’s in Scope*

- Implementation of a live chat system within the DocUpdate mobile app (and eventually web app).
- Chat UI for initiating conversations, sending/receiving messages, and reviewing chat history.
- Integration with a third-party chat provider (e.g., Intercom, Zendesk, Twilio Conversations) *or* building lightweight internal tooling.
- Routing logic to ensure messages reach the appropriate support staff.
- Support team console or integration with an existing support dashboard.
- Tracking and analytics to monitor response times, chat volume, and user satisfaction.


### [PROD-166](https://impiricus.atlassian.net/browse/PROD-166) — A/B testing capabilities in app

- **Initiative:** App Retention
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-06-15","end":"2026-06-15"}
- **Created:** 05/Sep/25 3:19 PM
- **Updated:** 13/Apr/26 8:44 AM

**Description**

#### *Overview*

Implement an A/B testing framework within DocUpdate that allows the product team to roll out different versions of new features to selected user segments, monitor engagement and qualitative feedback, and use data-driven insights to decide which version should be rolled out to the full user base. This framework will likely leverage Firebase (or a similar tool) for experiment configuration, segmentation, and analytics.

#### *Value for our Business*

- Ensures product decisions are backed by real user behavior rather than assumptions or anecdotal feedback.
- Reduces risk associated with shipping new features broadly by validating concepts with controlled groups.
- Increases the likelihood that launched features drive engagement, retention, and positive sentiment.
- Enables faster iteration loops and more confident roadmap planning.
- Builds a scalable experimentation culture that supports long-term product innovation.

#### *Value to our Users*

- Users receive higher-quality, more thoughtful features because only the best-performing versions reach full rollout.
- Reduces exposure to unproven or less-effective features, preserving trust and minimizing disruption to workflows.
- Ultimately results in a product that better aligns with real-world clinician needs.

#### *What’s in Scope*

- Implementation of an experimentation framework (likely via Firebase Remote Config, Firebase A/B Testing, or similar services).
- Ability to target user cohorts for different variations of features or UI changes.
- Mechanisms for tracking engagement, usage metrics, and feedback tied to experimental groups.
- Developer workflows for setting up, launching, monitoring, and ending experiments.
- Backend and mobile app updates required to support feature flagging and version control.
- Dashboards or accessible reporting to evaluate experiment performance.

#### *What’s Out of Scope*

- Developing a completely custom A/B testing engine from scratch.
- Full-scale personalization or ML-based optimization beyond experiment-level rollout choices.
- Redesigning existing features solely for the purpose of experimentation.
- Complex segmentation models or predictive analytics that extend beyond initial testing needs.


### [PROD-168](https://impiricus.atlassian.net/browse/PROD-168) — Configureable system messages

- **Initiative:** App User Expierience
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Platform Integrity
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 05/Sep/25 3:23 PM
- **Updated:** 10/Mar/26 8:31 PM

**Description**

### Configurable In-App Messaging & Workflow Alert System

#### Overview

Build a configurable in-app messaging and alert system that allows the product team to trigger context-specific informational pages, feature alerts, and workflow-based notifications.

The system will surface relevant updates such as:

- New feature launches
- Functionality changes
- Workflow-based alerts triggered by user behavior

Alerts may be triggered by favorable or unfavorable user activity to guide users toward high-value actions or re-engage them when friction or drop-off is detected.

Messages will appear only when contextually appropriate, ensuring communication is timely, targeted, and non-intrusive while driving adoption and deeper engagement across the app.

----

#### Value for Our Business

*Improves product communication*
Provides a flexible, centralized system to inform users about important updates, feature releases, and system changes.

*Drives feature adoption and engagement*
Enables proactive alerts for newly launched features and underutilized functionality to increase activation and usage.

*Supports product-led growth*
Uses workflow-based triggers to guide users toward high-value actions when favorable behavior is detected (e.g., successful completion of a key workflow).

*Reduces churn and friction*
Triggers contextual alerts when unfavorable behavior occurs (e.g., abandonment, repeated errors, inactivity), helping redirect users before disengagement.

*Reduces reliance on external channels*
Minimizes dependency on email, or SMS and enhances push notifications.

*Decreases support burden*
Proactively addresses confusion, errors, or known issues within the workflow to reduce support tickets.

----

#### Value to Our Users

*Timely, relevant communication*
Users receive updates and guidance at the moment they need it — not after the fact.

*Clear visibility into new features*
Ensures users are aware of new tools and improvements without requiring them to discover features independently.

*Guided workflow support*
Provides helpful prompts when users encounter friction or when an opportunity exists to enhance their workflow.

*Non-disruptive experience*
Alerts are contextual and behavior-based, avoiding unnecessary interruptions.

----

#### What’s in Scope

- A configurable in-app messaging and alert system
- Ability to trigger:
  - Informational modals
  - Feature announcements
  - Workflow-based alerts
- Behavioral trigger logic, including:
  - Show once
  - Recurring under defined conditions
  - Triggered by favorable activity (e.g., completion of key workflows)
  - Triggered by unfavorable activity (e.g., abandonment, repeated failure states)
  - Dismissal rules and cooldown logic
- Segmentation logic (basic role-based or usage-based targeting)
- Basic analytics tracking:
  - Views
  - Dismissals
  - Click-throughs
  - Conversion after alert
- Admin/configuration layer for Product/Support to manage:
  - Message content
  - Trigger conditions
  - Display rules
  - Priority logic

----

#### What’s Out of Scope

- Push notifications, email systems, or multi-channel messaging beyond in-app experiences
- Advanced personalization powered by AI (future enhancement)
- Full marketing automation or lifecycle campaign tooling
- A/B experimentation framework (future enhancement)


### [PROD-175](https://impiricus.atlassian.net/browse/PROD-175) — Landing screen/modal for push notifications/releases (Deep Link)

- **Initiative:** App User Expierience
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Customer Engagement
- **Created:** 05/Sep/25 3:30 PM
- **Updated:** 18/Feb/26 11:19 AM

**Description**

#### *Overview*

This initiative introduces a configurable in-app landing screen/modal that will allow us to inform users about new features and updates after each release. The experience will be built using a flexible template system, standardized headers, subheaders, and layout components with the ability to swap in different images or content depending on the release.

#### *What’s In Scope*

- Development of a configurable in-app landing page for release updates.
- Configuration options to update content without code changes (DB update without an app deployment required)
- Event-based triggering of landing screens that surfaces the on login after certain events or when a user clicks on a push notification. 

#### *What’s Out of Scope*

- A full in-app content management system beyond templated configuration.
- Multi-step onboarding or tutorial flows.
- Deep personalization or segmentation of which users see which updates.

#### *Value for Our Business*

- Creates a consistent and scalable communication channel for product updates.
- Reduces engineering lift for release communications by using reusable templates.
- Increases feature adoption by ensuring users are aware of new capabilities.
- Provides Marketing and Product with a reliable vehicle for announcements.

#### *Value for Our Customers*

- Clear visibility into new features that improve their workflow.
- A more guided and informative post-release experience.
- Reduced confusion around changes or additions to the app.
- A consistent, high-quality interface for receiving important updates.


### [PROD-176](https://impiricus.atlassian.net/browse/PROD-176) — Activating inactives and driving cross-sell

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 05/Sep/25 3:35 PM
- **Updated:** 20/Feb/26 8:15 AM

**Description**

#### Overview

Implementation of initiatives to increase DocU user engagement with Concierge. These combined efforts aim to boost awareness and adoption of Concierge among active users. 

#### Value for our Business

- Increase HCP retention on the app
- More users in Concierge should result in higher engagement rates for Ascend partners listed on the app

#### Value for our Customers

- Opportunity to discover our additional free tools that they may not be aware of 
- Increased frequency of sample deliveries due to reminders to request additional items

#### What’s In Scope

- *In-app:*
  - Rotating the default module app when app is launched (need Adam’s input on user impact here)
  - Prompt in concierge UI with rotating suggestions for custom concierge questions
  - Modal/toast on close in other services recommending concierge usage
- *Outside of App*:
  - e-mail and/or push notifications to past concierge users without usage in past 30 days (any concierge function)
  - E-mail and/or push notification to past concierge users if no usage of *_all_* modules in last 30 days (e.g, if sample request, message re: custom)
- Onboarding stream:
  - Include concierge in weekly cadence of welcome emails

#### What’s Out of Scope

- SMS to drive concierge usage (to avoid user opt-out)


### [PROD-167](https://impiricus.atlassian.net/browse/PROD-167) — Persona - legacy user migration 

- **Initiative:** Persona
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Innovation, Platform Integrity
- **Project start:** {"start":"2025-10-01","end":"2025-10-31"}
- **Project target:** {"start":"2025-11-15","end":"2025-11-15"}
- **Created:** 05/Sep/25 3:20 PM
- **Updated:** 11/Dec/25 3:21 PM

**Description**

#### *Overview*

Following the launch of ePrescribing, all legacy (non-Persona verified) users will be required to complete Persona identity verification in order to continue prescribing. This initiative introduces an in-app verification prompt for affected users and enforces mandatory completion prior to allowing further prescribing activity.

#### *Value for Our Business*

- Supports bringing 100 percent of prescribing users into compliance with identity verification requirements.
- Reduces regulatory, fraud, and audit risk.
- Aligns all prescribing workflows under a single, standardized verification process.
- Simplifies downstream support, compliance, and certification efforts.
- Strengthens DocUpdate’s security and trust posture with partners.

#### *Value for Our Customers*

- Take verification process from days to seconds
- Provides a clear, guided path to complete identity verification.
- Increases overall platform trust and security.
- Protects against unauthorized prescribing activity.

#### *What’s In Scope*

- In-app prompt for legacy users to initiate Persona verification.
- November 25th cutoff for mandatory verification.
- UX flows for verification success, failure, and retry states.

#### *What’s Out of Scope*

- Changes to Persona’s underlying identity verification process.


### [PROD-307](https://impiricus.atlassian.net/browse/PROD-307) — Encrypt PHI fields in DocUpdate DB

- **Initiative:** Security and Compliance
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** design
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 19/Feb/26 3:58 PM
- **Updated:** 03/Mar/26 1:40 PM

**Description**

##### Overview

Introduce an additional application-layer protection mechanism for Protected Health Information (PHI) beyond current infrastructure-level encryption. The goal is to ensure that even if database credentials are compromised, sensitive patient identifiers cannot be easily read or exfiltrated.

The final technical approach (e.g., tokenization, blind indexing, vault architecture, or hybrid model) will be determined during discovery to balance security, performance, and usability across search-heavy workflows.

##### Value for Our Business

- Reduces breach blast radius in credential compromise scenarios
- Strengthens HIPAA and audit posture
- Aligns with enterprise healthcare security expectations
- Improves confidence during external audits and partner diligence
- Protects brand and reduces financial/legal exposure

##### Value for Our Customers

- Stronger protection of patient data
- Maintains performance for patient search, filtering, and call center workflows
- Builds trust in DocUpdate as a secure clinical platform
- Enables scalable, secure data handling as user base grows

##### What’s In Scope

- Audit and mapping of all PHI fields in the database
- Security architecture discovery (tokenization, blind index, vault, or hybrid)
- Selection of approach that doesn’t have significant impact on app performance and search capabilities
- Application updates to handle protected fields appropriately
- Phased rollout plan to minimize operational disruption

##### What’s Out of Scope

- Full database rewrite
- Performance initiatives not directly tied to PHI protection
- Non-PHI data security enhancements


## Parking lot (159)

### [PROD-119](https://impiricus.atlassian.net/browse/PROD-119) — Strategic Agent Field Force

- **Initiative:** Agentic Field Force Platform
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Innovation, Operational Efficiency
- **Project start:** {"start":"2026-04-16","end":"2026-04-16"}
- **Project target:** {"start":"2026-10-15","end":"2026-10-15"}
- **Created:** 20/Aug/25 10:20 AM
- **Updated:** 02/Mar/26 10:37 AM

**Description**

#### Overview

Overall goal is to develop Impiricus 2.0, or the Ascend Agentic Field Force Deployer. The platform could be used to aggregate HCP preferences across multiple channels and then deploy the right message via the right channel at the right time.

#### Value for our Business

- Ascend as a business objective is driving deeper HCP engagement across multi-channels.
- Currently, we can support some targeted messaging to the right HCP on the right channel, but it is fairly manual.
- Secondly, we have disparate systems (Pulse Runner, VC Builder, Rep Connect) and need to think if a platform approach will provide greater enterprise value.

#### Value for our Customers

TBD

#### What’s In Scope

- NEEDS FURTHER SCOPING

This was brainstormed at the Aug 2024 Product Summit, notes below and definitely needs revisiting, rescoping.

Slide deck here w links to replits

[https://docs.google.com/presentation/d/1ZkccnTW0ut-UjRI6V2cmT3_DU8-w1SoC2U5OlkOQaBw/edit?slide=id.g33d5dd410e6_4_0#slide=id.g33d5dd410e6_4_0](https://docs.google.com/presentation/d/1ZkccnTW0ut-UjRI6V2cmT3_DU8-w1SoC2U5OlkOQaBw/edit?slide=id.g33d5dd410e6_4_0#slide=id.g33d5dd410e6_4_0|smart-link) 

This platform could do 4 main things

- Input data for Strategy/ Planning
  - Target Lists
  - IQVIA data
  - Impiricus db data
- Deploy across multiple channels
  - SMS
  - Voice
  - Docupdate
  - Email/Banner
- Provide Communications/ Integrations via
  - Rep Connect
  - VC
  - Integrations 
*** Samples, Hub Services, Prior Auth
  - Indep Activities
- Provide Real Time Analytics & Reporting

#### What’s Out of Scope

- TBD


### [PROD-248](https://impiricus.atlassian.net/browse/PROD-248) — AI Voice Survey in Impiricus 2.0 AFFD Platform

- **Initiative:** Agentic Field Force Platform
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2027-06-01","end":"2027-06-30"}
- **Created:** 09/Dec/25 5:04 PM
- **Updated:** 11/Dec/25 3:46 PM

**Description**

#### Overview

This work enhances our offering for AI-driven voice surveys, which we have thus far used for independent initiatives to engage with HCPs and collect insights that can be used to help inform our company and/or product strategies. 

Currently, we offer inbound and outbound call options where the HCP gets connected with the AI agent via phone and is guided through a pre-built survey flow. 

This work brings our AI Voice surveys properly onto the Impiricus platform and provides better tooling to generate and expedite voice survey initiatives. 

#### Value for our Business

This expands our suite of offerings and opens up another channel in which we can engage HCPs, which will enhance our standing in the market and generate additional revenue streams. 

#### Value for our Customers

Provides additional ways in which HCPs can be engaged, adding to the channel options that promote two-way HCP interactions. For HCPs, this offers a more interactive method of engagement and is available for users who prefer voice formats vs. written via web chatbot or SMS. 

#### What’s In Scope

- A branded Impiricus portal to manage AI voice survey projects
- Tools to generate multiple AI voice survey phone numbers / workflows
- Inbound and outbound call capabilities for multiple brands / survey efforts at a time
- Tools for call logging / tracking
- Reports to parse voice responses and highlight common themes / metrics

#### What’s Out of Scope

- TBD


### [PROD-172](https://impiricus.atlassian.net/browse/PROD-172) — In-app session replays - Mixpanel

- **Initiative:** App Retention
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-06-15","end":"2026-06-15"}
- **Created:** 05/Sep/25 3:26 PM
- **Updated:** 13/Apr/26 8:44 AM

**Description**

#### *Overview*

This initiative enables advanced user session replay and deeper behavioral analytics within the DocUpdate app. By capturing real user interactions, errors, and performance data, we will gain greater visibility into real-world usage patterns and be able to diagnose issues faster and with higher confidence. 

#### *Value for Our Business*

- Dramatically improves debugging speed and accuracy.
- Reduces time to resolution for user-reported issues.
- Enhances product decision-making with real behavioral insights.
- Strengthens QA and release confidence.
- Creates a scalable foundation for performance monitoring and UX optimization.

#### *Value for Our Customers*

- Faster resolution of bugs and usability issues.
- More stable and reliable app experience.
- Fewer repeated support requests.
- Improved overall usability through data-driven UX refinement.

#### *What’s In Scope*

- Implement Session Replay for modules outside of Prescriber 
  - This is due to us not yet having a BAA with Mixpanel
- Capture of frontend errors, crashes, and performance metrics.
- User session tagging for support and troubleshooting workflows.

#### *What’s Out of Scope*

- Replacement of foundational product analytics used for KPI reporting.
- Long-term data warehousing or BI reporting within the session replay tool.
- Advanced behavioral experimentation or A/B testing frameworks.
- Manual session recording outside of automated capture.
- Implementation within Prescriber (future iteration)


### [PROD-209](https://impiricus.atlassian.net/browse/PROD-209) — Firebase/Google Ads integration

- **Initiative:** App Retention
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Business Growth, Operational Efficiency
- **Project start:** {"start":"2026-01-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 10/Oct/25 3:22 PM
- **Updated:** 17/Feb/26 4:25 PM

**Description**

#### *Overview*

Marketing is requesting product support to scale DocUpdate’s presence within the Google Ads network. To effectively measure performance and return on ad spend, we will enable mobile analytics tracking through a Firebase integration. This will allow us to track app installs, downstream user signups, and accurately calculate customer acquisition cost (CAC tied to Google Ads).

#### *Value for Our Business*

- Enables accurate measurement of Google Ads performance.
- Establishes reliable CAC reporting for Google Ads network for paid acquisition.
- Improves confidence in marketing spend and ROI.
- Creates a scalable foundation for future paid growth channels.
- Aligns product, marketing, and leadership on a shared source of attribution data.

#### *Value for Our Customers*

- Indirect benefit through more targeted and effective user acquisition.
- Improved onboarding experiences driven by better-informed growth strategies.
- Faster iteration on acquisition flows based on real usage data.

#### *What’s In Scope*

- Firebase SDK integration into the DocUpdate mobile app.
- Enablement of Google Ads attribution for:
  - App installs
  - User signups
- Mapping conversion events to support CAC and funnel reporting.
- Collaboration with Marketing to define and confirm core acquisition metrics.

#### *What’s Out of Scope*

- Management or optimization of Google Ads campaigns themselves.


### [PROD-218](https://impiricus.atlassian.net/browse/PROD-218) — Hubspot integration

- **Initiative:** App Retention
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-01-05","end":"2026-01-05"}
- **Project target:** {"start":"2026-02-16","end":"2026-02-16"}
- **Created:** 06/Nov/25 6:38 AM
- **Updated:** 11/Dec/25 4:49 PM

**Description**

#### *Overview*

This initiative introduces an integration with HubSpot to enable targeted outreach and user engagement based on real-time journeys and behaviors within the DocUpdate app. HubSpot will receive a series of triggered events, similar to our Mixpanel integration, allowing campaigns and automations to fire based on in-app actions.

#### *Value for Our Business*

- Enables real-time, behavior-based marketing and engagement.
- Helps improve conversion across onboarding, activation, and retention flows.
- Reduces reliance on manual campaign execution.
- Aligns marketing automation strategy with in-app behavioral data.
- Creates a scalable foundation for marketing.

#### *Value for Our Customers*

- More relevant, timely, and personalized communications.
- Better onboarding and feature awareness through guided engagement.
- Improved overall product experience through contextual messaging.

#### *What’s In Scope*

- Real-time event-based integration between DocUpdate and HubSpot.
- Definition and mapping of core in-app events for marketing automation (aligned with Mixpanel where applicable).
- Triggered workflows for key user lifecycle moments (e.g., signup, first RX, inactivity, feature discovery).
- Testing and validation of real-time triggers and message delivery.
- Collaboration with Marketing to define segmentation and automation use cases.

#### *What’s Out of Scope*

- Full CRM migration to HubSpot.
- Marketing campaign creative development.


### [PROD-204](https://impiricus.atlassian.net/browse/PROD-204) — Add support for a web app version of DocUpdate to support prior authorization

- **Initiative:** App User Expierience
- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Value drivers:** Business Growth, Customer Engagement
- **Roadmap bucket:** Later
- **Project start:** {"start":"2026-10-01","end":"2026-12-31"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 01/Oct/25 4:57 PM
- **Updated:** 13/Apr/26 5:07 PM

**Description**

#### *Overview*

Introduce support for a web-based version of DocUpdate, as well as improved compatibility for larger non-mobile screens such as tablets. This effort focuses on extending our existing mobile experience to additional form factors without adding new features.

#### *Value for our Business*

- Expands DocUpdate’s addressable market by supporting clinicians who prefer desktop or tablet-based workflows.
- Strengthens adoption among users running telehealth or virtual care operations who rely on DocUpdate as their primary prescribing and patient-management tool.
- Positions DocUpdate as a more versatile, professional-grade clinical platform, increasing retention and enabling future enterprise or multi-modal product offerings.
- Required for future roadmap items such as proxy users (staff) to support PA assistance

#### *Value to our Users*

- Allows clinicians who prefer larger screens to work more comfortably and efficiently.
- Improves usability for telehealth providers who currently rely on mobile despite workflows better suited to web/tablet experiences.
- Enables easier multitasking, documentation, and prescribing by providing more screen real estate.
- Allows delegation of tasks from the validated HCP using the mobile app to staff using a tablet or desktop. 

#### *What’s in Scope*

- Creation of a new web application version of DocUpdate.
- Support for tablet and larger-screen layouts using responsive UI patterns.
- New codebase that mirrors the existing mobile app’s functionality.
- Ensuring feature parity with the current app (no new features).
- Ongoing maintenance and updates to keep the web app aligned with mobile.

#### *What’s out of Scope*

- Any new features or workflows beyond what currently exists in the mobile app.
- Redesign or reimagining of core DocUpdate features.
- Server-side architectural changes not required to enable the web experience.
- Enhancements specifically targeting desktop-only or advanced EMR-style functionality.


### [PROD-309](https://impiricus.atlassian.net/browse/PROD-309) — Push messaging

- **Initiative:** App User Expierience
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-06-30"}
- **Created:** 20/Feb/26 8:41 AM
- **Updated:** 10/Mar/26 8:23 PM

**Description**

#### Overview

Development of a system to send push messages to DocUpdate users

#### Value for our Business

- Push messaging will allow us to provide information to HCPs which will ultimately drive desired behaviors such as:
  - Sample ordering
  - More frequent engagement with the DocUpdate app
  - Engagement with more DocUpdate feature modules

#### Value for our Customers

- Users will be made aware of app features most likely to benefit them

#### What’s In Scope

- System to send push messages to users based on:
  - HCP presence on targeted list of NPIs
  - Specialty
  - Previous usage of app or specific feature modules
  - Trigger from HubSpot
  - Writing of specific NDC
- Confirmation of delivery to a specific user via MixPanel

#### What’s Out of Scope

- Integration or cadence between push messaging and other messaging such as e-mail


### [PROD-125](https://impiricus.atlassian.net/browse/PROD-125) — Modular Integrations - Prior Auth & Hub Services Beta

- **Initiative:** Ascend Integrations
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 20/Aug/25 10:24 AM
- **Updated:** 02/Mar/26 10:37 AM

**Description**

#### Overview

The strategy is similar to Samples integrations, 

1. Integrating with Prior Auth and Hub Services systems would greatly improve the overall HCP experience
   1. reducing friction by offering an SMS enabled workstream 
   1. Prior Auth systems are utilized by HCPs and help get patients prior approval from payers for the drug they need
   1. Hub Services refers to a broader suite of services that pharma can offer to HCPs and patients to improve HCP and patient access and awareness about the drug, while also helping remove barriers to the drug
##### Prior Auth and Patient Support are examples of Hub Services that could be offered
1. We currently receive HCP responses that there are coverage and access issues (that they need help with Prior Auth or other patient hub services that they are struggling with)
1. Goal is to identify strategy and/ or Ascend clients to engage with betas for these integrations

#### Value for our Business

- Huge value for Ascend
  - Drives HCP engagement via whatever Ascend channel they are interacting with
  - Allows us to provide more than just resource links to HCPs
*** We are helping them solve workflow issues 
*** This will make us hugely valuable and sticky
*** Also within pharma, we’re helping solve multiple problems for multiple departments, all through Ascend platform
**** attacking marketing strategy with resource links
**** driving sample volume via integration
**** helping market access teams by unlocking access and coverage issues
**** connecting HCPs to humans
***** Reps
***** MSLs
***** FRM

#### Value for our Customers

similar to above

#### What’s In Scope

- needs scoping
  - we need to identify the right Ascend client who we can work on an integration with, then define the integration
  - things to scope
*** if we’re dealing with PA, are we starting to deal with patient data? 

#### What’s Out of Scope

- TBD

----

*Update as of 10/31/25:*

- Rep Connect launched with Auvelity on 10/8/25
  - 2 of 32 HCP-Rep convos were HCP initiated questions to rep about prior auth issues
  - we want to scope a prior auth integration and workflow through CoverMyMeds for Axsome in Q4
*** no delivery timing promised to Axsome yet, just scoping
  - no update on product side on Hub Service

----

####


### [PROD-127](https://impiricus.atlassian.net/browse/PROD-127) — Modular Integrations - Patient Support Betas

- **Initiative:** Ascend Integrations
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2027-12-01","end":"2027-12-31"}
- **Created:** 20/Aug/25 10:25 AM
- **Updated:** 10/Dec/25 5:23 PM

**Description**

#### Overview

This would be an integration with pharma clients who offer patient support programs. Patient support programs, often from drug makers, help patients overcome barriers to starting and sticking with treatments by offering financial aid (like free medicine), insurance navigation, education about conditions, training for devices, and ongoing support via case managers or helpdesks, all aiming to improve health outcomes and medication adherence. They address complexities like insurance gaps and costs, ensuring patients get necessary therapies, especially specialty or complex medications. 

- Key Components of Patient Support Services:
Financial Assistance: Patient Assistance Programs (PAPs) provide free or low-cost medication for qualifying low-income or uninsured/underinsured patients.
- Insurance Navigation: Helping patients understand and manage complex insurance plans, including public (Medicare/Medicaid) and private coverage, and finding alternative funding.
- Patient Education: Resources and counseling to help patients learn about their disease, treatment, and adherence strategies.
- Training & Logistics: Hands-on training for medical devices (injections, pumps) and coordinating drug delivery.
- Personalized Support: Assigning case managers for one-on-one help or offering 24/7 helpdesks.
- Care Coordination: Connecting patients with other specialists like nutritionists or psychologists. 

#### Value for our Business

- Offering this as an integrated service is a natural progression from the types of resources we commonly send today from the HCP brand website
- This fits nicely into the Ascend platform engagement, where we can then offer 2-way engagement, and provide a deeper level of engagement to HCPs who truly need support navigating the complexities of multiple brands

#### Value for our Customers

- similar value to us; if we meet HCPs in SMS with easier to use workflows or ways to connect to pharma humans that can help them solve their patient issues in real-time, then we’re truly adding value and connecting resources to HCPs
- this will drive stickiness to our Ascend platform

#### What’s In Scope

- needs scoping - to be defined

#### What’s Out of Scope

- TBD

----

*Update as of 10/31/25:*

- No movement from product side
- Continue to monitor Ascend client pipeline and market for need

####


### [PROD-270](https://impiricus.atlassian.net/browse/PROD-270) — Modular Integrations - Other

- **Initiative:** Ascend Integrations
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2028-06-01","end":"2028-06-30"}
- **Created:** 10/Dec/25 4:06 PM
- **Updated:** 10/Dec/25 4:07 PM

**Description**

#### Overview

This is a placeholder for any other modular integrations that we decide to pursue to support the Ascend platform and driving 2 way HCP engagement.

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-122](https://impiricus.atlassian.net/browse/PROD-122) — Channels - DocUpdate App Notifications

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement, Network Health
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 20/Aug/25 10:22 AM
- **Updated:** 02/Mar/26 10:36 AM

**Description**

#### Overview

Goal here is to connect and leverage existing DocUpdate brand and app to deploy Ascend related content to HCPs. DocUpdate as a channel is leveraging DocUpdate as a venue to deliver content instead of SMS or email etc.

- DocUpdate could push notifications (in lieu of, in addition to SMS, email, etc) of relevant convo
- This could serve as a place to serve non branded content
- Links to conferences, zoom panels, events
- Display ascend partners as top providers for HCP access to brand samples or resources
- Control SMS bloat
  - HCPs may not want to save and find 30 brand Virtual Coordinators in their SMS

#### Value for our Business

- Drive multichannel engagement - grow DocUpdate via natural need from HCPs on pharma side getting inundated with SMS messaging and wanting a centralized place to receive notifications

#### Value for our Customers

- Could be an extra channel where we we drive HCP brand engagement on behalf of Pharma partners

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD

----

*Update as of 11/3/25:*

- No additional work started on this
- Use case still valid


### [PROD-123](https://impiricus.atlassian.net/browse/PROD-123) — Channels - VC Voice Agent

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Created:** 20/Aug/25 10:23 AM
- **Updated:** 09/Dec/25 2:33 PM

**Description**

*Update as of 10/31/25:*

- no further movement on Prod side

----

In addition to the chat component of Virtual Coordinator, explore the possibility of additional channel where an HCP could interact with voice and ask questions, get resources help via phone. Could tie into following up with SMS/ email with resources.


### [PROD-132](https://impiricus.atlassian.net/browse/PROD-132) — Channels - Outbound Voice Driving to DocUpdate Initiatives

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Created:** 20/Aug/25 10:50 AM
- **Updated:** 09/Dec/25 3:24 PM

**Description**

- This is like Pulse but via AI voice calls. Lots of legal and implementation questions here.


### [PROD-159](https://impiricus.atlassian.net/browse/PROD-159) — Create Multi Channel Roadmap

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Project start:** {"start":"2025-08-16","end":"2025-08-16"}
- **Project target:** {"start":"2025-07-01","end":"2025-09-30"}
- **Created:** 27/Aug/25 11:24 AM
- **Updated:** 15/Sep/25 1:13 PM

**Description**

Explore additional opportunities beyond SMS, Pulse & Spark today

Current ideas

- Replace Ostro Webchatbots for Axsome
- Email
- Voice AI Surveys
- Website/Banner Ads


### [PROD-199](https://impiricus.atlassian.net/browse/PROD-199) — Channels - Email in Platform

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Low
- **Reporter:** Brian Ongioni
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2025-11-01","end":"2025-11-30"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 23/Sep/25 10:06 AM
- **Updated:** 10/Dec/25 4:32 PM

**Description**

#### Overview

In addition to current outreach methods, expand Ascend to include email as a channel for reaching and engaging the HCP network. This would enable delivery of tailored resources, reminders, and follow-up communications directly to an HCP’s inbox. Email could complement other channels (e.g., SMS, DocUpdate, Web Chatbot, or VC Chat/Voice Agent) and support sequencing campaigns that provide resources, answer common questions, and drive continued engagement with Ascend programs.

#### Value for our Business

- Driving multichannel opportunities will help us build the Ascend platform, whereby we are providing more channels to send the right HCP the right message, via the right channel, at the right time

#### Value for our Customers

- Adds additional channel offering for Ascend clients
- Clients are likely comfortable and/ or already have some experience with email

#### What’s In Scope

- we want email to be used in a smart way
  - If we pursue email, then we need to fully scope out email, similar to any other channel (SMS)
*** who is our email vendor
*** how does it plug into existing systems (i.e. Pulse Runner today)
*** how does the content look
*** what offerings do we provide via email
*** how do we plug in email into our multi-channel agentic deployer
**** when would they receive email vs sms

#### What’s Out of Scope

- We do not plan to do email like other HCP marketing campaigns today - aka BLAST SPAM

----

*Update as of 10/31/25:*

- in Q4, we are doing an email beta test via Hubspot for Ascend client Pemazyre

----

####


### [PROD-238](https://impiricus.atlassian.net/browse/PROD-238) — Channels - DocUpdate Ascend Content Library

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Network Health
- **Project start:** {"start":"2026-10-01","end":"2026-10-31"}
- **Project target:** {"start":"2027-04-01","end":"2027-04-30"}
- **Created:** 09/Dec/25 2:29 PM
- **Updated:** 11/Dec/25 3:46 PM

**Description**

#### Overview

- Idea of a "library" to access past convos/history and content and a place for them to initiate from docUpdate vs. SMS

#### Value for our Business

- Drive multichannel engagement - grow DocUpdate via natural need from HCPs on pharma side getting inundated with SMS messaging and wanting a centralized place to receive notifications

#### Value for our Customers

- Solve HCP SMS bloat
- Could be an extra channel where we we drive HCP brand engagement on behalf of Pharma partners

#### What’s In Scope

- needs scoping

#### What’s Out of Scope

- TBD


### [PROD-239](https://impiricus.atlassian.net/browse/PROD-239) — Channels - 3rd Party Partners (High Intent Endemic Pubs)

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation, Network Health
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 09/Dec/25 3:21 PM
- **Updated:** 02/Mar/26 10:37 AM

**Description**

#### Overview

Starting early discussions to talk to partners such Doximity, OpenEvidence to bring DocUpdate Concierge as a channel displayed on 3rd party websites and then integrating this to provide other channel partners into reach as Ascend.

#### Value for our Business

- Enhances multi channel opportunities

#### Value for our Customers

- More channels that clients get with Ascend boosts engagement and Ascend metrics for the client

#### What’s In Scope

- TBD - needs scoping

#### What’s Out of Scope

- TBD


### [PROD-240](https://impiricus.atlassian.net/browse/PROD-240) — Channels - EHR Partner Integration

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation, Network Health
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2027-09-01","end":"2027-09-30"}
- **Created:** 09/Dec/25 3:22 PM
- **Updated:** 10/Dec/25 4:34 PM

**Description**

#### Overview

HCP’s are in their EHRs everyday. EHR is a common HCP marketing channel today. So EHR as a channel could provide a place for us to display content to HCPs. We are still scoping what the overall EHR content would be:

- The content could be branded or non-branded
- Could display QR code to VC
  - or QR code to order samples

#### Value for our Business

- Driving multichannel opportunities will help us build the Ascend platform, whereby we are providing more channels to send the right HCP the right message, via the right channel, at the right time

#### Value for our Customers

- Adds additional channel offering for Ascend clients
- Clients are likely comfortable and/ or already have some experience with EHR content

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-329](https://impiricus.atlassian.net/browse/PROD-329) — Ascend as Source of Record

- **Initiative:** Ascend Multi-Channel Roadmap
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Created:** 26/Feb/26 9:52 AM
- **Updated:** 26/Feb/26 9:54 AM

**Description**

#### Overview

Rep Connect 2.0 – System of Record for Rep Conversations

As discussed at the commercial F2F, we will be pushing "always on" communication, samples, and surveys and de-emphasizing Rep Connect from a sales perspective in the immediate term.

That being said, we have learned a ton about what Rep Connect 2.0 will likely be: a compliant, enterprise-grade system of record for HCP communication

Strategic Positioning: The current pharma landscape requires a focus on rep enablement and compliance — not rep replacement.

Leaders are incentivized to strengthen and support field forces, not remove them. Our narrative should consistently reinforce that we empower reps, enhance compliant communication, and increase their effectiveness — serving as the compliant pipes and intelligence layer that makes them stronger.

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-325](https://impiricus.atlassian.net/browse/PROD-325) — Channels - Intelligent Media Dashboard 

- **Initiative:** Channels - Intelligent Media
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 26/Feb/26 8:55 AM
- **Updated:** 26/Feb/26 8:58 AM

**Description**

#### Overview

- Impiricus adds Intelligent Media QR codes to brand media (website, direct mail, conferences, any marketing materials)
- Then we can leverage that data of HCP Inbound via specific channel
- Compile aggregate data and sell as insights back to media/ pharma

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-171](https://impiricus.atlassian.net/browse/PROD-171) — Prior authorizations - Integrate with a partner

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-11-01","end":"2026-11-30"}
- **Project target:** {"start":"2027-01-01","end":"2027-03-31"}
- **Created:** 05/Sep/25 3:26 PM
- **Updated:** 14/Apr/26 4:10 PM

**Description**

#### *Overview*

Implement full prior authorization (PA/ePA) support within DocUpdate by integrating with third-party partners who specialize in electronic prior authorizations. This includes partnering with one or more partners (e.g., Tandem, Squad Health) for ePA processing.  The goal is to streamline the PA experience without introducing unnecessary new prescribing features.

#### *Value for our Business*

- Positions DocUpdate as one of the only streamlined PA solutions available to clinicians, differentiating us from competitors.
- Increases user acquisition by solving one of the most widely acknowledged pain points in clinical practice.
- Strengthens brand recognition by tackling a problem doctors frequently complain about.
- Enhances long-term stickiness for users who begin relying on DocUpdate as their primary prescribing and administrative tool.

#### *Value to our Users*

- Eliminates a major barrier in the prescribing workflow by automating and simplifying prior authorization submissions.
- Reduces administrative burden and time spent navigating payer portals or fax workflows.
- Minimizes disruptions to patient care by speeding up time-to-therapy for medications requiring PAs.
- Offers an integrated, modern solution where none currently exists in a chaotic market.

#### *What’s in Scope*

- Integration with partner(s) to handle electronic prior authorizations.
- UI/UX within DocUpdate to initiate, track, and receive updates on PA status.
- Backend updates needed to transmit prescription and clinical data to partners.
- Maintaining parity with existing prescribing workflows while adding PA functionality.

#### *What’s Out of Scope*

- Building our own in-house PA engine or clinical data exchange system.
- Redesigning or replacing existing prescribing workflows beyond what is necessary for ePA integration.
- Creating payer-specific rules engines or formularies beyond what partners provide.
- Broader billing, insurance verification, or EMR-style administrative features unrelated to PAs.


### [PROD-207](https://impiricus.atlassian.net/browse/PROD-207) — Concierge - Integrate SDK to enable in-app chat

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-01-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-04-15","end":"2026-04-15"}
- **Created:** 08/Oct/25 12:31 PM
- **Updated:** 13/Apr/26 7:05 PM

**Description**

#### *Overview*

This initiative introduces the Zendesk In-App SDK to enable a fully integrated in-app chat experience within DocUpdate. Users will be able to manage multiple conversations in a portal-style interface similar to SMS, receive real-time alerts for new messages, and configure communication preferences for how and when they are contacted.

#### *Value for Our Business*

- Reduces dependence on external SMS tools for support and engagement.
- Reduces the drop-off rate caused by the convo transferring from in-app to SMS
- Ability to build in automation to improve the scaleability of Concierge (automated messages, samples integrations, and in the future will support AI chatbots)
- Improves response time and support efficiency.
- Provides richer engagement and support analytics through Zendesk.
- Creates a scalable foundation for future in-app support and concierge experiences such as samples integrations 

#### *Value for Our Customers*

- Reduced reliance on external text messaging for critical communications (less SMS messages getting marked as spam).
- Seamless, real-time in-app communication with support and concierge teams.
- Ability to manage multiple conversations in one place.
- Notifications for new messages.
- Greater control over how and when they are contacted.

#### *What’s In Scope*

- Integration of the Zendesk In-App SDK into the DocUpdate app.
- New UI for managing multiple concurrent conversations.
- Push and in-app notifications for new messages.
- User communication preferences, including:
  - In-app vs SMS/text
  - Preferred time of day for contact
- Initial storage of preferences in Zendesk, with a later planned migration to BBDB.
- Architecture designed to support future sample and partner messaging integrations.

#### *What’s Out of Scope*

- End to End sample integration workflows 
- Advanced chatbot or AI-driven support automation.


### [PROD-286](https://impiricus.atlassian.net/browse/PROD-286) — Content creation and distribution

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-09-01","end":"2027-09-30"}
- **Project target:** {"start":"2027-10-01","end":"2027-12-31"}
- **Created:** 02/Jan/26 12:06 PM
- **Updated:** 13/Mar/26 7:56 AM

**Description**

#### Overview

Sourcing of content for distribution to our users to drive engagement and provide value. Content will initially be distributed via a newsletter to targeted HCPs to drive registration.

#### Value for our Business

- Increases engagement with the platform 
- Increases perception of DocUpdate as an entity with significant value to a HCP
- Targeted content can drive registration, usage and penetration with our targeted high value specialties
- Engaging with clinicians in the context of content creation can create DocUpdate evangelists and adherents
- Potential future monetization of content library

#### Value for our Customers

- Timely, useful content provides actionable information for use in clinical work and practice management

#### What’s In Scope

- Leveraging/licensing of third party content (potentially Practice Update library)
- Securing new content from HCPs (likely from HCP council members)
- Delivery of generated content via newsletters to existing and targeted HCPs

#### What’s Out of Scope

- AI content optimization at the user level
- Delivery of content within the DocUpdate application


### [PROD-289](https://impiricus.atlassian.net/browse/PROD-289) — Providing Concierge service to partner Jiro

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-04-16","end":"2026-04-16"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 02/Jan/26 2:17 PM
- **Updated:** 13/Apr/26 7:06 PM

**Description**

#### Overview

Provide Concierge service to third party partner Jiro

#### Value for our Business

- Increase awareness of our services and enagement with our platform
- Part of a larger partnership which provides us with access to Jiro HCPs
- When concierge HCPs are monetized, Jiro HCPs will also be revenue-generating (with a rev share w/Jiro)

#### Value for our Customers

- Connects HCPs to pharma resources for a broader HCP universe

#### What’s In Scope

- Integration of the Concierge service with the Jiro native and web app
- Impiricus hosted API through which Jiro can access Concierge services
- Initial implementation will be a free text box for all requests (no sections for samples, request-a-rep, etc like Concierge v3)

#### What’s Out of Scope

- Creation of UI for Concierge in Jiro web or native apps
- Provision of Customer Service support for Jiro services via the concierge app
- Direct integration between Jiro and Zendesk


### [PROD-295](https://impiricus.atlassian.net/browse/PROD-295) — Medvantx Samples Integration (Sanofi Toujeo Solostar and Toujeo Max)

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 17/Feb/26 4:33 PM
- **Updated:** 13/Apr/26 12:54 PM

**Description**

#### *Overview*

This initiative allows in-app ordering of samples for the Toujeo brands at Medvantx.

#### *Value for Our Business*

- Allows support of our Ascend business by allowing easier sample ordering for these Ascend contracted brands
- Integration with Medvantx for a major brand provides a negotiating point for integrating with other sampling partners
- Initial implementation with Medvantx is a first step to integration with all Medvantx brands
- Allowing direct ordering of samples in-app reduces staff time required to handle related Concierge requests and makes the Concierge business more scalable. 

#### *Value for Our Customers*

- Allows easier ordering of samples for HCP users
- Provides additional sample orders for Ascend client Sanofi

#### *What’s In Scope*

- Full scope of integration with Medvantx already executed for Ascend (with the sample ordering flow and Sample Request Form all rendered in-app) for Toujeo Solostar and Toujeo Max

#### *What’s Out of Scope*

- Integration with any other Medvantx brand


### [PROD-296](https://impiricus.atlassian.net/browse/PROD-296) — Continuous development of new integrations for sample ordering

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 17/Feb/26 4:53 PM
- **Updated:** 13/Apr/26 12:54 PM

**Description**

#### *Overview*

Integration with sample partners as agreements are reached to allow ordering of samples by DocUpdate HCP users in the application.

#### *Value for Our Business*

- Easier sample ordering makes the DocUpdate app stickier and more useful to HCP users, making them more likely to use the app and remain opted in for SMS messaging
- Allowing direct ordering of samples in-app reduces staff time required to handle related Concierge requests and makes the Concierge business more scalable. 
- As more brands and sample partners are integrated, DocUpdate becomes the leading aggregator of pharmaceutical sample supply and demand

#### *Value for Our Customers*

- Allows easier ordering of samples for HCP users
- Provides additional sample orders for pharmaceutical brands who choose to contract with us

#### *What’s In Scope*

- Integration with new sample partners as contracted
- Scope of each TBD as agreements are reached

#### *What’s Out of Scope*

- TBD


### [PROD-302](https://impiricus.atlassian.net/browse/PROD-302) — Concierge as MSL

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2028-02-15","end":"2028-02-15"}
- **Project target:** {"start":"2028-12-01","end":"2028-12-01"}
- **Created:** 17/Feb/26 8:20 PM
- **Updated:** 14/Apr/26 5:42 PM

**Description**

#### Overview

Upload objective medical content for brands to allow concierge to respond to clinician inquiries in real time via a chat interface (like a “Virtual MSL”)

#### Value for our Business

- Rationale for new HCP registration which can grow our enrolled HCP base
- Pharma will pay for inclusion of their content on the platform

#### Value for our Customers

- Objective clinical content on demand for our HCP users
- Inclusion of information on their brands in an objective venue for pharma brands

#### What’s In Scope

- Parsing and upload of objective clinical content such as PI, trial results, and published real world analyses of widely prescribed medications and other medications of interest (not only medications for which we have a sponsor)
- Development of an LLM which delivers appropriate medical content based on a chat request 
- Responses will include not only a response to the specific question but also a link to any sources that support the response
- The AI model should include a provision to limit responses for a sponsored brand to those approved by the brand

#### What’s Out of Scope

- TBD


### [PROD-306](https://impiricus.atlassian.net/browse/PROD-306) — Custom concierge recommendations in UI

- **Initiative:** Concierge
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Created:** 18/Feb/26 6:23 AM
- **Updated:** 18/Feb/26 10:02 AM

**Description**

#### Overview

Render suggestions for custom concierge requests in UI

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-136](https://impiricus.atlassian.net/browse/PROD-136) — AI Agent as first line responder in Concierge

- **Initiative:** Concierge: Sample Request Automation
- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-04-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 21/Aug/25 11:30 AM
- **Updated:** 10/Mar/26 8:16 PM

**Description**

#### *Overview*

Utilize an AI Agent as much as possible for Concierge conversations and to handle straightforward request processes.

#### *Value for our Business:*

- Increased scalability for the Concierge Department
- Possibility for faster/real-time updates for unavailable products

#### *Value for our Customers:*

- Opportunity for communication outside of Concierge online business hours
- Faster, on-demand conversations

#### *What’s in Scope:*

- Utilizing Zendesk’s AI Agent as a first-line responder for drop-down select sample items
  - It will be the one sending links to sample closets and HCP portals for highly requested items
  - If anything is free-typed in or AI cannot provide a link, it will be escalated to a Concierge Agent

#### *What’s out of Scope:*

- AI for manufacturer direct communications (phone or email)
- Agentic AI for completion of online forms


### [PROD-114](https://impiricus.atlassian.net/browse/PROD-114) — Connect - Two-way Calling

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 20/Aug/25 10:16 AM
- **Updated:** 25/Feb/26 10:47 AM

**Description**

#### Overview

The goal of this feature is to offer a full service 2-way calling solution directly within Rep Connect.

#### Value for our Business

This will increase engagement within our network. Initial feedback and use cases of Axsome Rep Connect has been that a text message intro frequently leads to a phone call follow up. However, we want to protect HCPs numbers within our network and not directly share the number. Thus, we want to provide the capability for direct calling in Rep Connect without HCPs or Reps having to share their actual number.

#### Value for our Customers

The need for 2 way calling was requested by our first rep connect client, Axsome. They also like the fact that Reps are not sharing their actual phone numbers as well. 

#### What’s In Scope

- Phone call functionality inside of a Rep Connect conversation
  - Offer 2-way calling, with hiding of HCP number similar to Uber platform where riders can call the Driver and vice versa without sharing real numbers
  - Rep, MSL or Manager can call HCP from the Rep Connect Portal via phone call button
  - HCP can call the Rep and the call is fwded directly to Rep’s actual mobile (i.e. their phone rings without being logged in the portal)
*** can also send Rep notification or log missed call in Connect platform
  - Assumption that Manager can also call HCP as well

#### What’s Out of Scope

- Ability to schedule future calls and send calendar invites to HCPs
  - Group calls
  - Video links (like a zoom)
  - call reminders

Notes

- We tried a Goole Meet proof of concept and client did not think it was intuitive or user friendly.
- Then we tried a free pilot of Telynx and internal tests were good. 

----

Update as of 10/31/25:

- Dev team testing out new 2-way calling service
  - [https://impiricus.atlassian.net/browse/AS-387](https://impiricus.atlassian.net/browse/AS-387|smart-link) 
  - initial internal testing is good
  - next, dev is looking into assigning this to existing Rep Connect bandwidth numbers
  - in Q4, to determine if we proceed with Telynx vs Bandwidth voice calling 
  - in external roadmap to Axsome, still putting 2-way calling as Q2 26 prio

----

Offer a full service 2-way calling solution within Rep Connect

Notes 9.4.25

- We scoped a google meet POC solution, with the idea we would start with only sharing direct call conference bridge (there is a ascend daily zoom meeting recording from 9.2.25 that also shows the functionality)
_(image: Screenshot 2025-09-02 at 11.54.48 AM.png)_
- Reviewed it with Axsome, and they thought it was a clunky, antiquated user experience
- Decided for MVP launch, we will continue to allow reps/ hcps to exchange their direct phone numbers/ email addresses
  - we will monitor for how frequently the need to call happens and then determine if the google POC is necessary
- they currently send out meeting zoom like links through veeva engage where they have scheduled meetings to review slides with HCPs
- In parallel, product to get the voice campaign bandwidth letter

####


### [PROD-115](https://impiricus.atlassian.net/browse/PROD-115) — Connect - Demo Environment + Infra

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement, Operational Efficiency
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 20/Aug/25 10:17 AM
- **Updated:** 26/Feb/26 1:24 PM

**Description**

#### Overview

- As part of launching the Auvelity (Axsome) Rep Connect product, we have been asked to give multiple client facing demos.
  - QA demo to key Axsome clients (Vinny,Jamie, Justin)
  - Demo to Chief Commercial Officer
  - Video recording of Auvelity demo for Axsome board
  - Demo training for actual DSAM reps and manager
- Each time we setup a demo, it is a manual process, requiring multiple team members to facilitate setting up a testing environment and testers.
- The key problems to solve in demo:
  - Ability to setup a demo environment for a specific client (i.e. Auvelity Axsome)
*** upload 
**** real MLR messages as Initial Ascend message
**** brand specific replies
**** brand specific resource bank
**** brand specific AI stoplight
**** brand specific automatic responses, other configurable items (manager routing, etc.)
*** ability for brand to setup
**** reps
**** managers
**** compliance
**** HCPs for testing
*** ability to setup 1 to many HCP-rep conversations specifically in demo environment

#### Desired outcome

- We want a demo environment that can be used to showcase
  - 1 - general Rep Connect feature - Stelazio environment
*** a way for interested clients to test and feel out the product
  - 2- client specific training - ex. a training for actual Axsome Auvelity with their resource bank and messages
*** a way to provide training for the reps ahead of time
- We also want a way to replicate the HCP experience - can this be a series of AI HCPs who are preprogrammed to ask specific questions? 
  - Currently, Anna has been acting as the HCP
  - we also have built into Rep Connect that only 1 rep - 1 HCP can be mapped. To support trainings at scale, we need to break this rule.

#### Value for our Business

- Reduce manual labor and time required to configure and setup multiple client demos in QA and production
- Cleaner data (we had testing for Axsome conducted in a production test account)

#### Value for our Customers

- Provide sandbox training environment prior to go-live

#### What’s In Scope

- to determine exact scope
  - but initial goal is to ability to setup a demo environment for a specific client (i.e. Auvelity Axsome)
*** use real data
*** real users
  - however → solve the issue where they need test HCPs!
*** or allow 1 person to act as multiple HCPs
- many questions to determine
  - what is the best environment to host this
  - how do we support this
  - is this a true business need and worth the cost of development

#### What’s Out of Scope

- TBD

----

*Update as of 10/31/25:*

- No work on demo environment started
- Vinny at Axsome did mention a request again where he could easily demo this to executives at his company
- This is still a priority and will be something we need to deliver in 2026 but currently working on other prios
  - direct outreach
  - veeva integration
  - admin portal
- Pushing to Q1 26 start


### [PROD-116](https://impiricus.atlassian.net/browse/PROD-116) — Connect - Automated Reporting 

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-01-16","end":"2026-01-16"}
- **Project target:** {"start":"2026-05-30","end":"2026-05-30"}
- **Created:** 20/Aug/25 10:18 AM
- **Updated:** 26/Feb/26 9:49 AM

**Description**

#### Overview

Ability to create automated reports for Connect early clients.

There will be 2 lanes of Connect Reporting we need to work on:

1. PLD reporting - 
   1. scope and build automated solution via Pulse Runner
1. Campaign level metrics in Sigma
   1. We have an existing Rep Connect Dashboard; 
##### We need to launch a similar MSL connect dashboard with similar or different metrics
   1. Ascend value is highly dependent on metrics - so we need to report on metrics that matter to our clients

#### Value for our Business

- Metrics will drive Ascend business growth, contract value. If we can deliver Ascend metrics, we can continue to penetrate and expand into Pharma and drive larger Ascend enterprise contracts.

*Ascend leadership team update (Feb 2026) -->*

Metrics matter more than ever for Ascend

Ascend is not just VC interactions. We should not sell it that way, and we need to set expectations and align around metrics and KPIs accordingly. 

Metrics are of paramount importance for Ascend: and it's not about CTR or VC interactions. If Ascend is judged on those two metrics, we are not doing something right 

Ascend is all about driving lift and providing great ROI. That's the ultimate goal of Ascend, and we will measure that for all Ascend programs (quarterly)

Having clear conversations at KO about what their goals are, documenting those (in Asana on the Dashboard) and building their Ascend program to unlock those KPIs is critical

CS Pod Leads are taking point on this focus in the current state for programs that are in flight, as how we message needs a heavy handed approach. More info to come soon on that approach

This is a MAJOR area of focus for us for Ascend, and the entire CS and Sales team will be trained on our metrics approach and how to frame it when it rolls out soon

#### Value for our Customers

Similar to value for our business, these insights are driving insights into how HCPs are interacting with Reps via Rep Connect

- what HCPs interact based on target list segementation
- how are they interacting with Rep Connect compared to Rep interactions in other channels (face to face, veeva, phone calls, email)

#### What’s In Scope

- PLD reporting automation, if required for Rep Connect
- Updates to existing Sigma Dashboard that drive campaign level insights for clients and ourselves
  - Dashboards specific for
*** Rep Connect
*** MSL Connect
- Reporting drives insights for us into the new product line - examples
  - how many HCPS are engaging with Reps via Rep Connect
*** what do HCPs reach out to humans for (reps) versus automated resources
  - what are the key topics being discussed
  - how is this 2 way engagement line different than our traditional 1 way engagement lines
  - Additionally, PLD reporting if required, is a contractual obligation to our clients

#### What’s Out of Scope

- Custom reports at client level
  - overall goal is to maintain a standard of Connect reporting by product line if possible

----

*Update as of 10/31/25*

- Campaign metrics dashboard
  - v1 Auvelity Rep Connect Dashboard completed in Sigma
  - [https://app.sigmacomputing.com/impiricus/workbook/Rep-Connect-Dashboard-4SUolGAjANN5Bz1IcUPCJn](https://app.sigmacomputing.com/impiricus/workbook/Rep-Connect-Dashboard-4SUolGAjANN5Bz1IcUPCJn|smart-link) 
  - still working on 
*** AI categorization of Rep Connect HCP-Rep Topics [https://impiricus.atlassian.net/browse/AS-372](https://impiricus.atlassian.net/browse/AS-372|smart-link) 
*** Axsome has expressed interest in being able to mine the data of topics
  - CS presented initial Rep Connect metrics 
*** [https://docs.google.com/presentation/d/1A-ByZ4pJPpar3P5Yifj0K7bL2pPQ_Xiq6I6jlNRdw1c/edit?slide=id.p#slide=id.p](https://docs.google.com/presentation/d/1A-ByZ4pJPpar3P5Yifj0K7bL2pPQ_Xiq6I6jlNRdw1c/edit?slide=id.p#slide=id.p|smart-link) 
- PLD reporting
  - Q1 to do 
*** currently Rep Connect is value add
*** determine contractually obligated PLD for Rep Connect 
**** Product/ CS to own
**** Axsome request to distinguish 1-way vs 2-way outreach in Impiricus PLD reporting
*** any PLD passback to be manually supported until we build it in to a tool

----

####


### [PROD-126](https://impiricus.atlassian.net/browse/PROD-126) — Modular Integrations - Veeva Betas

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 20/Aug/25 10:25 AM
- **Updated:** 26/Feb/26 1:25 PM

**Description**

#### Overview

Veeva continues to be a major platform that has many products that pharma uses, such as

- Veeva CRM (P1)
  - ex. Axsome would like to integrate with Veeva CRM so DSAMs can directly log Rep Connect convos into their CRM
- Veeva for content submissions
  - in VC builder, if we could directly submit content from our platform
*** Pulse/ Spark/ Ascend content is currently manually uploaded into Veeva by CS into the brands content libraries
- Veeva MIRF (Axsome uses this for medical information requests submitted by HCPs)
  - ex. for Axsome - this is a clunky process where reps have to submit a MIRF in Veeva and then this MIRF has to get signed by the HCP
*** while the MIRF is pending, the Rep cannot do anything else in their Veeva CRM

If we can integrate our Ascend products into Veeva, then it will improve the overall ease of use and stickiness for our Ascend pharma clients

#### Value for our Business

- Because so many clients use Veeva CRMs, it would be a huge value add from the Ascend side if we have a ready to go integration with Veeva. Good selling point - it comes up in sales convos.
- Veeva is the 800 lb gorilla - the best route of attack for us to get a Veeva integration is to work directly with a pharma client and setup an integration with them. 
  - Then we could look into a broader Veeva partnership.

#### Value for our Customers

- Main value here is that a lot of pharma client workflows are already embedded into Veeva. The more Impiricus data we can feed into their Veeva systems, the easier it is for them to have cross-platform visibility and make workflows easier for their end users.

#### What’s In Scope

- Current scope -
  - working with Axsome to get a Veeva integration setup
*** Integrate into Veeva CRM and show Impiricus HCP activity within timeline
**** ability to log 2 way messages sent to HCPs
***** log Rep Connect conversations
***** log VC requests
***** log sample ordering
**** ability to log 1 way messages sent to HCPs
***** Pulse messages
***** Spark messages

#### What’s Out of Scope

- current focus is likely on Veeva CRM
  - other Veeva systems may come up as priority later

----

*Update as of 10/31/25:*

- Initial scoping call with Axsome Veeva Integration team on 10/30/25
  - next steps
*** P1 - focus on Request a Rep integration
*** Impiricus PLD reporting to distinguish between 1-way and 2-way HCP engagement
*** Axsome team start work on integrating Rep Connect interactions directly into Veeva CRM
**** determine MIRF process and if there’sa. better solution
- summary of meeting

_(image: Screenshot 2025-10-31 at 10.21.14 AM.png)_

- 10.30.25 meeting notes - Anna, Brian, Mike, Vinny, Julia, Joelle (Axsome Veeva), Erica (Axsome Veeva)
  - rep connect - axsome veeva integration
*** Joelle - supporting Axsome CRM
*** today dsams in veeva are logging the Rep Connect events as a call
*** goal - keep things in axsome integration instead of 3rd party
*** virtual meetings today
**** scheduled in teams or Veeva enage (these are diff links)
***** most sams are using veeva engage links
****** flash card
***** most SAMs are in the Veeva app (most sams have ipad)
*** samples today
**** sams sending link to qpharma
**** through veeva, have to ask hcp to sign for samples or send them a link
***** async link (this is what dsams) do - send them via email or only iphone
***** hcp can sign there
***** will have the qpharma integration
***** VC up front manages samples requests
***** what would need to be integrated with veeva- hcp does have samples, show in timeline view
*** veeva has an integration with samples
**** once request is signed, send to qpharma
**** info eventually comes back to veeva bc of AOCs
**** procurement part is done via qpharma directly (current scoped integration is fine)
***** qpharma integration already getting dropped in there
***** close loop with qpharma, anything that gets ordered via Impiricus SMS gets dumped
*** MIRF
**** Rep in Rep Portal will screenshot the MIRF request and then emails it to the mirf email
**** now that this has occurred, can the rep get this back into Veeva
**** essentially this has already been taken care of via email w/ screenshot
**** problem to solve - dsam does not want to fill out the MIRF form
***** synchronous form
****** if they go to send the HCP a link to sign the MIRF, then it locks their screen until HCP signs it
****** dsams uniquely remote - DSAM gets stuck
****** so dsams have to cancel the MIRF request
****** so what vinny aligned to
******* dont worry about submitting this in Veeva
******* just email the screenshot and they'll take care of it
***** if they email to Med Info, then it wont be logged into CRM
***** med info team would record it - ask Lolly if theres a report
***** Erica to take this back
*** require PLD data that is provided by Impiricus to push back to Nitro
**** simple file in multi channel view
**** for whats appearing in multi channel view,
**** *Impiricus PLD ask - differentiate between 2 way text from 1 way text*
**** *to define - what is a conversation that gets logged in Veeva*
***** *when HCP says nothing*
**** reps can log calls in 1 of 10 ways
***** train model on
****** fast and last message
*** next steps
**** Axsome team look into a few items
**** schedule axsome only time on mirf process
**** Impiricus follow ups
***** PLD to distinguish 2 way
***** AI categorization of messages
****** want to mine data but also have some general categories
**** Impiricus scope out the Rep Direct integration
**** pull in Nathan
*** *P1 - Request a Rep direct integration*
**** let Axsome call Rep Request API
**** immed HCP receives text message
**** workflow
***** HCP requests to speak to a rep
***** immed text message --> thanks for requesting a rep
****** here's the VC in the meantime
****** can order samples, request resources
****** triage to rep option

----

####


### [PROD-164](https://impiricus.atlassian.net/browse/PROD-164) — Connect - Admin Portal

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Operational Efficiency
- **Project start:** {"start":"2025-10-01","end":"2025-10-31"}
- **Project target:** {"start":"2026-01-01","end":"2026-01-31"}
- **Created:** 04/Sep/25 9:22 PM
- **Updated:** 12/Dec/25 9:22 AM

**Description**

#### Overview

In the Rep connect Portal, for any users with role brand or client admin, this portal will provide ability for Ascend clients to 

- Manage users
  - Support for login issues - abillty for admin to reset password, send password reset email
- Manage Rep to Ter mappings and changes

#### Value for our Business

Currently, this is all setup by Dev/ QA and is not scalable for multiple clients. Clients will have many changes to users and we cannot manage this.

#### Value for our Customers

At scale, internal Impiricus managing this would slow down client ability to make changes. This will give clients real-time ability to update their Rep Connect users and mappings.

#### What’s In Scope

- UI ability to Manage Users
  - edit user info
  - mark users as active/ inactive (not delete)
- Ability to import from client spreadsheet
  - Users, Roles & Territories
  - Terr to NPI
  - Terr to ZIP
- Dashboard that displays any mapping inconsistencies between the datasets.
- This functionality sets up users at the brand level and also sets the mapping such that when an HCP asks to speak to a rep, then the mapping is in place to map them to the correct Rep.

#### What’s Out of Scope

- All information is managed at brand level
  - note: users are added at client level; hierarchy is client > brand
  - all work is currently at brand level; there is no client level workspace or view.

----

*Update as of 10/31/25:*

- Client Admin portal work in development 
  - 2 parts
*** Manage Users - Add, Edit, Delete, Assign Roles, Set Active/ Inactive [https://impiricus.atlassian.net/browse/AS-304](https://impiricus.atlassian.net/browse/AS-304|smart-link) 
*** Update Rep to NPI (Rep to Ter) mappings [https://impiricus.atlassian.net/browse/AS-305](https://impiricus.atlassian.net/browse/AS-305|smart-link) 
*** bulk import spreadsheet functionality
  - Miro link  - [https://www.figma.com/design/QziZruNM2825SMrqRnMftx/Impiricus---Source-of-Truth?node-id=13495-14875&p=f&t=G6n7u3jVBM1hBqqI-0](https://www.figma.com/design/QziZruNM2825SMrqRnMftx/Impiricus---Source-of-Truth?node-id=13495-14875&p=f&t=G6n7u3jVBM1hBqqI-0|smart-link) 
- this is a Q4 25 initiative

----

Provide ability for Ascend clients to 

- Add/ Edit/ Delete users
- Support for login issues - abillty for admin to reset password, send password reset email
- Rep- HCP changes

Currently, this is all setup by Dev/ QA and is not scalable for multiple clients. Clients will have many changes to users and we cannot manage this.

####


### [PROD-165](https://impiricus.atlassian.net/browse/PROD-165) — Rep Connect - Dedicated Customer Support Team

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Project start:** {"start":"2025-11-01","end":"2025-11-30"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 04/Sep/25 9:25 PM
- **Updated:** 14/Oct/25 8:29 AM

**Description**

We need to setup dedicated resources to support Rep Connect users who have issues

We anticipate Reps to have login issues and need help with their password

We anticipate Ascend client admins to have issues and need help setting up their client accounts, making change to users or updating the Rep to HCP mappings in the system

Determine if existing resources can handle (Angela’s team) or if need addl resources.


### [PROD-190](https://impiricus.atlassian.net/browse/PROD-190) — Connect - Support for Rep Brand Overlap

- **Initiative:** Connect
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement
- **Created:** 15/Sep/25 11:56 AM
- **Updated:** 09/Dec/25 12:58 PM

**Description**

*Update as of 10/31/25:*

- Dev added support for brands in Ascend Rep Connect data
  - [https://impiricus.atlassian.net/browse/AS-309](https://impiricus.atlassian.net/browse/AS-309|smart-link) 
- This will assist in supporting any UI and data changes when we add additional Axsome brands and there is overlap
- Product to continue to scope timelines with Axsome to determine when to prioritize this work
  - we will need UI changes to support reps on multiple brands
  - building out client admin portal with assumption that 1 client admin may be overseeing multiple brands

----

Axsome notes from 9.3.25 call

- only auvelity brand has dsams
- SAMs - 3 brands, soon to be 4 - filing for q4 alzheimers, planning for overlap
- current auvelity 300, sunosi 75, symbravo 100 (some overlap)
- certain reps that have the ability to sell multiple brands -

Need in future to support brand overlap at manufacturer level. 

Ability for 1 Axsome rep to login and view/ have multiple conversations on different brands. UI to separate the brands (probably another tab of conversations).


### [PROD-195](https://impiricus.atlassian.net/browse/PROD-195) — Connect - Ability to reassign an HCP to another rep (within Rep connect)

- **Initiative:** Connect
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 15/Sep/25 1:57 PM
- **Updated:** 26/Feb/26 8:46 AM

**Description**

#### Overview

Potential client need to re-assign an HCP conversation to another rep. Current functionality is that manager is the assigned backup.

- If rep is on vacation and wants to re-assign their convos to another Rep
- If rep is on extended leave (maternity leave)
- Note this would be assign to a Rep within the same Product line, i.e. reassign a rep from Auvelity Rep Connect to another Rep in Rep Connect.
  - There is another ticket where we will need to transfer an HCP talking to a rep from Auvelity Rep Connect to a MSL in Auvelity MSL connect.

#### Value for our Business

- Meets business needs for our customers

#### Value for our Customers

- Aligns to how current workflows work today
  - typically if a rep/ team member is out, there is a way to transfer conversations

#### What’s In Scope

- needs further thought as to how re-assignment works
  - is it a 4 way convo - HCP, rep 1, rep 2 and Manager
  - or does the re-assigment means rep 1 is not part of the conversation (this makes sense)
  - but what if rep 1 wants to takeover the convo? does rep 2 reassign this back to rep 1
*** we do not currently support conversation history transfer between reps

#### What’s Out of Scope

- TBD

----

*Update as of 10/31/25:*

- No update on this yet
- Auvelity has not mentioned this as a need yet as Jamie the manager is currently handling any Rep coverage gap needs
- will continue to monitor 
- will delay timeline to Q1 26

----

####


### [PROD-198](https://impiricus.atlassian.net/browse/PROD-198) — (REMOVE) Rep Connect Blue Bubbles via Linq 

- **Initiative:** Connect
- **Priority:** Low
- **Reporter:** Mike Gelber
- **Created:** 19/Sep/25 11:21 AM
- **Updated:** 03/Nov/25 10:57 AM

**Description**

*Update as of 10/31/25:*

No movement on this, not sure it’s viable

Originally scoped as a solution to boost Rep believability in convos

Linq is a solution that enables convos to look like iMessages

[https://linqapp.com/s/linq-blue](https://linqapp.com/s/linq-blue|smart-link)


### [PROD-220](https://impiricus.atlassian.net/browse/PROD-220) — Connect - Rep triggered messages to HCPs

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Created:** 12/Nov/25 11:19 AM
- **Updated:** 02/Mar/26 10:42 AM

**Description**

#### Overview

Request for ability for Reps to trigger pre-approved content to an HCP post visit. This has come up a sales need as a Rep Connect lite, for clients who are a hard no on Rep Connect. Additional, even Axsome who is using Rep Connect, would find it useful to also have the ability to send triggered messages.

The goal of this is to expand the offerings and ways we can initiate and provide HCP-Rep connections.

Could also apply to other Connect product lines - MSL, FRM

#### Value for our Business

- Offers Rep connect functionality via alternative format
  - currently, Rep Connect available as fully loaded option → HCPs receive a Pulse/ Spark message that are already on a target list for Reps
  - next, we’re developing HCP Direct Outreach - offering any HCP/ Office Staff to scan a QR code and be connected to a Rep
  - this would be a third alternative for HCP-Rep connection
*** Reps could trigger messages to HCPs under certain business rules

#### Value for our Customers

- Great entry point to offer triggered messages; some pharma will never be interested in the deeper level of Rep connect offered (i.e. free way text convos between HCPs & Reps, “unfettered access”)
- this offers an additional way
  - Reps can trigger a message and have (limited) capabilities on how to continue to engage with that HCP

#### What’s In Scope

- Details to scope:
  - How does Rep get HCP number and send them a message
*** is this a message from the HCP or is this a Spark message from Impiricus
*** what happens if HCP responds to that message
  - Legal/compliance - does HCP need to be opted in, is this a different channel
  - what does the UI look like for Reps, how do they select a list of messages 
  - what happens after Reps send a triggered message
*** does it turn into a conversation like Rep Connect
*** how is the same vs diff than actual Rep Connect

#### What’s Out of Scope

- TBD


### [PROD-236](https://impiricus.atlassian.net/browse/PROD-236) — Connect - Branding & UI Update Prior to 2nd Launch

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2026-02-01","end":"2026-02-28"}
- **Created:** 09/Dec/25 12:08 PM
- **Updated:** 25/Feb/26 10:25 AM

**Description**

#### Overview

We want to rebrand the Rep Connect to Connect in order to support multiple Connect Product Lines: MSL, FRM, etc.

Secondly, we want to update the existing Rep Connect UI to the new Impiricus branding. And we’d like to update the python libraries that support the front end as well.

Goal is to update branding before we launch our second brand on Connect.

#### Value for our Business

- Modern UI gives impression of innovative tech company (which we are)
- Presents cohesive branding 
- Provides one source of truth design for future Ascend platform

#### Value for our Customers

- they are impressed by the user experience
- not only does it look good, but it functions well for them (that is a true bonus)
- easy to use leads to good impression

#### What’s In Scope

- Connect rebranding on all Connect UI
  - log in
  - admin portal
  - conversations view
- python libraries update
- Adding name branding to portal

#### What’s Out of Scope

- n/a


### [PROD-237](https://impiricus.atlassian.net/browse/PROD-237) — Connect - Ability for HCP to ask for MSL or Rep 

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation, Operational Efficiency
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 09/Dec/25 2:24 PM
- **Updated:** 09/Dec/25 2:24 PM

**Description**

#### Overview

- If a client has multiple connects, how do we allow an HCP to transfer or loop in someone else
  - or vice versa, the HCP has a question for a Rep but the Rep wants to loop in the MSL or FRM
- Allow real time "transfer" or "loop in" MSL into a Rep <> HCP call 

#### Value for our Business

- Major value driver if we can drive real-time, seamless and compliant connected engagement across multiple pharma departments while also providing a super seamless HCP experience

#### Value for our Customers

- same value as business
- Impiricus starts to become a key hub for multiple parts of their pharma business; this will drive stickiness and retention

#### What’s In Scope

- TO DISCUSS SCOPE
  - Is it a 3 way chat between MSL, Rep and HCP
*** or is it 2 separate convos (to check with client on legal/compliance allowability and/or preferences
  - Define HCP experience 

#### What’s Out of Scope

- TBD


### [PROD-272](https://impiricus.atlassian.net/browse/PROD-272) — Connect - MSL Pathway Initial Setup

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-03-01","end":"2026-03-31"}
- **Created:** 12/Dec/25 11:41 AM
- **Updated:** 26/Feb/26 8:48 AM

**Description**

#### Overview

This is to leverage the existing Rep Connect platform for Medical Science Liaisons within pharma, or Medical Affairs teams.

This is a different organization in pharma, separate from commercial. They focus on disease state or indication awareness and education, typically pre-launch but can certainly support post-launch activities.

MSLs typically act similarly to Reps, in that they have target lists of HCPs who they are trying to reach out and provide education about certain indications. The Connect platform would provide a similar value prop as Rep Connect - expanding opportunities for breadth and depth of coverage.

Also, a key value in expanding the the Connect platform is the opportunity for HCP to engage with multiple pharma contacts (rep, MSL, FRM) all through a single solution. 

#### Value for our Business

- Same platform built for reps can be leveraged for other pharma departments
- MSL Connect would make us sticky across pharma.
- The goal is that entry into one part of pharma, i.e. through MSL, would prove valuable and then we can sell our other Ascend products into other parts of the business, providing a one stop shop.

#### Value for our Customers

- There aren’t great tools out there today that can offer what Connect offers
  - real-time access
  - no need to manage app download or logins for both HCP and MSLs
- The platform can also serve as a mechanism to track MSL effectiveness as well as provide insights into what topics HCPs are interested in learning more from MSLs

#### What’s In Scope

- MSL Initial Setup 
  - Adjust Connect backend architecture to support Therapeutic Area for MSL setup
  - Create distinct MSL role
  - Update any functionality, UI, messaging that directly says “Rep Connect” to generic “Connect”
- initial goal is to offer same functionality as Rep Connect
  - Initial outreach through SMS outbound messaging
  - Ability for HCP direct outreach 
  - MSL approved content
  - real-time conversation between HCP-Rep
  - data driven insights to pharma
- future state (in 2026 roadmap)
  - ability for 3 way conversation, rep, msl, HCP
  - or for rep to transfer convo to an MSL
  - 2 way calling, zoom scheduling capabilities

#### What’s Out of Scope

- TBD


### [PROD-273](https://impiricus.atlassian.net/browse/PROD-273) — Connect - FRM Pathway

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 12/Dec/25 11:43 AM
- **Updated:** 26/Feb/26 9:23 AM

**Description**

#### Overview

This is to leverage the existing Rep Connect platform for Field Reimbursement Managers (FRM) within pharma.

FRM teams help HCPs with coverage or access issues, such as prior authorization, or if there are complicated patient portal steps to sign up for particular drugs.

FRMs engage with HCPs similarly to Reps in that they may be virtual or go in-office. The key differentiator is that many FRMs work with the Office Staff/ Office Practice Manager rather than the HCP. It is typically not the HCP who is responsible for working through any payer coverage issues. 

The Connect platform would provide a similar value prop as Rep or MSL Connect - expanding opportunities for breadth and depth of coverage for FRMs.

Also, a key value in expanding the the Connect platform is the opportunity for HCP to engage with multiple pharma contacts (rep, MSL, FRM) all through a single solution. 

#### Value for our Business

- Same platform built for reps can be leveraged for other pharma departments
- FRM Connect would make us sticky across pharma - today, we see HCPs responding to our 1 way SMS with coverage or access issues.
- The goal is that entry into one part of pharma, i.e. through MSL, would prove valuable and then we can sell our other Ascend products into other parts of the business, providing a one stop shop.

#### Value for our Customers

- Coverage and Access is a huge pain point for HCPs and it is in pharma’s best interest to make the process of script writing and patient adoption as easy as possible
- Doctors are going to prescribe the drugs that are easiest to navigate
  - a tool like FRM Connect would help extend the reach of FRMs

#### What’s In Scope

- initial goal is to offer same functionality as Rep Connect
  - Initial outreach through SMS outbound messaging
  - Ability for HCP direct outreach 
  - MSL approved content
  - real-time conversation between HCP-Rep
  - data driven insights to pharma
- future state
  - ability for 3 way conversation, rep, msl, HCP
  - or for rep to transfer convo to an MSL
- based on early discovery, we will very likely need to support 
  - calling capabilities and zoom capabilities for FRM to help Office Managers
  - Also, to scope a solution where FRMs can easily connect to Office Staff vs the HCP
*** Do we continue to target HCPs with messaging but allow them to easily transfer the convo to the Office Staff
*** Or directly target the office staff 

#### What’s Out of Scope

- TBD


### [PROD-274](https://impiricus.atlassian.net/browse/PROD-274) — Connect - HCP Inbound v2 to support chatbot (multichannel)

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 15/Dec/25 9:11 AM
- **Updated:** 26/Feb/26 8:57 AM

**Description**

#### Overview

This ticket covers the direct outreach request from other Ascend channels, with first up being chatbot. In chatbot, we want to build functionality to support an HCP 1-click requesting a rep via the chatbot. The HCP would be able to then talk to a rep (need to determine how reps are mapped to HCPs, likely based on existing territory mappings).

#### Value for our Business

- Drives HCP engagement and ease of use where an HCP can now connect to a rep via different channels; typically there is already a form on brand websites where HCPs can connect to a rep, this would bring a real-time connection which would be more valuable than the form
- Multichannel engagement will drive Ascend platform value

#### Value for our Customers

- similar as business

#### What’s In Scope

- scope to be determined
  - on chatbot
*** button to request a rep
*** ability to connect either HCP (and/ or Office Staff) to Rep
**** ask for NPI or other information
*** Then the HCP is connected to a rep via chatbot
**** determine if chatbot experience makes more sense or if we connect HCP to SMS
  - needs scoping
*** if HCP has existing convo to a Rep - determine behavior vs. if new HCP-Rep convo

#### What’s Out of Scope

- future state via chatbot - seamless transfer of conversation from chatbot to SMS to email


### [PROD-323](https://impiricus.atlassian.net/browse/PROD-323) — Connect - Ability for HCP to opt out of Connect convo

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 26/Feb/26 8:40 AM
- **Updated:** 26/Feb/26 1:17 PM

**Description**

#### Overview

- We want to provide a way for HCPs to opt out/ end the conversation with a rep/ msl.
- These HCPS may have accidentally connected with a rep or intentionally connected and then realize they don’t want to keep chatting with the rep

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- ability for HCP to reply “end” and end that convo
  - that does not opt them out of our network, brand level, etc.
- ability for HCP to reply “rep” or something to start that again
  - *think about this when VC Orchestrator is part of it

#### What’s Out of Scope

- TBD


### [PROD-324](https://impiricus.atlassian.net/browse/PROD-324) — Connect - Self Service Admin Portal Buildout

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 26/Feb/26 8:50 AM
- **Updated:** 26/Feb/26 1:23 PM

**Description**

#### Overview

- Continue to build UI functionality in Admin Portal so Clients/ CS Admins can add/ edit without dev intervention

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- Ability for Super Admins to 
  - Add/ Edit/ Delete Resource Bank 
  - Add users as Super Admins - switch them between roles
- Update Zip to Ter functionality in Admin Portal
- AI Stoplight

#### What’s Out of Scope

- TBD


### [PROD-327](https://impiricus.atlassian.net/browse/PROD-327) — Connect - Human in the Loop: Create HCP-Rep conversation via Connect automatically 

- **Initiative:** Connect
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Operational Efficiency
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 26/Feb/26 9:22 AM
- **Updated:** 26/Feb/26 9:22 AM

**Description**

#### Overview

TBD

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- Connect HCP to Connect (Rep, MSL) automatically vs manual
  - to determine - client preferences on mapping any HCP to a rep 
*** HCP to be mapped as NPI target
*** HCP zip code determined (pulled from NPPES)
*** default auto mapped HCPs go to specific user/role, i.e. manager
*** tagging this HCP in Connect platform with appropriate inbound channel

#### What’s Out of Scope

- TBD


### [PROD-268](https://impiricus.atlassian.net/browse/PROD-268) — Content Preference Data for Content Team

- **Initiative:** Content Affinity
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 10/Dec/25 2:19 PM
- **Updated:** 03/Mar/26 9:15 AM

**Description**

#### Overview

This initiative focuses on partnering with the Content Team to produce multiple MLR compliant message variations (i.e. such as short, medium, and long formats) to support ION’s content preference optimization ([https://impiricus.atlassian.net/browse/PROD-265](https://impiricus.atlassian.net/browse/PROD-265|smart-link)). These structured content variants enable ION to dynamically select the best performing message version for each HCP based on their demonstrated content length affinity.

#### Value for our Business

Creating standardized message variations unlocks the next level of ION personalization by allowing the algorithm to tailor content delivery to individual HCP behaviors. This strengthens product differentiation, improves engagement performance, and streamlines future optimization work that relies on content level variables.

*Business Drivers:* Customer Engagement, Innovation

#### Value for our Customers

Customers gain higher quality engagement as HCPs receive the type of content they are most likely to interact with, improving resonance, CTRs, and overall campaign effectiveness.

#### What’s In Scope

- Collaborating with the Content Team to define required message-length formats
- Creating standardized MLR-approved templates across campaigns
- Establishing guidelines for message variation production

#### What’s Out of Scope

- Developing net-new campaign content types outside of message length variations

*Notes from 12/10/25:*

- Chris & Alan are calling this “multi dimensional demeanor” (i.e. there are no limit to that amount of variables we can add)


### [PROD-111](https://impiricus.atlassian.net/browse/PROD-111) — Protecting & Growing Oncologist Segment of Network

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Created:** 15/Aug/25 4:32 PM
- **Updated:** 25/Aug/25 12:17 PM

**Description**

Heading into Q4 it has become clear that we need to be proactive around how we handle the Oncologist segment of our Network. We’re putting together a multi-pronged plan for how we can grow, protect, & sustain healthy Oncologist relationships.

*The attack plan will consist of 4 general buckets:*

- Net new additions to the Network
  - DocUpdate Ads Targeting 
*** Ben will share a list of Oncs we’ve seen in client TLs but who we haven’t been able to find a Clay number for
  - Continue finding new numbers for Oncs via Clay
*** Prioritize previously nuclear opted out Oncs as part of [https://impiricus.atlassian.net/browse/DT-318](https://impiricus.atlassian.net/browse/DT-318|smart-link) 
- Engaging existing Oncologists to boost disposition scores
  - Perform overlap of Klick Survey Target List (544652) and include Oncs not on this list that have < =3- DD or one’s how previously have had high engagement and have since dropped off
*** Should we have a general follow up a couple of weeks after to maintain relevancy with the HCPs?
- Direct Outreach
  - Conference or Society Partnerships
  - In-Person Events
  - Direct calling (Lauren reaching out to Oncs??)
- Changes to Relationship Logic
  - Let’s look into and determine if we need to change any way we interact with Oncs
*** i.e. should we increase the _daysbetweenmessages_ for them?

The Data Analytics team is doing analysis around trends in Oncologist engagement as well as other indicators across specialties, being tracked in the below tickets:

- [https://impiricus.atlassian.net/browse/DA-16](https://impiricus.atlassian.net/browse/DA-16|smart-link)
- [https://impiricus.atlassian.net/browse/DA-18](https://impiricus.atlassian.net/browse/DA-18|smart-link)
- [https://impiricus.atlassian.net/browse/DA-19](https://impiricus.atlassian.net/browse/DA-19|smart-link) 
- [https://impiricus.atlassian.net/browse/DA-20](https://impiricus.atlassian.net/browse/DA-20|smart-link)


### [PROD-154](https://impiricus.atlassian.net/browse/PROD-154) — Direct Outreach to Re-Engage Oncs

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-10-20","end":"2025-10-20"}
- **Created:** 25/Aug/25 11:58 AM
- **Updated:** 09/Dec/25 9:28 PM

**Description**

Ideas for Direct Outreach:

- Conference or Society Partnerships
  - Notes from conversation with Waqas [here](https://docs.google.com/document/d/1IDi3iuTLGVOYxVHYm6Sr6eNsv7xcvIZ6uRLmX3if8qA/edit?tab=t.0)
- In-Person Events
- Direct calling (Lauren reaching out to Oncs??)


### [PROD-155](https://impiricus.atlassian.net/browse/PROD-155) — Revisit Interaction Logic for Oncologist Segment

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-11-03","end":"2025-11-03"}
- **Created:** 25/Aug/25 12:01 PM
- **Updated:** 09/Dec/25 9:28 PM

**Description**

Do we need to make any changes to how we interact with Oncologists?

- Let’s look into and determine if we need to change any way we interact with Oncs
  - i.e. should we increase the _daysbetweenmessages_ for them?

 

The Data Analytics team is doing analysis around trends in Oncologist engagement as well as other indicators across specialties, being tracked in the below tickets:

- [https://impiricus.atlassian.net/browse/DA-16](https://impiricus.atlassian.net/browse/DA-16|smart-link)
- [https://impiricus.atlassian.net/browse/DA-18](https://impiricus.atlassian.net/browse/DA-18|smart-link)
- [https://impiricus.atlassian.net/browse/DA-19](https://impiricus.atlassian.net/browse/DA-19|smart-link)
- [https://impiricus.atlassian.net/browse/DA-20](https://impiricus.atlassian.net/browse/DA-20|smart-link)


### [PROD-287](https://impiricus.atlassian.net/browse/PROD-287) — Trial Navigator: Migrating to own chat based function w/multiple partners

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-09-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-11-01","end":"2026-11-30"}
- **Created:** 02/Jan/26 1:48 PM
- **Updated:** 13/Apr/26 5:06 PM

**Description**

#### Overview

Chat-based, AI-enabled tool which allows searching for clinical trials based on condition, geography and inclusion/exclusion criteria as available from [clinicaltrials.gov](http://clinicaltrials.gov) and other sources. This project will develop the search tool in house, enhanced with partner data, and will refer HCPs and patients to partners to answer questions and handle patient onboarding. The in-house tool will drive patients to multiple partners including existing partner 1104 Health. 1104 Health’s search functionality will be sunset and replaced with in-house search as part of this project. 

#### Value for our Business

- Drives engagement with high value prescribers in high value specialties, initially dermatology and oncology
- Expand beyond the oncology focus of 1104 Health.
- Add more sponsored trials across partners to generate more revenue. 

#### Value for our Customers

- Saves time currently spent in searching for trials
- Expands universe of trials available in search and improves data available for each

#### What’s In Scope

- Chat-based search for use by HCPs to match patients with appropriate trials based on that already developed and demonstrated
- Existing functionlaity is based on [clinicaltrials.gov](http://clinicaltrials.gov) data; refinements will pull in additional data sets including investigator contacts at the trial site level as sources from partners
- Search function refers HCPs to partners who have sponsorship relationships with pharmaceutical companies and CROs

#### What’s Out of Scope

- Direct relationships with CROs
- Facilitation of HCPs becoming trial sites
- Any human based support for questions or patient enrollment (all such inquiries are referred to partners)


### [PROD-187](https://impiricus.atlassian.net/browse/PROD-187) — Customized HCP Journeys Integrated with Ascend

- **Initiative:** HCP Journeys
- **Priority:** Low
- **Assignee:** Scott Burian
- **Reporter:** Anna McDermott
- **Value drivers:** Network Health, Operational Efficiency
- **Created:** 12/Sep/25 1:30 PM
- **Updated:** 03/Mar/26 11:15 AM

**Description**

#### *Overview*

This initiative focuses on enabling automated end-to-end journey orchestration for HCPs across the Impiricus platform. Instead of manually configuring campaigns across various product lines to set up a cross-product journey, the system will dynamically determine journey steps and transitions based on parameters established pre campaign launch.

#### *Value for our Business*

Automating cross-product HCP journeys strengthens our competitive moat by transforming Impiricus into a unified engagement platform rather than a collection of independent products. It reduces operational overhead, streamlines campaign setup, and unlocks more sophisticated multi-touch programs that scale with minimal manual effort.

*Business Drivers:* Operational Efficiency, Network Health

#### *Value for our Customers*

Customers benefit from more seamless, intelligent, and personalized engagement paths that span SMS, Ascend outreach, and future channels. Automated journeys improve targeting accuracy, enhance campaign outcomes, and reduce time-to-launch for multiproduct strategies.

#### *What’s In Scope*

- Defining journey logic that spans PulseRunner and Ascend
- Building automation to transition HCPs from SMS engagement into Ascend based on triggers or behavioral criteria
- Enabling cross-product sequencing within the platform
- Establishing an internal interface to configure journey rules without manual data extraction

#### *What’s Out of Scope*

- Full redesign of Ascend or PulseRunner user interfaces
- Development of net-new channels


### [PROD-258](https://impiricus.atlassian.net/browse/PROD-258) — ION KPI-Level Custom Optimization

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-12-01","end":"2026-12-31"}
- **Project target:** {"start":"2027-06-01","end":"2027-06-30"}
- **Created:** 10/Dec/25 8:13 AM
- **Updated:** 05/Mar/26 4:14 PM

**Description**

#### Overview

This epic introduces KPI-level custom optimization within ION, allowing each campaign to select one primary optimization goal (i.e. guaranteed delivery, guaranteed engagement rate, or downstream impact like script lift) while the system continues to optimize for all KPIs in the background. The goal is to give ION clear directional priority that aligns with campaign objectives and brand strategies.

#### Value for our Business

Enabling campaign specific optimization priorities enhances our product flexibility and positions ION as a more customizable, outcomes driven decisioning engine. This differentiation strengthens our commercial offering, improves client satisfaction, and unlocks new opportunities for premium or KPI-specific packages.

*Business Drivers:* Customer Engagement, Innovation

#### Value for our Customers

Customers gain more control over how their campaigns are optimized, ensuring ION aligns with brand goals. Prioritized KPI optimization enables more transparent performance tradeoffs and clearer value realization.

#### What’s In Scope

- Defining available KPI optimization options
- Building campaign-level configuration settings
- Adjusting ION’s decisioning logic to prioritize one selected KPI
- Validating performance impacts across different targets

#### What’s Out of Scope

- Changes to client billing structures


### [PROD-259](https://impiricus.atlassian.net/browse/PROD-259) — ION-Powered Look a Like Audience Extension

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2027-01-01","end":"2027-03-31"}
- **Project target:** {"start":"2028-01-01","end":"2028-03-31"}
- **Created:** 10/Dec/25 8:20 AM
- **Updated:** 03/Mar/26 11:40 AM

**Description**

#### Overview

This epic introduces ION-powered look-a-like audience generation and optimization, enabling clients to supplement their existing target lists with intelligently recommended HCPs who share similar attributes, behaviors, or engagement patterns.

The goal is to expand high-quality reach using predictive similarity modeling embedded directly into ION’s delivery engine. This transforms audience expansion from a manual, one-time action into a data-driven, continuously improving optimization layer.

#### Value for our Business

Look-a-like capability strengthens product differentiation by embedding predictive targeting intelligence within ION. It expands the effective addressable audience for restrictive campaigns and improves campaign efficiency through algorithmic expansion.

This unlocks new monetization opportunities by increasing usable inventory and enhancing performance outcomes, reinforcing ION’s role as an intelligent delivery and targeting engine.

##### Business Drivers

Business Growth, Customer Engagement, & Innovation

#### Value for our Customers

Customers gain broader, high-value reach beyond their initial target list by leveraging ION’s intelligence to identify similar HCPs likely to engage.

This improves campaign performance, enhances optimization flexibility, and supports stronger engagement outcomes without requiring manual list expansion.

#### What’s In Scope

- Developing the methodology for generating look-a-like audiences
- Defining similarity criteria (behavioral signals, content engagement, profile attributes, etc.)
- Building similarity scoring and ranking models
- Integrating recommendations into ION’s delivery workflow
- Enabling controlled optimization toward look-a-like audiences
- Validating performance uplift through controlled testing

#### What’s Out of Scope

- Full-scale standalone audience segmentation products
- Manual curated expansion workflows (covered under Network Demand Activation epic)
- Identity infrastructure development (covered under Device Graph initiative)
- Fully autonomous audience replacement without guardrails


### [PROD-265](https://impiricus.atlassian.net/browse/PROD-265) — Content Preference as ION Variable

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Innovation, Network Health
- **Project start:** {"start":"2026-08-01","end":"2026-08-31"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 10/Dec/25 10:13 AM
- **Updated:** 05/Mar/26 4:17 PM

**Description**

We’re turning the research from [https://impiricus.atlassian.net/browse/INT-2591](https://impiricus.atlassian.net/browse/INT-2591|smart-link) into product.

#### Overview

This epic focuses on incorporating content preference signals (i.e. such as ideal message length and likelihood to click on embedded links) into ION’s optimization logic. These insights, discovered through ION Marketing research, will allow ION to tailor messaging strategies to individual HCP behaviors.

#### Value for our Business

Adding content preference as a variable strengthens ION’s personalization capabilities and enhances engagement performance through more context aware delivery. It also increases the strategic value of our content and optimization engine, creating differentiation in how effectively we target message formats to HCPs.

*Business Driver:* Network Health, Innovation

#### Value for our Customers

Customers benefit from higher quality engagement as messaging becomes better aligned to each HCP’s preferences, increasing CTR and improving downstream actions. This leads to more efficient campaigns, better KPI performance, and clearer insight into how content strategy influences outcomes.

#### What’s In Scope

- Modeling content preference signals such as preferred message length and link-click likelihood
- Incorporating these signals into ION’s decisioning logic
- Defining thresholds or scoring for preference categories

#### What’s Out of Scope

- TBD

*NOTES:* 

- Or says this is important we can get it done before EOY


### [PROD-331](https://impiricus.atlassian.net/browse/PROD-331) — ION Time of Day Optimization

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Innovation, Network Health, Operational Efficiency
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 03/Mar/26 10:18 AM
- **Updated:** 06/Mar/26 3:38 PM

**Description**

#### Overview

This initiative introduces *Time of Day Optimization* into ION, enabling delivery decisions to account for when an HCP is most likely to engage within the working day. Today, delivery timing is primarily dictated by queue-based execution (Celery), without consideration for behavioral engagement patterns at the intra-day level.

By incorporating a time-of-day variable into the ION optimization framework, we will transition from operationally convenient delivery timing to behaviorally intelligent delivery timing. This enhancement will leverage historical engagement data to identify correlations between time windows and HCP responsiveness, enabling personalized delivery schedules that increase engagement probability and overall network efficiency.

#### Value for our Business

Time of Day Optimization enhances ION’s intelligence layer by introducing a high-impact behavioral variable into delivery decisioning. This increases campaign performance without requiring additional inventory, directly improving efficiency and ROI.

It also strengthens ION’s differentiation as a true adaptive delivery system rather than a rules-based scheduler. By leveraging historical engagement data at the HCP level, we increase the compounding value of our data assets and create additional defensibility in our optimization engine.

Over time, this initiative supports higher engagement rates, stronger customer retention, and improved campaign performance benchmarks.

##### Business Drivers

Operational Efficiency, Network Health, Business Growth, & Innovation

#### Value for our Customers

Customers benefit from improved engagement rates and more precise HCP outreach. Messages are delivered at moments when providers are more likely to review and interact with content, increasing effectiveness without increasing spend.

Time-aware delivery also improves pacing stability, reduces wasted impressions, and aligns outreach with real-world workflow patterns. This ultimately drives better campaign outcomes and greater confidence in Impiricus as an intelligent engagement partner.

#### What’s In Scope

- Conducting historical data analysis to identify time-of-day engagement patterns at the HCP level
- Determining whether statistically significant correlations exist between time windows and engagement likelihood
- Designing a Time of Day variable within the ION optimization framework
- Developing logic to incorporate time affinity scoring into delivery decisioning
- Building infrastructure to support time-window-based scheduling within ION (beyond Celery queue ordering)
- Testing and validating performance improvements via controlled experimentation
- Establishing a framework for continuous learning and refinement of time-based delivery models

#### What’s Out of Scope

- Real-time adaptive micro-scheduling (sub-hour optimization) in initial release
- External third-party data integrations related to HCP work schedules
- Replacing the core ION architecture or campaign pacing logic
- Immediate deprecation of the existing Celery-based scheduling system; this enhancement will be layered into ION progressively and validated before broader rollout


### [PROD-332](https://impiricus.atlassian.net/browse/PROD-332) — ION Zero Revenue Slippage

- **Initiative:** ION
- **Priority:** Medium
- **Reporter:** Scott Burian
- **Value drivers:** Network Health, Operational Efficiency
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 03/Mar/26 11:18 AM
- **Updated:** 04/Mar/26 11:21 AM

**Description**

#### Overview

This initiative focuses on *Revenue Slippage Prevention for 2026 Campaigns*, with the goal of ensuring that all campaigns contracted for 2026 fully deliver and conclude within the 2026 calendar year.

Revenue slippage into 2027 creates financial forecasting risk, operational strain, and misalignment between booked revenue and realized delivery. While this is a cross-functional effort spanning Sales, Operations, Finance, and Product, from a Product perspective the core mandate is to achieve *100% visibility into campaign delivery health, pacing accuracy, and forecasted completion dates*.

We will leverage ION’s enhanced forecasting and delivery precision capabilities to proactively identify at-risk campaigns and intervene before timeline drift occurs. In parallel, we will strengthen internal workflow safeguards to prevent overdelivery, pacing misalignment, and operational gaps that contribute to revenue slippage.

#### Value for our Business

Preventing revenue slippage directly protects revenue recognition integrity, improves forecast reliability, and reduces end-of-year operational fire drills.

This initiative increases confidence in our revenue model by aligning contracted timelines with actual delivery performance. It also reduces operational inefficiencies caused by last-minute adjustments, under-pacing corrections, and inventory strain.

By combining improved forecasting (via ION) with operational workflow guardrails, we create a more predictable and scalable delivery engine that strengthens financial planning and executive visibility.

##### Business Drivers

Operational Efficiency, Business Growth, Platform Integrity, & Network Health

#### Value for our Customers

Customers benefit from clearer delivery expectations, more reliable pacing, and stronger alignment between contracted timelines and execution.

Proactive monitoring reduces the need for rushed year-end adjustments, minimizes abrupt delivery shifts, and ensures campaigns run according to agreed-upon strategic plans. This builds trust and reinforces Impiricus as a disciplined and reliable partner.

#### What’s In Scope

- Establishing real-time visibility into campaign pacing, forecasted completion dates, and revenue risk
- Defining and tracking “at-risk of slippage” indicators within Product dashboards
- Leveraging ION forecasting to improve delivery precision and end-date predictability
- Building alerting mechanisms for campaigns trending beyond contracted end dates
- Implementing safeguards to prevent overdelivery and pacing drift
- Partnering cross-functionally to update internal workflows that contribute to slippage
- Creating standardized reporting for executive visibility into 2026 delivery health

#### What’s Out of Scope

- Retroactive restructuring of existing 2025 campaign agreements
- Changes to contractual revenue terms
- Manual end-of-year intervention as the primary strategy (this initiative focuses on systemic prevention)
- Rebuilding ION’s core architecture beyond enhancements required for forecasting precision


### [PROD-334](https://impiricus.atlassian.net/browse/PROD-334) — Low Demand Network HCPs Activation

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Customer Engagement, Network Health, Operational Efficiency
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2027-05-01","end":"2027-05-31"}
- **Created:** 03/Mar/26 11:39 AM
- **Updated:** 03/Mar/26 11:41 AM

**Description**

#### Overview

This epic focuses on curating and activating demand for the 1M+ HCPs already reachable within the Impiricus Network but not currently targeted in campaigns.

While look-a-like modeling expands audiences algorithmically, this initiative addresses a more foundational opportunity: significant portions of our deterministic, reachable network remain under-monetized. The goal is to surface and operationalize structured pathways to activate these untargeted HCPs, unlocking incremental revenue from existing supply.

This effort is focused on monetizing latent reach through visibility, packaging, and workflow enablement, not predictive modeling.

#### Value for our Business

This initiative unlocks revenue from existing network supply without requiring net-new HCP acquisition. By activating under-targeted but reachable providers, we increase revenue per HCP and improve overall network yield.

It reduces revenue concentration across commonly targeted segments and strengthens long-tail monetization. By broadening demand across the network, we improve utilization efficiency and create incremental growth capacity.

##### Business Drivers

Business Growth, Network Health, Customer Engagement, & Operational Efficiency

#### Value for our Customers

Customers gain structured access to incremental, high-quality HCP segments already within the Impiricus Network. Rather than relying exclusively on historical targeting norms, brands can expand reach in a more deliberate and curated way.

This improves scale, increases delivery flexibility, and supports broader campaign objectives without introducing probabilistic targeting risk.

#### What’s In Scope

- Quantifying untargeted but reachable HCP inventory across the network
- Identifying high-potential under-monetized segments
- Creating internal visibility into network utilization gaps
- Building workflows to support curated reach expansion
- Packaging incremental audience opportunities for Sales/CS enablement
- Measuring incremental revenue lift from newly activated HCP cohorts

#### What’s Out of Scope

- Predictive or algorithmic similarity modeling (covered in separate Look-a-Like Optimization epic)
- Net-new HCP acquisition initiatives
- Development of a full segmentation product suite
- Major changes to ION’s optimization engine


### [PROD-335](https://impiricus.atlassian.net/browse/PROD-335) — ION Forecasting Sandbox

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Customer Engagement, Innovation, Network Health, Operational Efficiency
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 03/Mar/26 12:00 PM
- **Updated:** 05/Mar/26 4:24 PM

**Description**

#### Overview

The *ION Forecasting Sandbox* is a pre-campaign simulation environment that allows users to upload new or existing target lists and evaluate delivery feasibility before launch.

The Sandbox will provide forward-looking insights into HCP overlap, projected deliverability, pacing feasibility, ideal flight timing, and opportunities for audience expansion. Rather than discovering constraints mid-campaign, customers and internal teams will have a proactive planning tool powered by ION’s intelligence layer.

This capability depends on ION’s forecasting, pacing, and optimization infrastructure being fully operational and reliable. The Forecasting Sandbox serves as the externalized planning interface to ION’s delivery intelligence.

#### Value for our Business

The ION Forecasting Sandbox reduces campaign risk, improves delivery predictability, and minimizes revenue slippage caused by unrealistic audience or pacing assumptions.

It increases customer confidence pre-sale, supports smarter scoping conversations, and strengthens our ability to commit to delivery timelines. By identifying overlap, saturation risk, and under-scaled audiences in advance, we improve operational efficiency and reduce reactive adjustments during live campaigns.

Over time, this becomes a strategic differentiator by positioning Impiricus not just as a delivery partner, but as a planning intelligence partner.

##### Business Drivers

Operational Efficiency, Business Growth, Innovation, & Customer Engagement

#### Value for our Customers

Customers gain transparency and predictive clarity before campaign launch. They can understand:

- Whether their target list is fully deliverable
- How much overlap exists with other active campaigns
- The optimal timing and flighting strategy
- Whether additional HCPs should be added to improve scale and engagement

This enables smarter planning, reduces campaign risk, and improves performance outcomes without trial-and-error during execution.

#### What’s In Scope

- Building a Forecasting Sandbox environment powered by ION’s forecasting engine
- Enabling upload of new and existing target lists for simulation
- Modeling projected deliverability and completion likelihood
- Identifying HCP overlap across campaigns and network saturation risks
- Recommending optimal flight windows based on delivery constraints and network dynamics
- Generating audience expansion recommendations to improve engagement and scale
- Providing clear feasibility indicators (e.g., high confidence / moderate risk / at risk)
- Creating reporting outputs usable by Sales, CS, and customers

#### What’s Out of Scope

- Real-time campaign optimization (this is a pre-launch forecasting tool)
- Replacement of ION’s core delivery engine
- Fully automated campaign creation from sandbox outputs (recommendations only in v1)
- Standalone audience segmentation product buildout
- Major rebuild of ION infrastructure (this relies on ION being operational)


### [PROD-337](https://impiricus.atlassian.net/browse/PROD-337) — ION Marketing: Predicting & Preventing HCP Opt-Outs

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 03/Mar/26 12:15 PM
- **Updated:** 05/Mar/26 4:18 PM

**Description**

#### Overview

This work focuses on publishing thought leadership materials explaining how Impiricus leverages data and AI to predict and proactively reduce HCP opt-out behavior.

This body of work will articulate how ION uses engagement signals, behavioral insights, and delivery intelligence to improve content relevance and reduce disengagement risk. The goal is to position Impiricus as a responsible, data-driven steward of HCP attention.

#### Value for our Business

Demonstrating our ability to predict and mitigate opt-outs reinforces our commitment to long-term Network Health which is a key competitive advantage.

This narrative differentiates Impiricus from volume-based delivery platforms and strengthens trust with customers concerned about fatigue, compliance risk, and diminishing engagement quality.

It also supports Sales by framing ION not just as a performance engine, but as a sustainability engine for HCP engagement.

##### Business Drivers

Customer Engagement & Innovation

#### Value for our Customers

Customers gain confidence that their campaigns are being delivered in a way that protects long-term access to HCPs.

Understanding how opt-out risk is modeled and mitigated helps brands see that relevance and respect for provider attention are built into the delivery system. This improves trust and reinforces Impiricus as a partner focused on durable engagement, not short-term volume.

#### What’s In Scope

- Publishing research on behavioral indicators correlated with opt-out risk
- Explaining how engagement data informs relevance optimization
- Communicating high-level methodologies for predicting disengagement trends
- Sharing case studies demonstrating improved retention or reduced opt-outs
- Establishing a repeatable process for translating network health insights into public-facing thought leadership

#### What’s Out of Scope

- Disclosure of proprietary modeling techniques or sensitive internal thresholds
- Sales collateral creation
- Internal technical documentation
- Public release of raw data or sensitive performance benchmarks


### [PROD-338](https://impiricus.atlassian.net/browse/PROD-338) — ION Marketing: ION Bidding Algorithm Overview

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-08-01","end":"2026-08-31"}
- **Project target:** {"start":"2026-11-01","end":"2026-11-30"}
- **Created:** 03/Mar/26 12:18 PM
- **Updated:** 03/Mar/26 12:21 PM

**Description**

#### Overview

This work focuses on publishing a high-level, non-proprietary overview of the ION Bidding Algorithm and how it prioritizes delivering valuable, relevant content to HCPs.

As ION introduces more sophisticated optimization and decisioning capabilities, it is important to clearly communicate the philosophy and structure behind our bidding approach to showcase how we’re continually innovating with AI.

#### Value for our Business

Providing transparency into the ION Bidding framework positions Impiricus as an AI-forward, intelligent delivery platform rather than a static scheduling engine.

It builds credibility in competitive sales cycles, supports enterprise conversations, and reinforces the perception that ION operates with deliberate, science-backed logic.

This strengthens market differentiation while protecting proprietary advantages.

##### Business Drivers

Innovation & Customer Engagement

#### Value for our Customers

Customers gain clarity into how campaign delivery decisions are made and how relevance is prioritized within the system.

Understanding the principles behind the bidding approach increases trust in optimization decisions and reinforces confidence that campaigns are competing and pacing in a fair, performance-driven environment.

#### What’s In Scope

- Publishing a high-level explanation of ION’s bidding philosophy
- Explaining how relevance, engagement likelihood, pacing, and network health factor into prioritization
- Communicating guardrails that protect fairness and campaign objectives
- Developing diagrams or conceptual frameworks (non-technical) to explain decision logic
- Creating a repeatable content strategy for ongoing algorithm updates

#### What’s Out of Scope

- Disclosure of proprietary scoring formulas, weightings, or model architecture
- Release of competitive-sensitive performance benchmarks
- Internal algorithm documentation
- Sales pitch decks or feature comparison sheets


### [PROD-345](https://impiricus.atlassian.net/browse/PROD-345) — ION 3rd Party Licensing

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Innovation
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2028-01-01","end":"2028-03-31"}
- **Created:** 03/Mar/26 2:10 PM
- **Updated:** 03/Mar/26 2:11 PM

**Description**

#### Overview

This initiative captures the strategic exploration of licensing ION’s AI intelligence and decisioning engine to third parties as a standalone capability.

Rather than limiting ION to powering delivery within Impiricus-owned channels, this initiative evaluates whether our optimization, forecasting, bidding, and relevance decisioning systems could be exposed as a licensable product that external partners integrate into their own technology stacks.

The objective is to assess the viability of evolving ION from an internal delivery engine into an *Intelligence-as-a-Service (IaaS)* platform.

This is an exploratory initiative only. There is no commitment to productizing or licensing ION at this time.

#### Value for our Business

Licensing ION could:

- Unlock high-margin, recurring SaaS-style revenue streams
- Decouple revenue growth from owned media inventory constraints
- Expand Impiricus’ influence across broader healthcare and marketing ecosystems
- Increase enterprise valuation through platform monetization
- Strengthen defensibility by embedding ION within external infrastructures

It also creates strategic optionality by enabling Impiricus to evolve from a network-centric business to a hybrid infrastructure and intelligence company.

##### Business Drivers

Business Growth & Innovation

#### Value for our Customers

Partners and enterprise clients could benefit from access to ION’s optimization intelligence within their existing ecosystems.

This would allow external platforms to leverage Impiricus’s expertise in engagement scoring, pacing optimization, bidding logic, forecasting, and relevance modeling without needing to rebuild similar capabilities internally.

For current customers, this may create opportunities for expanded integrations and broader ecosystem coordination.

#### What’s In Scope

- Evaluating productization pathways for ION components (bidding, forecasting, scoring, optimization layers)
- Defining licensing models (API access, embedded SDK, white-labeled engine, revenue share, etc.)
- Assessing technical architecture required for modularization and external API exposure
- Modeling pricing, packaging, and margin implications
- Evaluating IP protection strategies and competitive risks
- Identifying target partner profiles (agencies, media platforms, health-tech providers, etc.)
- Assessing data governance and compliance implications when deployed externally

#### What’s Out of Scope

- Immediate commercialization or public API launch
- Full separation of ION from Impiricus core delivery infrastructure
- Disclosure of proprietary algorithms or model weightings
- Strategic pivot away from owned Network monetization


### [PROD-348](https://impiricus.atlassian.net/browse/PROD-348) — ION Quantum Pricing

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Network Health, Operational Efficiency
- **Project start:** {"start":"2026-09-01","end":"2026-09-30"}
- **Project target:** {"start":"2027-01-01","end":"2027-03-31"}
- **Created:** 04/Mar/26 11:25 AM
- **Updated:** 06/Mar/26 4:25 PM

**Description**

#### Overview

This epic focuses on leveraging ION’s delivery intelligence and platform data to generate pricing insights *at the n-of-1 level* that support the Sales team during campaign planning and negotiations.

Today, pricing decisions often rely on historical norms or manual analysis. By utilizing ION’s visibility into platform demand, specialty-level supply, campaign competition, and seasonal dynamics, we can generate data-driven pricing guidance that reflects real market conditions on the platform.

These insights will help inform pricing recommendations by incorporating factors such as platform demand, HCP specialty scarcity, campaign overlap, seasonal trends, and delivery competition. The goal is not to automate pricing decisions, but to provide structured intelligence that improves pricing consistency, forecasting accuracy, and deal strategy.

#### Value for our Business

ION-powered pricing insights enable more informed and consistent pricing strategies across campaigns. By grounding pricing recommendations in platform dynamics and historical delivery performance, we can better capture market value, reduce underpricing risk, and improve overall revenue yield.

This capability also strengthens Sales enablement by equipping teams with defensible, data-backed pricing context during negotiations. Over time, this may support improved forecasting accuracy and better alignment between campaign demand and available network inventory.

##### Business Drivers

Business Growth, Operational Efficiency, & Network Health

#### Value for our Customers

Customers benefit from more transparent and consistent pricing aligned with actual platform dynamics.

Pricing informed by network supply, specialty demand, and seasonal trends helps ensure campaigns are structured realistically and delivered successfully. This can improve delivery predictability and reduce the likelihood of campaigns being under-scoped or over-constrained.

#### What’s In Scope

- Leveraging ION data to analyze platform demand and supply dynamics
- Incorporating specialty-level supply and demand signals into pricing insights
- Modeling seasonality trends that impact campaign delivery and inventory availability
- Evaluating campaign competition and platform saturation signals
- Developing pricing insight outputs that can be used by Sales during planning and negotiations
- Creating internal tools or reporting surfaces that surface these insights in a usable format
- Testing and validating the accuracy and usefulness of pricing recommendations

#### What’s Out of Scope

- Fully automated campaign pricing or dynamic pricing systems
- Changes to contractual pricing structures or rate cards
- Public disclosure of internal pricing models or algorithms
- Direct integration into external-facing client tools (initial focus is internal Sales enablement)


### [PROD-350](https://impiricus.atlassian.net/browse/PROD-350) — ION Framework for Variable Testing

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 05/Mar/26 4:22 PM
- **Updated:** 06/Mar/26 4:53 PM

**Description**

#### Overview

This epic focuses on building foundational support within ION to enable *A/B testing of delivery strategies, campaign configurations, and optimization variables*.

As ION evolves into an intelligent decisioning engine, experimentation becomes essential for validating optimization strategies and continuously improving campaign performance. This work will introduce the infrastructure required to run controlled experiments that compare different delivery approaches and measure their impact on engagement, pacing, and network health.

The A/B testing framework will allow ION to test hypotheses such as delivery timing strategies, audience selection adjustments, pacing logic, and other optimization variables. Results from these experiments will inform future improvements to the ION algorithm and broader delivery strategy.

#### Value for our Business

A/B testing enables data-driven decision-making and accelerates the development of ION’s optimization capabilities. Rather than relying solely on theoretical improvements, we can validate changes through controlled experimentation before rolling them out broadly.

This reduces risk when introducing algorithm changes, improves the quality of optimization decisions, and allows the platform to continuously learn from real campaign performance.

##### Business Drivers

Innovation

#### Value for our Customers

Customers benefit from campaigns that are continuously optimized using validated improvements rather than assumptions.

The ability to test and measure different delivery strategies ensures that ION evolves based on real-world engagement patterns, leading to better performance outcomes and more reliable campaign optimization over time.

#### What’s In Scope

- Building infrastructure to support controlled A/B experiments within ION
- Enabling campaign traffic or audience splits between test and control groups
- Defining experiment configuration and eligibility rules
- Supporting testing of delivery variables (e.g., timing strategies, pacing logic, audience expansion approaches)
- Collecting and analyzing experiment performance metrics
- Establishing frameworks to evaluate experiment outcomes and determine winning strategies

#### What’s Out of Scope

- Client-facing A/B testing configuration tools in the initial phase
- Full experimentation platform development beyond ION delivery optimization
- Public disclosure of internal experimentation methodologies
- Non-delivery related experimentation across unrelated product areas


### [PROD-129](https://impiricus.atlassian.net/browse/PROD-129) — Independent Initiatives - HCP Peer Zoom Network

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement, Innovation
- **Created:** 20/Aug/25 10:26 AM
- **Updated:** 10/Dec/25 2:13 PM

**Description**

Testing capabilities to provide additional content outside of branded, MLR content. This is an education initiative to gather physicians so they can develop a peer network and discuss relevant condition and experiences, or learn more about a particular condition that is tied to Ascend clients.

Discussing if we setup these types of activities ourselves (hire a team) or if we source to 3rd party

- Scoping with Pemazyre
  - Currently, we are internally setting up a Zoom panel as a test
- Osama chatted with this group as well as 3rd party options
  - [https://precisca.com/events](https://precisca.com/events|smart-link)


### [PROD-131](https://impiricus.atlassian.net/browse/PROD-131) — Independent Initiatives - Community / Academic Bridge MVP Pemazyre

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Created:** 20/Aug/25 10:27 AM
- **Updated:** 10/Dec/25 2:14 PM

**Description**

- This is not yet well defined and requires further thought, but ultimately it refers to a mechanism for connecting community oncologists (those working in distributed, non-specialized practices) with academic oncologists (those working at academic institutions that specialize in research and advanced care) through some form of product or initiative.


### [PROD-246](https://impiricus.atlassian.net/browse/PROD-246) — Independent Initiatives - AI Voice Survey NEEDS DETAIL

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Created:** 09/Dec/25 4:55 PM
- **Updated:** 09/Dec/25 4:55 PM

**Description**

#### Overview

TBD

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-247](https://impiricus.atlassian.net/browse/PROD-247) — Independent Initiatives - Other NEEDS DETAIL

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Created:** 09/Dec/25 5:01 PM
- **Updated:** 10/Dec/25 2:14 PM

**Description**

#### Overview

TBD

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-77](https://impiricus.atlassian.net/browse/PROD-77) — CS & Sales Automation (RFP, Mock Tools)

- **Initiative:** Internal Automation
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency
- **Created:** 18/Jul/25 1:21 PM
- **Updated:** 09/Dec/25 8:56 PM

**Description**

### 🚀 Opportunity Statement

> Transform problems into opportunities to improve people’s experiences

#### Problem context

_Describe the background or current situation that reveals the problem or unmet need._

_Example: Users are unable to provide feedback quickly and easily, leading to dissatisfaction and reduced engagement_

#### Impact

_Describe how the problem affects the customer experience. Highlight how it impacts the business objectives._

_Example:_ _This issue results in fewer feedback submissions, making it difficult to gather user insights for improvement. This results in slower iterations, affecting overall customer retention_

#### Desired outcome

_Define what success looks like if this problem is solved, using measurable metrics where possible._

_Example: A streamlined feedback submission process would increase the feedback submission rate by 30% and lead to faster product iterations_

*Resources (add your own):*

- 📝 *PRD/spec*
- 📹 *Loom* *Video*
- 👩‍🎨 *Design file*


### [PROD-260](https://impiricus.atlassian.net/browse/PROD-260) — Network Coverage

- **Initiative:** Network Coverage
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-07-01","end":"2025-07-31"}
- **Project target:** {"start":"2028-06-01","end":"2028-06-30"}
- **Created:** 10/Dec/25 9:09 AM
- **Updated:** 03/Mar/26 12:37 PM

**Description**

#### Overview

This evergreen initiative focuses on protecting, growing, and sustaining our HCP network by expanding reach, improving engagement quality, and strengthening ongoing relationships. It includes adding new HCPs to the Network, re-engaging low disposition portions of the network, and optimizing relationship logic to ensure longterm network health.

#### Value for our Business

A larger and more engaged HCP network enhances inventory availability, improves campaign performance, and bolsters our advantage as having the largest opted-in Network of HCPs. Sustaining network quality ensures predictable delivery, stronger client outcomes, and improved monetization opportunities.

*Business Drivers:* Network Health

#### Value for our Customers

Customers benefit from broader audience reach, more consistent campaign pacing, and increased access to high-value HCPs. A healthier network ensures better engagement quality, more responsive messaging pathways, and improved KPI outcomes across campaigns.

#### What’s In Scope

- Expanding the network by adding new phone numbers
- Developing strategies to increase engagement among low-disposition HCPs
- Executing direct outreach (e.g., in-person events, society partnerships)
- Refining relationship logic such as message frequency updates for specific specialties (i.e. oncologists)

#### What’s Out of Scope

- TBD


### [PROD-188](https://impiricus.atlassian.net/browse/PROD-188) — Staff support - app access for HCP's admin team

- **Initiative:** Prescriber
- **Priority:** Low
- **Reporter:** Abiy Kaltiso
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-10-01","end":"2026-12-31"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 12/Sep/25 4:05 PM
- **Updated:** 13/Apr/26 5:07 PM

**Description**

#### *Overview*

This initiative introduces delegated access within DocUpdate, allowing physicians to grant their office staff controlled access to the platform to perform specific tasks on their behalf. This enhancement supports team-based workflows and enables more efficient collaboration within clinical practices.

#### *Value for Our Business*

- Expands DocUpdate’s fit for multi-user clinical environments.
- Increases daily active usage across entire care teams.
- Improves retention by embedding DocUpdate into broader office workflows.

#### *Value for Our Customers*

- Enables clinical teams to work more efficiently.
- Reduces the administrative burden on physicians.
- Improves turnaround time for office-driven tasks.
- Provides clearer ownership and accountability for assigned work.
- Creates a more scalable workflow as practices grow.

#### *What’s In Scope*

- Creation of delegated access account types for office staff.
- Role-based permissions and access controls.
- Ability for physicians to assign specific tasks or workflows to designated staff members.
- Visibility into task ownership and activity status.
- Audit logging and security controls for delegated actions.

#### *What’s Out of Scope*

- Full enterprise identity management or SSO.
- Non-clinical staff management features (e.g., HR, scheduling, payroll).
- Broad administrative dashboards beyond delegated task visibility.
- Cross-practice staff sharing.
- No ability for staff to prescribe.


### [PROD-216](https://impiricus.atlassian.net/browse/PROD-216) — FDB Drug Database Implementation 

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Project start:** {"start":"2025-12-08","end":"2025-12-08"}
- **Project target:** {"start":"2026-02-09","end":"2026-02-09"}
- **Created:** 06/Nov/25 6:32 AM
- **Updated:** 22/Jan/26 11:59 AM

**Description**

#### *Overview*

Our current drug database (RxNorm) is not sufficient to support the premium prescribing experience we aim to deliver in the DocUpdate app. To address limitations in drug search accuracy, form/strength fidelity, and downstream pharmacy integrations, we plan to adopt First Databank (FDB) as our primary drug database. FDB will power drug search in the app and serve as the foundation for tighter integration with Surescripts and pharmacy networks.

#### *Value for Our Business*

- Enables a more robust and reliable e-prescribing infrastructure.
- Reduces prescription errors tied to incomplete or mismapped drug data.
- Unlocks future medication-driven product initiatives that require high-fidelity drug data.
- Strengthens DocUpdate’s market positioning as an enterprise-grade prescribing platform.

#### *Value for Our Customers*

- More accurate and complete drug search results.
- Clear, reliable forms, strengths, and routes of administration.
- Fewer prescribing failures and pharmacy call-backs.
- Improved confidence that prescriptions will transmit successfully to pharmacies.

#### *What’s In Scope*

- Product + Data teams confirm full field-level mapping between FDB and the data surfaced to HCPs and passed to Surescripts.
- Backend team updates existing APIs to source and transmit data from the FDB database.
- App team consumes updated APIs without UX regression.
- Completion of all required Surescripts re-certification testing to go live with the new drug database.
- Validation of downstream pharmacy data integrity post-launch.

#### *What’s Out of Scope*

- No major changes to the prescribing functionality beyond required data adjustments.


### [PROD-271](https://impiricus.atlassian.net/browse/PROD-271) — Stock and supply (Marley and Amazon)

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 12/Dec/25 10:33 AM
- **Updated:** 13/Apr/26 7:36 PM

**Description**

#### *Overview*

Integrate real-time pharmacy inventory visibility into DocUpdate by connecting to pharmacies which provide real time stocking information. The aim is to reduce prescription failures and improve clinical workflow efficiency while opening a pathway to monetization through mail-order fulfillment partners.

----

#### *Value for our Business*

- Positions DocUpdate as a smarter, more reliable prescribing platform by eliminating one of the biggest pain points for clinicians and patients: pharmacies being out of stock for the prescribed medication.
- Drives user growth and retention by solving a real operational workflow challenge.
- Creates a natural monetization path through mail-order pharmacy partnerships or referral models.
- Differentiates DocUpdate from other prescribing tools that lack pharmacy intelligence or availability insights.
- Generates valuable inventory and fulfillment data that can inform future feature development and commercial strategy.

----

#### *Value to our Users*

- Provides upfront insight into medication availability—reducing frustration for both clinician and patient when a pharmacy is out of stock.
- Improves patient experience by shortening time to therapy and reducing back-and-forth with pharmacies.
- Gives clinicians confidence that prescriptions will be filled successfully on the first attempt.
- Supports more streamlined care delivery, strengthening trust in DocUpdate as a prescribing companion.

----

#### *What’s in Scope*

- Integration with pharmacies which provide real-time stock information to obtain real-time or near-real-time drug availability. (Known such pharmacies are Amazon and Marley/Curahealth)
- Displaying stock status within the prescribing workflow for the user’s selected pharmacy.
- Suggesting alternative pharmacies—retail or mail-order—based on availability data.
- Highlighting mail-order options when clinically appropriate and without explicit favoritism.
- UI updates within the prescription flow to show availability, recommendations, and selection options.
- Basic analytics to track stock-related issues, pharmacy conversions, and user behavior.
- Current scope is Marley Drug ONLY


### [PROD-297](https://impiricus.atlassian.net/browse/PROD-297) — Translator improvements

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-03-16","end":"2027-03-16"}
- **Project target:** {"start":"2027-05-15","end":"2027-05-15"}
- **Created:** 17/Feb/26 5:13 PM
- **Updated:** 13/Apr/26 7:23 PM

**Description**

#### *Overview*

Improvements to the Translator module based on analysis of user data

#### *Value for Our Business*

- Drives opt-in to DocUpdate and usage of the app for HCPs 

#### *Value for Our Customers*

- Changes will make the Translator module more valuable and/or easier to use 

#### *What’s In Scope*

- TBD based on market research

#### *What’s Out of Scope*

- TBD


### [PROD-299](https://impiricus.atlassian.net/browse/PROD-299) — Prescribing API

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-11-01","end":"2027-11-30"}
- **Project target:** {"start":"2027-10-01","end":"2027-12-31"}
- **Created:** 17/Feb/26 5:45 PM
- **Updated:** 14/Apr/26 4:28 PM

**Description**

#### Overview

API with which prescribers, practices and health systems can integrate to prescribe via the DocUpdate platform outside of the DocUpdate application

#### Value for our Business

- Increased prescribing volume increases revenue potential from fees, HCP and patient communication
- As prescribers would be required to be opted-in DocUpdate users, the API would potentially expand the user base while making the platform stickier

#### Value for our Customers

- Allows HCPs to prescribe in the interface they find easiest to use
- Expanded HCP universe provides opportunities for our pharma clients to reach their targeted HCPs

#### What’s In Scope

- Creation of an API via which a third party could send a script to a pharmacy via the DocUpdate platform
- Authentication which requires that each prescriber writing via the API must be an authenticated and current DocUpdate user

#### What’s Out of Scope

- TBD


### [PROD-301](https://impiricus.atlassian.net/browse/PROD-301) — State License Validation

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-08-01","end":"2026-08-31"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 17/Feb/26 6:13 PM
- **Updated:** 13/Apr/26 1:01 PM

**Description**

#### Overview

Validate state license for HCPs using Prescriber

#### Value for our Business

- This is required by Surescripts to continue to send prescriptions via their network

#### Value for our Customers

- Allows prescribing

#### What’s In Scope

- Verifying that new prescribers have a valid state license 
- Invalidating and blocking those new prescribers who do not have a valid state liceense

#### What’s Out of Scope

- Securing or retaining copies or evidence of the state license; scope is limited to verifying that there is a license vs a trusted source


### [PROD-353](https://impiricus.atlassian.net/browse/PROD-353) — Integrate with SingleCare for generic card distribution

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-06-16","end":"2026-06-16"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 11/Mar/26 9:45 AM
- **Updated:** 13/Apr/26 5:20 PM

**Description**

#### Overview

Integrate with Singlecare to include generic Rx coupons in XML to pharmacy and SMS to patients.

#### Value for our Business

- Provides revenue from coupon redemptions

#### Value for our Customers

- Reduces medication cost for patients, thereby benefitting HCPs with better patient retention

#### What’s In Scope

- Integration with the Singlecare API
- Including returned offers (group/BIN/PCN) in XML to pharmacy
- Includng returned offers in SMS to patient

#### What’s Out of Scope

- TBD


### [PROD-358](https://impiricus.atlassian.net/browse/PROD-358) — Trial Navigator: Initial implementation of 1104 Health via API

- **Initiative:** Prescriber
- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-06-16","end":"2026-06-16"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 13/Apr/26 1:28 PM
- **Updated:** 13/Apr/26 5:20 PM

**Description**

#### Overview

Delivery of MVP for Trial Navigator product by white labeling the 1104 Health offering consisting of chat-based search for trials followed by 1104 Health supplied human support with questions and patient intake.

#### Value for our Business

- Provides an initial offering in the trial search/placement space at minimal cost to (a) test market interest in the functionality and (b) create a narrative of innovation in the space for use at conferences and in HCP acquisition.
- Provides revenue when HCPs are referred, when patients are enrolled and when patients take their first treatment. (Proposed revenue milestones from draft contracting.)

#### Value for our Customers

- For HCPs, enhanced trial search makes it easier to enroll their patients in appropriate trials. 
- HCPs may receive compensation for their time in searching for a trial and/or the time involved in transferring the patient to the trial. 

#### What’s In Scope

- Rendering the 1104 Health functionality in the DocUpdate app via the existing 1104 Health API

#### What’s Out of Scope

- Any partners other than 1104 Health
- In-house search functionality


### [PROD-191](https://impiricus.atlassian.net/browse/PROD-191) — (REMOVE) Pulse Creation and Tracking Improvements

- **Initiative:** Pulse Runner Improvements
- **Priority:** Low
- **Reporter:** Anna McDermott
- **Created:** 15/Sep/25 12:53 PM
- **Updated:** 03/Nov/25 10:07 AM

**Description**

Update as of 11/3/25

- No active ongoing work for Pulse Creation and Tracking Improvements
  - the below listed items are still things that are nice to have’s but not a priority at the momet
  - no work has been done on the below items

----

This is for general improvements to Pulse Runner, such as

- Improvements to PR UI
  - Pulse Creation Page
- Deprecating not used sections of the tool (such as AI Message Generator)
- Improving Spark message statuses like Pulse statuses
  - Pending, Paused, Expired, Done
- Improving Pulse and Spark Monitoring Dashboards
- Improving Pulse Runner Performance loading speeds
  - Messages tab loading takes a while


### [PROD-342](https://impiricus.atlassian.net/browse/PROD-342) — Direct-to-Carrier

- **Initiative:** Pulse Runner Improvements
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2027-01-01","end":"2027-03-31"}
- **Project target:** {"start":"2028-01-01","end":"2028-03-31"}
- **Created:** 03/Mar/26 1:54 PM
- **Updated:** 03/Mar/26 1:58 PM

**Description**

*NOTE:* This initiative is not an active roadmap _commitment_, it’s a placeholder for work we _may_ take on in the future.

#### Overview

This initiative captures the strategic exploration of moving toward a *Direct-to-Carrier messaging infrastructure*, reducing or eliminating reliance on third-party Message Service Providers (MSPs) such as Bandwidth and Twilio for message delivery.

Today, Impiricus depends on external partners to route and deliver SMS traffic. While this model enables scale and operational simplicity, it introduces dependency risk, margin constraints, and limited control over delivery pathways.

This initiative is exploratory in nature. There is no current commitment to build direct carrier connectivity, but this workstream exists to evaluate feasibility, cost structure, regulatory implications, operational complexity, and long-term strategic value.

#### Value for our Business

Direct-to-Carrier capabilities could provide:

- Greater control over message routing and delivery reliability
- Reduced dependency on third-party vendors
- Potential margin expansion over time
- Improved negotiation leverage with existing providers
- Enhanced visibility into delivery diagnostics and carrier-level performance

Owning delivery infrastructure would strengthen platform defensibility and reduce external concentration risk.

##### Business Drivers

Platform Integrity, Operational Efficiency, & Business Growth

#### Value for our Customers

Customers could benefit from improved delivery transparency, greater reliability, and potentially faster resolution of carrier-related issues.

Direct infrastructure control may also allow for enhanced delivery optimization and long-term stability in messaging pathways.

#### What’s In Scope

- Evaluating technical feasibility of direct carrier connectivity
- Assessing regulatory and compliance requirements (carrier agreements, messaging regulations, registration processes)
- Modeling cost structures and margin implications
- Comparing operational complexity versus MSP model
- Identifying risks (throughput management, deliverability variance, redundancy planning)
- Conducting executive-level build vs. buy analysis
- Documenting infrastructure requirements and phased implementation options

#### What’s Out of Scope

- Immediate termination of existing MSP relationships
- Full infrastructure buildout commitment
- Migration timelines or execution planning
- Contract renegotiation as part of this exploratory phase


### [PROD-343](https://impiricus.atlassian.net/browse/PROD-343) — Self-Service Deployment

- **Initiative:** Pulse Runner Improvements
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2027-10-01","end":"2027-12-31"}
- **Project target:** {"start":"2029-01-01","end":"2029-03-31"}
- **Created:** 03/Mar/26 1:59 PM
- **Updated:** 03/Mar/26 2:00 PM

**Description**

*NOTE:* This initiative is not an active roadmap _commitment_, it’s a placeholder for work we _may_ take on in the future.

#### Overview

This initiative captures the strategic exploration of building a *Self-Service Campaign Platform*, enabling clients to independently configure, launch, and manage campaigns through external-facing platform interfaces.

Today, campaign setup and deployment are supported through internal workflows and managed-service processes. A self-service model would introduce customer-facing tooling that allows brands to directly control targeting, flighting, budgeting, forecasting, and optimization inputs within guardrails defined by Impiricus.

This initiative is exploratory in nature. There is no current commitment to building a full self-service platform. The purpose is to evaluate feasibility, infrastructure requirements, operational implications, revenue model impact, and long-term strategic alignment.

#### Value for our Business

A self-service platform could:

- Increase scalability without proportional headcount growth
- Reduce operational overhead per campaign
- Expand into mid-market or lower ACV segments
- Shorten sales cycles and campaign launch timelines
- Improve margin structure over time

It also positions Impiricus as a more platform-oriented company rather than a purely managed-service partner, potentially increasing enterprise valuation multiples.

##### Business Drivers

Business Growth, Customer Engagement, & Innovation

#### Value for our Customers

Customers could gain greater autonomy, faster campaign deployment, and more transparency into delivery forecasting and performance insights.

Self-service tooling may allow brands to iterate more quickly, test new strategies, and access ION’s intelligence in a more direct and flexible way — while still benefiting from platform guardrails that protect network health and performance standards.

#### What’s In Scope

- Evaluating technical feasibility of external-facing campaign management interfaces
- Defining required user roles, permissions, and governance guardrails
- Assessing impact on ION delivery logic and forecasting systems
- Exploring pricing and packaging implications (platform vs managed-service tiers)
- Identifying operational workflows that would need automation
- Conducting build vs phased rollout analysis (internal beta → hybrid model → full self-service)
- Evaluating support, compliance, and network health safeguards required in a self-directed model

#### What’s Out of Scope

- Immediate development of a full external-facing product
- Commitment to replacing the managed-service model
- Migration timelines for existing customers
- Detailed UX/UI design execution


### [PROD-183](https://impiricus.atlassian.net/browse/PROD-183) — Update Survey & VC Response Scoring

- **Initiative:** Response Monitoring
- **Priority:** Low
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health, Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2026-04-01","end":"2026-04-30"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 08/Sep/25 3:57 PM
- **Updated:** 04/Mar/26 3:43 PM

**Description**

#### Overview

This epic focuses on updating how *Survey and Virtual Coordinator (VC) responses are scored* within our engagement tracking systems. Currently, multiple inbound messages from the same HCP during a survey or VC interaction may be scored as separate engagement events. This can artificially inflate engagement signals and distort how HCP responsiveness is interpreted.

The goal of this work is to *score only the first inbound message associated with a survey or VC interaction* and ignore subsequent inbound messages for scoring purposes. This change will ensure engagement signals more accurately reflect meaningful participation rather than conversational follow-up messages.

By refining this scoring logic, we improve the integrity of engagement data that feeds into optimization systems, network health monitoring, and reporting.

#### Value for our Business

Accurate response scoring is foundational to maintaining the reliability of engagement signals used across the platform. By preventing multiple messages from being scored within a single interaction, we ensure behavioral data more accurately reflects true HCP engagement.

Improving scoring accuracy strengthens downstream systems that rely on these signals, including delivery optimization, engagement analysis, and network health monitoring. It also prevents inflated engagement metrics that could misinform decision-making.

##### Business Drivers

Platform Integrity, Network Health, & Operational Efficiency

#### Value for our Customers

Customers benefit from more accurate campaign performance insights and engagement reporting. Ensuring that interactions are scored consistently helps maintain trust in reported engagement metrics and ensures optimization systems are prioritizing true participation signals.

More reliable engagement data ultimately supports better targeting decisions and improved campaign outcomes.

#### What’s In Scope

- Updating scoring logic so only the *first inbound message* within a survey or VC interaction is scored
- Ensuring subsequent inbound messages tied to the same interaction are not scored as additional engagement events
- Updating response classification rules to properly identify survey and VC interaction boundaries
- Validating scoring changes against existing engagement tracking systems
- Ensuring downstream reporting and analytics continue to function correctly with the updated scoring behavior

#### What’s Out of Scope

- Changes to how surveys or VC interactions are initiated or delivered
- Redesign of the broader engagement scoring framework
- Modifications to response scoring outside of survey and VC contexts
- Public-facing changes to reporting formats or campaign metrics

*Notes around initial conversation* [*here*](https://docs.google.com/document/d/16m3uT6oFkmmq468_V7JV1fYeYkY1A8JbG35lrLNa8oQ/edit?tab=t.0#heading=h.7fjieckdagug)*.*


### [PROD-333](https://impiricus.atlassian.net/browse/PROD-333) — RightChannel Device Graph

- **Initiative:** RightChannel
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Innovation, Network Health
- **Project start:** {"start":"2026-10-01","end":"2026-12-31"}
- **Project target:** {"start":"2027-10-01","end":"2027-12-31"}
- **Created:** 03/Mar/26 11:24 AM
- **Updated:** 03/Mar/26 11:27 AM

**Description**

#### Overview

This initiative creates an *Impiricus Device Graph* to power *RightChannel’s multi-channel expansion* by enabling deterministic identification of HCPs across channels. Today, identity is often channel-specific, limiting our ability to recognize the same HCP as they engage through different endpoints.

The Device Graph will collect and reconcile multiple identifiers across channels into a unified identity layer so we can confidently map interactions back to a single HCP profile. This becomes foundational infrastructure for cross-channel orchestration, measurement, and optimization within RightChannel.

#### Value for our Business

A deterministic Device Graph unlocks scalable multi-channel growth by enabling RightChannel to expand beyond single-channel delivery without losing identity continuity. It improves the efficiency of spend and inventory by reducing duplicated outreach, strengthening frequency management, and enabling more accurate attribution and reporting.

It also provides a durable platform capability that compounds over time: every new channel integration becomes easier, measurement becomes more credible, and optimization becomes more powerful because identity resolution is consistent across the ecosystem.

##### Business Drivers

Business Growth, Innovation, & Network Health

#### Value for our Customers

Customers benefit from coordinated, consistent HCP engagement across channels—fewer redundant touches, improved sequencing, and better experience alignment.

A deterministic identity layer also improves cross-channel measurement and attribution, increasing customer confidence in performance reporting and making it easier to understand which combinations of channels and messages drive engagement.

#### What’s In Scope

- Defining the identity strategy and requirements for deterministic HCP matching across channels
- Identifying and supporting key identifier types used across channels (e.g., hashed identifiers, device identifiers, platform IDs, channel-specific IDs)
- Designing the Device Graph data model and linking logic (identity nodes, edges, confidence rules, provenance)
- Building ingestion pipelines to collect and normalize identifiers from existing and new channels
- Implementing deterministic matching rules and identity stitching to a unified HCP profile
- Establishing governance and auditability (lineage, reason codes, match transparency)
- Enabling downstream consumption by RightChannel (targeting, orchestration, reporting)
- Defining privacy/security guardrails and access controls appropriate for identity infrastructure

#### What’s Out of Scope

- Purely probabilistic identity resolution as a primary approach in v1 (deterministic-first)
- Cross-device consumer-style tracking approaches that rely on third-party cookies as a core dependency
- Channel expansion work that does not require identity stitching (this epic focuses on the identity layer)
- Full rebuild of existing HCP master data systems (integration-focused, not replacement-focused)


### [PROD-336](https://impiricus.atlassian.net/browse/PROD-336) — RightChannel Network Coverage

- **Initiative:** RightChannel
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Innovation, Network Health
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 03/Mar/26 12:05 PM
- **Updated:** 03/Mar/26 12:06 PM

**Description**

#### Overview

This (will be an evergreen) initiative focuses on expanding and strengthening Impiricus’ *RightChannel identity coverage* by acquiring and maintaining multi-channel identifiers beyond phone numbers (e.g., email addresses, cookies, device IDs, physical addresses, and other channel-specific identifiers).

As RightChannel expands into multi-channel engagement, deterministic identity coverage becomes foundational infrastructure. This initiative ensures we can recognize, reach, and coordinate engagement with HCPs across channels outside of SMS.

The goal is to systematically increase multi-channel addressability, improve identifier match rates, and maintain the quality and integrity of our cross-channel identity graph to support scalable RightChannel growth.

#### Value for our Business

Expanding multi-channel identifier coverage increases monetizable reach across RightChannel offerings and strengthens our ability to deliver coordinated, cross-channel campaigns.

Improved identity resolution enhances targeting precision, frequency management, measurement accuracy, and attribution reliability. It also increases available inventory across channels and strengthens our competitive positioning as a true deterministic healthcare identity platform.

Sustained identifier coverage ensures long-term scalability as we introduce new channel integrations.

##### Business Drivers

Network Health, Business Growth, & Innovation

#### Value for our Customers

Customers benefit from broader and more consistent cross-channel reach within a unified HCP identity framework.

Stronger identifier coverage enables coordinated messaging, reduced duplication across channels, improved attribution transparency, and more seamless multi-channel engagement strategies. This improves campaign effectiveness and provides greater confidence in performance reporting.

#### What’s In Scope

- Expanding deterministic identifier collection beyond phone numbers (emails, cookies, device IDs, physical addresses, platform-specific IDs, etc.)
- Improving match rates between identifiers and existing HCP profiles
- Building ingestion and normalization pipelines for new identifier types
- Strengthening data governance and identity hygiene processes
- Monitoring identifier coverage metrics (coverage %, match confidence, decay rates)
- Supporting new channel integrations that require additional identifier types
- Implementing processes to refresh and maintain identifier validity over time

#### What’s Out of Scope

- Net-new HCP acquisition initiatives unrelated to multi-channel identifiers
- Probabilistic-only identity modeling approaches as a primary strategy
- Development of standalone consumer identity products
- Rebuilding the core HCP master database (integration-focused, not replacement-focused)


### [PROD-344](https://impiricus.atlassian.net/browse/PROD-344) — Commercializing Audiences through 3P Data Marketplace

- **Initiative:** RightChannel
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2028-04-01","end":"2028-06-30"}
- **Created:** 03/Mar/26 2:03 PM
- **Updated:** 05/Mar/26 4:21 PM

**Description**

#### Overview

This initiative captures the strategic exploration of commercializing Impiricus’ first-party (1P) HCP audience data through third-party data marketplaces such as LiveRamp.

Impiricus has built a large, high-quality opted-in HCP Network with rich engagement signals. This initiative evaluates whether and how portions of our deterministic, privacy-compliant audience data could be monetized outside of native Impiricus campaigns through approved marketplace partnerships.

The objective is to assess the viability of extending our audience value into external ecosystems while maintaining strict governance, privacy safeguards, and brand protection.

This is an exploratory initiative only. There is no current commitment to launching marketplace distribution.

#### Value for our Business

Commercializing 1P audiences externally could:

- Unlock incremental revenue streams independent of managed campaigns
- Increase monetization yield per HCP
- Expand brand awareness within broader programmatic and identity ecosystems
- Strengthen strategic positioning as a premium healthcare identity provider
- Diversify revenue sources beyond core campaign delivery

It also creates optionality — enabling Impiricus to participate in broader data infrastructure conversations without committing to a full pivot in business model.

##### Business Drivers

Business Growth

#### Value for our Customers

Customers could benefit from extended reach of Impiricus audiences beyond our owned channels, potentially enabling omnichannel continuity in approved ecosystems.

However, strict governance would be required to ensure this does not dilute exclusivity, create competitive conflicts, or impact network experience. The guiding principle would be controlled, compliant value expansion and not open data distribution.

#### What’s In Scope

- Evaluating partnership models with platforms such as LiveRamp
- Assessing compliance, consent, and privacy implications
- Defining what audience segments (if any) would be eligible for commercialization
- Modeling revenue potential and margin structure
- Evaluating brand, exclusivity, and customer perception risks
- Designing governance frameworks for controlled distribution
- Exploring technical requirements for secure onboarding and identity resolution

#### What’s Out of Scope

- Immediate launch of 1P audience sales through marketplaces
- Unrestricted resale of HCP data
- Sharing proprietary engagement signals or sensitive optimization data
- Repositioning Impiricus as a pure data broker


### [PROD-124](https://impiricus.atlassian.net/browse/PROD-124) — Modular Integrations - Samples Pilot (QPharma Axsome)

- **Initiative:** Sample Integrations
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2025-10-01","end":"2025-10-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 20/Aug/25 10:24 AM
- **Updated:** 10/Mar/26 5:01 PM

**Description**

#### Overview

Goal - Brands have reported that HCPs accessing samples is clunky, poor experience and often leads to HCP frustration and HCP drop off

- Today sample closets are managed by 3rd parties, HCPs have to manage login/password for sample closets to order samples - big drop off point
- we want to solve this clunky workflow for HCPs by integrating directly with samples vendors and enabling an easier experience via SMS, either through Pulse 
- We are currently scoping an Ascend samples integration with Sanofi LOE and RxS, who has been recently acquired by Medvantx
- *This ticket is specifically for launching the first brand integration with QPharma for Axsome Symbravo.*

#### Value for our Business

- it’s a win-win
  - drives engagement for us
  - drives sample volume for our clients and for the sample partners
  - we are not competing with the sample closets, we’re adding another channel for them to get more business
- when we establish the partnership with each sample closet
  - then turning on additional brands becomes a configuration and lower lift
- also helps on DocUpdate side, where we can drive more business for ourselves and in turn the sample closet vendors by making it easy for HCPs to order multiple samples at one timeValue for our Customers

#### What’s In Scope

- Impiricus launches VC SMS for Axsome Symbravo
- HCP replies back with request for samples
- VC categorizes HCP response as “sample”
- This initiates sample integration workflow with Medvantx for singular brand
  - We ask HCP for NPI
  - HCP returns an NPI
*** We call our NPPES API to confirm the NPI provided is a valid NPI (not validating that the phone number/ NPI we have on file matches the NPI the HCP provided)
*** then we pull all info needed for QPharma eligibility check
*** post to QPharma api for eligiblity
*** they return back if HCP is eligible or not
**** if eligible, QPharma returns back the QPharma sample order form link
**** if not eligible, we send HCP a message letting them know with X reason
*** if eligible, then we send them the QPharma sample order form link
**** Once HCP clicks on link, we send them a 6 digit OTP (from a new number)
**** on sample order form link, HCP enters 6 digit OTP
**** HCP enter or selects their shipping address 
**** HCP electronically signs for samples
*** HCP then receives order updates via SMS
*** note this whole SMS sample flow (besides the OTP) happens within same number as VC

#### What’s Out of Scope

- for pilot, out of scope
  - channel partnership

----

*Update as of 10/31/25*

- 2 Integrations in progress with channel partners
  - RxS (Medvantx) - Sanofi Toujeo [https://miro.com/app/board/uXjVJBJqVAM=/](https://miro.com/app/board/uXjVJBJqVAM=/|smart-link) 
*** timing est Q1 2026
  - QPharma - Axsome (Symbravo first, but Auvelity and Sunosi to follow) [https://miro.com/app/board/uXjVJ3CgP3c=/](https://miro.com/app/board/uXjVJ3CgP3c=/|smart-link)
*** timing est Jan 2026
- Miro flows essentially complete with both partners, driving towards consistent DocUpdate flow across all vendors so an HCP order samples via SMS doesn’t have a different experience if it’s RxS as sample closet or QPharma, etc
  - Updated commercial slides demonstrating Impiricus flow
  - [https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28](https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28|smart-link) 
- Joe working on broader level channel partnerships for DocUpdate side
- goal is to develop one technical architecture that can support singular brand sample orders via Ascend VC as well as multiple sample checkouts via DocUpdate 

----

Goal - Brands have reported that HCPs accessing samples is clunky, poor experience and often leads to HCP frustration and HCP drop off

- today sample closets are managed by 3rd parties
- we want to solve this clunky workflow for HCPs by integrating directly with samples vendors and enabling an easier experience via SMS, either through Pulse 
- We are currently scoping an Ascend samples integration with Sanofi LOE and RxS, who has been recently acquired by Medvantx
- Also in parallel, Joe Jackson to scope a broader samples strategy for impiricus with top samples vendors (notes below)

Ascend Samples Comml Slides

[^Copy of Impiricus Sample Request message performance.pdf]

Anna folder with RxS integration proposal and screenshots

[https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link](https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link|smart-link) 

9.2.25 Notes from Joe Samples kickoff (Docupdate samples + Ascend)

- largest 2 samples closet
  - knipper - dont entertain channel partners
*** they have a target list - land dr hashmi on their website or channel partner
  - in docupdate app
  - they have an iframe, import our UI
- knipper interested in us
- could lauren get a superuser login?
  - sales reps may already have this - ability to act on behalf of HCPs
- sandy's understanding - veeva doesnt have a samples interface, just used to count how many samples are sent out
- co build something with knipper
- knipper controls more of market, cardinal is larger
- ascend partnerships in near term will drive more volume than docupdate samples
- whatever plugs into ascend will drive volume
- samples are a cost center for brands;
- if we can find 3 brands that use knipper
- todd sync with sales on who would be the ideal partners
- get Joe involved to lead RxS side

####


### [PROD-241](https://impiricus.atlassian.net/browse/PROD-241) — Modular Integrations - Samples Pilot (Medvantx) 

- **Initiative:** Sample Integrations
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2025-08-01","end":"2025-08-31"}
- **Project target:** {"start":"2026-03-01","end":"2026-03-31"}
- **Created:** 09/Dec/25 4:16 PM
- **Updated:** 26/Feb/26 9:03 AM

**Description**

#### Overview

Goal - Brands have reported that HCPs accessing samples is clunky, poor experience and often leads to HCP frustration and HCP drop off

- Today sample closets are managed by 3rd parties, HCPs have to manage login/password for sample closets to order samples - big drop off point
- we want to solve this clunky workflow for HCPs by integrating directly with samples vendors and enabling an easier experience via SMS, either through Pulse 
- We are currently scoping an Ascend samples integration with Sanofi LOE and RxS, who has been recently acquired by Medvantx
- *This ticket is specifically for launching the first brand integration with Medvantx for Sanofi Toujeo.*

#### Value for our Business

- it’s a win-win
  - drives engagement for us
  - drives sample volume for our clients and for the sample partners
  - we are not competing with the sample closets, we’re adding another channel for them to get more business
- when we establish the partnership with each sample closet
  - then turning on additional brands becomes a configuration and lower lift
- also helps on DocUpdate side, where we can drive more business for ourselves and in turn the sample closet vendors by making it easy for HCPs to order multiple samples at one time

#### Value for our Customers

same as above

#### What’s In Scope

- Impiricus launches VC SMS
- HCP replies back with request for samples
- VC categorizes responses
- initiates sample integration workflow with Medvantx for singular brand

#### What’s Out of Scope

- for pilot, out of scope
  - channel partnership 

----

*Update as of 10/31/25*

- 2 Integrations in progress with channel partners
  - RxS (Medvantx) - Sanofi Toujeo [https://miro.com/app/board/uXjVJBJqVAM=/](https://miro.com/app/board/uXjVJBJqVAM=/|smart-link) 
*** timing est Q1 2026
  - QPharma - Axsome (Symbravo first, but Auvelity and Sunosi to follow) [https://miro.com/app/board/uXjVJ3CgP3c=/](https://miro.com/app/board/uXjVJ3CgP3c=/|smart-link)
*** timing est Jan 2026
- Miro flows essentially complete with both partners, driving towards consistent DocUpdate flow across all vendors so an HCP order samples via SMS doesn’t have a different experience if it’s RxS as sample closet or QPharma, etc
  - Updated commercial slides demonstrating Impiricus flow
  - [https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28](https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28|smart-link) 
- Joe working on broader level channel partnerships for DocUpdate side
- goal is to develop one technical architecture that can support singular brand sample orders via Ascend VC as well as multiple sample checkouts via DocUpdate 

----

Goal - Brands have reported that HCPs accessing samples is clunky, poor experience and often leads to HCP frustration and HCP drop off

- today sample closets are managed by 3rd parties
- we want to solve this clunky workflow for HCPs by integrating directly with samples vendors and enabling an easier experience via SMS, either through Pulse 
- We are currently scoping an Ascend samples integration with Sanofi LOE and RxS, who has been recently acquired by Medvantx
- Also in parallel, Joe Jackson to scope a broader samples strategy for impiricus with top samples vendors (notes below)

Ascend Samples Comml Slides

[^Copy of Impiricus Sample Request message performance (afe90e7e-e1b7-48ef-b9fb-a428734e8626).pdf]

Anna folder with RxS integration proposal and screenshots

[https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link](https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link|smart-link) 

9.2.25 Notes from Joe Samples kickoff (Docupdate samples + Ascend)

- largest 2 samples closet
  - knipper - dont entertain channel partners
*** they have a target list - land dr hashmi on their website or channel partner
  - in docupdate app
  - they have an iframe, import our UI
- knipper interested in us
- could lauren get a superuser login?
  - sales reps may already have this - ability to act on behalf of HCPs
- sandy's understanding - veeva doesnt have a samples interface, just used to count how many samples are sent out
- co build something with knipper
- knipper controls more of market, cardinal is larger
- ascend partnerships in near term will drive more volume than docupdate samples
- whatever plugs into ascend will drive volume
- samples are a cost center for brands;
- if we can find 3 brands that use knipper
- todd sync with sales on who would be the ideal partners
- get Joe involved to lead RxS side

####


### [PROD-326](https://impiricus.atlassian.net/browse/PROD-326) — Modular Integrations - Samples Partnership Expansion

- **Initiative:** Sample Integrations
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 26/Feb/26 9:04 AM
- **Updated:** 26/Feb/26 9:12 AM

**Description**

#### Overview

This is the ticket to cover the expansion of the sample management partnerships and driving additional brands with current partnerships (QPharma and Medvantx). Samples drive script lift; samples ordering is clunky today; if we can provide frictionless SMS ordering via the top sample closet vendors, then we can fuel Ascend growth and improve the HCP experience. We want to setup channel partnerships so that we can plug a sample integration into the Ascend platform for any brand, any manufacturer.

#### Value for our Business

- same as above; if we can make sample ordering easier and make it available via channel partnerships, then this will boost the Ascend platform engagement offering
- Samples integration also will boost any existing channels where HCPs are asking for samples
  - VC/ SMS
  - chatbot (tbd, based on initial Gary thoughts if clients would be open to requesting samples via chatbot, to determine authentication measures).
  - email

#### Value for our Customers

- same as above
  - samples drive script lift
  - sample closet ordering for HCPs is clunky and leads to high drop off
  - if we can make this process easier for HCPs, then it’s a win win
  - this is viewed as innovative compared to current sample requesting process

#### What’s In Scope

- Based on conversations with partners and sales/clients would be to start in Q2:
  - Synergistix: JnJ (Xarelto & Symtuza) & maybe GSK Trelegy???
  - Knipper: at least one from: Phathom (Voquezna), BI (Spiriva, Stiolto), Bayer (Kerendia)
  - QPharma Potential Additions: Merck and/or BMS
  - Medvantx Potential Additions: TBD, as we just started expansion opps with them and they are eager to expand. Client overlap TBD
- The goal is to expand samples integrations and attack as follows.
  - set up channel partnerships with leading sample closets
  - set up integration at brand level (to implement via Brand VC)
*** modify configuration as needed to support HCP ordering via DocUpdate side

#### What’s Out of Scope

- Anything related to DocUpdate side of sample requesting via Concierge - the DocUpdate team handles that. This is Ascend focused.


### [PROD-113](https://impiricus.atlassian.net/browse/PROD-113) — VC Generative AI Responses

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Mike Gelber
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-09-15","end":"2026-09-15"}
- **Created:** 20/Aug/25 10:14 AM
- **Updated:** 04/Mar/26 8:43 AM

**Description**

#### Overview

This work would allow for the Virtual Coordinator (VC) to generate its own responses to HCP questions, with some built-in guardrails. 

In current state, the VC sends pre-canned, MLR-approved content based on the HCP’s message categorization. There is no content being generated by the VC that hasn’t been curated by our CS or client teams. With this work, we would allow the VC to generate its own VC response content on the fly, based on what the HCP asks for in the VC conversation. 

#### Value for our Business

This would drastically speed up delivery timelines and remove the need for our CS teams to develop and obtain approval on MLR content. Additionally, we wouldn’t need to spend as much time mapping content to categories and training the VC on how to identify certain categories; instead, we could train the VC on the brand website and let it handle message content on its own based on the HCP conversation. 

#### Value for our Customers

Expedited delivery timelines and better handling of HCP messages in cases where today we don’t have certain questions or content categories mapped / in use. 

#### What’s In Scope

- Tools to train the VC on brand content (e.g. a brand website)
- Tools to test the VC and see how it would respond to example HCP messages
- Ability to add certain guardrails to the VC (e.g. do not use profanity, maintain a professional tone, restrict responses to brand information, don’t provide medical advice, etc.)

#### What’s Out of Scope

- TBD


### [PROD-186](https://impiricus.atlassian.net/browse/PROD-186) — VC Deployed Via DocUpdate

- **Initiative:** Virtual Coordinator
- **Priority:** Low
- **Assignee:** Sam Thomas
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 12/Sep/25 1:27 PM
- **Updated:** 26/Feb/26 1:56 PM

**Description**

#### Overview

This work is focused on adding DocUpdate as another channel for Virtual Coordinator (VC) deployments. 

In current state, VCs are only available via SMS; as we expand our omnichannel offerings, we are looking to add web chatbot and other avenues (like DocUpdate) to facilitate a larger / more connected ecosystem for our HCPs. 

#### Value for our Business

We would be able to expand our omnichannel strategy and make our DocUpdate app stickier for users. This could potentially unlock further revenue streams, but more importantly it drives more connection between our already existing product offerings. 

#### Value for our Customers

For HCPs, this would provide a more robust way to organize VC activities and it would allow users to stay in one modal vs. switching between mobile app and SMS threads for different brand work. 

#### What’s In Scope

- Ability for HCPs to search for VCs by brand, specialty, indication or MOA
- Once a HCP identifies a brand VC they want to engage with, they can enter into a two-way chat with the VC and they are able to have the same experience that we currently offer via SMS

#### What’s Out of Scope

- Tailored VC deployments (e.g. deploying certain VCs to certain users)
- Continuous conversations - this will come with later roadmap work


### [PROD-202](https://impiricus.atlassian.net/browse/PROD-202) — Personalized VC Agents

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-06-01","end":"2026-06-30"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 30/Sep/25 1:29 PM
- **Updated:** 04/Mar/26 8:43 AM

**Description**

#### Overview

This work is focused on being able to provide personalized Virtual Coordinator (VC) responses to HCP messages. 

In current state, all HCPs will receive the same MLR-approved VC messaging; in future state, we want the ability to provide HCP-specific messaging when and where it makes sense (e.g. HCP asks for local coverage, contact info for their specific rep, etc.) 

#### Value for our Business

Two primary value drivers:

- Unlocks new / additional contract and revenue options
- Provides a more tailored and relevant experience for our users, which should improve our relevancy rates and reduce opt outs

#### Value for our Customers

Our users are provided with a customized VC experience that is more personal and relevant to what they want and need. The current one-size-fits-all is still better than traditional marketing techniques, but the ability to provide a custom experience enhances the stickiness of our VC solution. 

#### What’s In Scope

- Ability for the VC to provide HCP-specific resources (e.g. rep contact cards, insurance coverage, etc.) based on their geographic location

#### What’s Out of Scope

- Generative AI responses


### [PROD-205](https://impiricus.atlassian.net/browse/PROD-205) — VC - Human in the Loop

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 06/Oct/25 3:14 PM
- **Updated:** 09/Apr/26 1:37 PM

**Description**

#### Overview

This work will allow human intervention into HCP <> Virtual Coordinator (VC) conversations. 

In current state, all HCP <> VC messages are pre-canned, MLR approved content that is sent based on the way the VC interprets and categorizes the HCP’s message. If there were an instance where the VC were down, or if the VC was responding inaccurately, we want the ability for a human Impiricus team member to jump in and intervene accordingly. 

#### Value for our Business

This helps ensure high performance and accuracy in our messages sent to HCPs. If the VC is for some reason mishandling a situation, this would allow us to intervene and get things back on track - which in turn provides a better HCP experience and might save the HCP from opting out or unsubscribing. 

#### Value for our Customers

Customers would be comforted knowing that we can take over a HCP <> VC interaction in case things go awry. Human oversight and intervention strategies can help more conservative customers accept progressive AI models as part of their marketing plans. 

#### What’s In Scope

- Internal Impiricus monitoring tools to provide visibility into HCP <> VC messages
- An option for an Impiricus or authorized third party team member to temporarily take control of the conversation while pausing VC responses
- An option for an Impiricus or authorized third party team member to relinquish control of a conversation and return back to VC handling when desired
- Strict permissions to ensure only authorized Impiricus team members have access to send messages to HCPs
- Controls to ensure any human takeover is restricted to triggering of templated MLR-approved content
- Ability for human users to click a button and connect the HCP to Connect, Samples Integration, etc
- Proper logging and reporting for human in the loop activities

#### What’s Out of Scope

- 100% custom free text messaging fields for humans in control of the convo


### [PROD-278](https://impiricus.atlassian.net/browse/PROD-278) — VC Studio v2

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Reporter:** Sam Thomas
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-08-01","end":"2026-08-31"}
- **Created:** 18/Dec/25 3:48 PM
- **Updated:** 25/Feb/26 4:43 PM

**Description**

#### Overview

This work is the next iteration of [https://impiricus.atlassian.net/browse/PROD-118](https://impiricus.atlassian.net/browse/PROD-118|smart-link) .

The VC Studio is the internal tooling / admin portal for Virtual Coordinator program delivery.

#### Value for our Business

Scalability

#### Value for our Customers

Customers will realize faster implementation timelines and more flexibility in what gets built. With our current technical builds today, it can be hard to change certain VC functionality as we get close to deployment; as we move away from technical team delivery and rely more on point-and-click tooling, we will have more flexibility to make adjustments faster.

#### What’s In Scope

- VCs deployed via web chatbot
- Web chatbot config tools
- Interfaces to monitor all HCP <> VC conversations in one place, for all VCs
- TBD - “Human in the loop” takeover of HCP <> VC conversations

#### What’s Out of Scope

- Integrations with Veeva or other MLR content review / approval systems
- Impiricus team member account management / access provisioning
- SaaS usage / external client accounts
- Mobile / tablet design / performance
- Ability to trigger initial VC messages via VC Studio (this will stay in Pulse Runner for the foreseeable future)


### [PROD-279](https://impiricus.atlassian.net/browse/PROD-279) — VC Reporting v2

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Operational Efficiency
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-07-01","end":"2026-09-30"}
- **Created:** 18/Dec/25 4:46 PM
- **Updated:** 26/Feb/26 1:56 PM

**Description**

#### Overview

This work is a continuation of [https://impiricus.atlassian.net/browse/PROD-112](https://impiricus.atlassian.net/browse/PROD-112|smart-link) and is focused on finding ways to more easily and rapidly automate our VC reporting. 

The Sigma dashboards that we use are created manually, and the PLD template is time-consuming for our IMs.  With this work, we want to focus on automated reported in the VC Studio that does not require any developer or IM work to configure. 

#### Value for our Business

This will allow us to track VC performance so that we can see and articulate the value of our VC programs. This will also free up time from our data analytics and IM teams so that we can be more scalable. 

#### Value for our Customers

This will drive better read outs and will help our customers better understand the value they are getting from our VC programs. 

#### What’s In Scope

TBD - early thoughts include:

1. Ability to generate PLD reports without JSON blobs / IM teams
1. Ability to create Sigma-type views without needing our data analytics team to build them
1. More metadata and visibility into metadata for each conversation
1. New graphs to show things like:
   1. The distribution of categories
   1. Average length of conversations
   1. Engagement rates by population (e.g. HCP vs. NP vs. other)

#### What’s Out of Scope

- Customers building their own reports on an ad-hoc / on-demand basis


### [PROD-280](https://impiricus.atlassian.net/browse/PROD-280) — Conversation Context / History for VCs

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 18/Dec/25 5:27 PM
- **Updated:** 26/Feb/26 1:56 PM

**Description**

#### Overview

This work is focused on enabling more tailored / personalized HCP <> VC conversations by introducing the concept of VCs being able to recall the history of HCP messages / conversations. Additionally, this will allow us to move away from the 1:1 message model (1 message in, 1 message out) that we’ve had to date and will allow our VCs to handle stream of consciousness HCP messaging. 

#### Value for our Business

Two primary value drivers:

- Unlocks new / additional contract and revenue options
- Provides a more tailored and relevant experience for our users, which should improve our relevancy rates and reduce opt outs

#### Value for our Customers

Our users are provided with a more human-like VC experience, which is more natural to work with and can handle scenarios where the HCP wants something more than a simple agentic interaction. 

#### What’s In Scope

- Ability for the VC to:
  - Remember / recall conversation history with a HCP
  - Handle stream of consciousness messaging 

#### What’s Out of Scope

- Generative AI responses


### [PROD-281](https://impiricus.atlassian.net/browse/PROD-281) — VC <> Connect Integration

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Customer Engagement, Innovation, Operational Efficiency
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-01-01","end":"2026-03-31"}
- **Created:** 18/Dec/25 5:31 PM
- **Updated:** 26/Feb/26 1:50 PM

**Description**

#### Overview

This work allows us to integrate VCs and Connect (Rep Connect, FRM Connect, MSL Connect, etc.) programs.

Example: if a HCP is interacting with a VC and they indicate they want to be connected to a rep, the VC can hand the HCP off to a rep to kick off the Rep Connect workflows / experience. 

#### Value for our Business

We continue to become one connected ecosystem across our entire product suite, which further drives the concept of stickiness / one stop shop to keep our users and our buyers coming back to Impiricus vs looking at other solutions. This also allows us to deliver more rapidly and sustainably, where we can deliver integrated product offerings at scale. 

#### Value for our Customers

Our buyers and our users will benefit from being able to choose what they want to use in our ecosystem of products. 

#### What’s In Scope

- HCP asks the VC for a rep / FRM / MSL >> the VC initiates the Connect workflows

#### What’s Out of Scope

- TBD


### [PROD-318](https://impiricus.atlassian.net/browse/PROD-318) — VC: Add Support for Bandwidth Messaging

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Operational Efficiency, Platform Integrity
- **Project start:** {"start":"2026-04-16","end":"2026-04-16"}
- **Project target:** {"start":"2026-06-15","end":"2026-06-15"}
- **Created:** 25/Feb/26 4:45 PM
- **Updated:** 16/Apr/26 4:08 PM

**Description**

#### Overview

This work expands our ability to use different SMS messaging services for Virtual Coordinator programs. In current state, we are only able to support / use Twilio; with this work, we aim to support Bandwidth as an additional messaging service that can be used for SMS campaigns. 

#### Value for our Business

This work provides more flexibility for the business to choose the partners with services that work best for us and with us vs. being locked into certain partnerships due to product / platform limitations. 

#### Value for our Customers

N/A - no real impact for this work. 

#### What’s In Scope

- Enabling Bandwidth as a messaging service that can be used for SMS programs which contain Virtual Coordinator

#### What’s Out of Scope

- The ability to use Pulse Runner Flows with VC programs


### [PROD-319](https://impiricus.atlassian.net/browse/PROD-319) — VC: Email and SMS Notifications for VC Monitoring

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Operational Efficiency
- **Project start:** {"start":"2026-04-01","end":"2026-04-30"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 25/Feb/26 4:46 PM
- **Updated:** 08/Apr/26 1:36 PM

**Description**

#### Overview

This work allows us to better support our CS end users and the requirements they have to report certain VC activity to clients. One example: when an Adverse Event has been identified, our CS team has to report that to the client within 24 hours. 

In current state, we trigger notifications to our CS team in Slack if/when a VC categorizes something with a category that has been built to trigger these notifications (e.g. Adverse Event); with this work, we want to add the ability to send our CS team emails and SMS notifications when these trigger events occur to help provide additional visibility outside of just Slack. 

#### Value for our Business

This work allows us to better support our CS team with their client requirements for reporting. 

#### Value for our Customers

Our customers benefit by knowing that we have mechanisms in place to monitor VC activity and escalate anything that may need client attention. 

#### What’s In Scope

- Adding email and SMS channels for VC notifications

#### What’s Out of Scope

- Ability to customize notification message content


### [PROD-320](https://impiricus.atlassian.net/browse/PROD-320) — VC: Inbound Messages

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Project start:** {"start":"2026-04-16","end":"2026-04-16"}
- **Project target:** {"start":"2026-06-15","end":"2026-06-15"}
- **Created:** 25/Feb/26 4:50 PM
- **Updated:** 08/Apr/26 1:36 PM

**Description**

#### Overview

This work allows us to expand our channel offerings by enabling inbound messages to the Virtual Coordinator (VC).  

In current state, we can only support outbound messages to HCPs where HCP replies are then handled by the VC; with this work, we want to allow for inbound messages from HCPs being able to trigger VC interactions. 

An example use case for this is adding a QR code to a brand’s marketing materials and allowing HCPs to scan the QR code to get connected to a VC. 

#### Value for our Business

This work expands our channel capabilities and further contributes to our mission of empowering HCPs to choose when and how they engage with us. 

#### Value for our Customers

Customers are able to serve and reach a much larger target of HCPs as they are no longer restricted to using the HCPs that are:

1. In our network
1. At/above required demeanor and believability thresholds
1. Outside of certain message window restrictions

#### What’s In Scope

- Ability for the VC to handle inbound messages as a starting point for HCP <> VC conversations

#### What’s Out of Scope

- Ability to build custom if/then flows for each inbound channel / offering


### [PROD-322](https://impiricus.atlassian.net/browse/PROD-322) — VC: Different Content per Channel

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Assignee:** Sam Thomas
- **Reporter:** Sam Thomas
- **Value drivers:** Customer Engagement, Operational Efficiency
- **Project start:** {"start":"2026-04-16","end":"2026-04-16"}
- **Project target:** {"start":"2026-06-01","end":"2026-06-30"}
- **Created:** 25/Feb/26 5:06 PM
- **Updated:** 16/Apr/26 4:16 PM

**Description**

#### Overview

This work allows us to surface different VC messaging in different channels (e.g. the VC content we build for SMS is specific to SMS and the content we build for web chatbot is specific to web chatbot). 

#### Value for our Business

This allows us to sell more robust products that can be tailored to our clients and their use cases. A more flexible product can help us make sure we’re able to scale and support future requirements. 

Additionally, this helps us scale by allowing us to build one VC for all channels (with different content for each) vs. building a VC for each channel (which is what we have to do today, without this work). 

#### Value for our Customers

Customers get more flexibility with how the VC works and they can tailor it to their needs. They are able to provide better experiences for their targeted end users accordingly. 

#### What’s In Scope

- One VC being able to handle different VC / MLR content per each channel (e.g. SMS, web chatbot, inbound via QR codes, etc)
- Ability to handle rich messaging (primarily for web - future state RCS, MMS, etc.)

#### What’s Out of Scope

- Generative AI for VC content
- Ability to build custom flows (if/then scenarios) for each channel


### [PROD-328](https://impiricus.atlassian.net/browse/PROD-328) — MSL as front door VC Coordinator --> Connect

- **Initiative:** Virtual Coordinator
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Created:** 26/Feb/26 9:36 AM
- **Updated:** 26/Feb/26 1:04 PM

**Description**

#### Overview

[^Adapting Virtual Coordinator for Medical Affairs.pdf]

_(image: Screenshot 2026-02-26 at 9.35.44 AM.png)_

_(image: Screenshot 2026-02-26 at 9.35.49 AM.png)_

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-200](https://impiricus.atlassian.net/browse/PROD-200) — IQVIA AIM Integration

- **Initiative:** Web Chatbot
- **Priority:** Low
- **Assignee:** Sam Thomas
- **Reporter:** Brian Ongioni
- **Value drivers:** Business Growth, Innovation
- **Project start:** {"start":"2026-07-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 23/Sep/25 10:16 AM
- **Updated:** 02/Mar/26 10:37 AM

**Description**

*Update as of 10/31/25:*

- Initial call with IQVIA AIM on 9.30.25
  - call notes here [https://impiricus.atlassian.net/wiki/spaces/IPS/pages/892928012/IQVIA+AIM+Integration](https://impiricus.atlassian.net/wiki/spaces/IPS/pages/892928012/IQVIA+AIM+Integration|smart-link) 
- Key callouts
  - IQVIA AIM mentioned Ostro is not providing PLD reporting on chatbot usage
  - IQVIA AIM seeing increase in data from docupdate
*** not a lot of identity associated - assuming we are vetting these numbers belong to a doctor
  - Axsome (Vinny) mentioned he doesn’t think the data from IQVIA AIM was helpful or easy to marry to existing data
*** <10% HCP tracking on brand websites
*** looking into alternatives with deepintent 
*** Mike mentioned deep intent and iqvia aim are partners
- Product to continue to discuss business need for this integration

----

Integrate IQVIA’s AIM XR with the Impiricus Web Chatbot to enhance HCP engagements via predictive, behavior-driven insights. By leveraging AIM XR’s real-time tracking of HCP research/reading behavior, custom behavioral audiences, and trigger-based signals, the chatbot can surface more relevant content, initiate conversations at optimal moments, and follow up with tailored suggestions. 

API Documentation to come


### [PROD-101](https://impiricus.atlassian.net/browse/PROD-101) — Ascend + DocUpdate

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Intake
- **Created:** 04/Aug/25 2:48 PM
- **Updated:** 06/Nov/25 6:22 AM


### [PROD-117](https://impiricus.atlassian.net/browse/PROD-117) — Platforming - Virtual Coordinator Manager - DEMO (not doing)

- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Created:** 20/Aug/25 10:18 AM
- **Updated:** 04/Sep/25 5:08 PM

**Description**

1. Create a functional demo of the VC Manager UI

per 9.4.25 discussion - we are going to work on an MVP with real data and not go with an open ai demo


### [PROD-133](https://impiricus.atlassian.net/browse/PROD-133) — Concierge v3

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Project start:** {"start":"2025-10-16","end":"2025-10-16"}
- **Project target:** {"start":"2026-03-15","end":"2026-03-15"}
- **Created:** 21/Aug/25 9:25 AM
- **Updated:** 09/Dec/25 2:51 PM

**Description**

#### *Overview:*

Building out the Concierge section of the DocUpdate app and integrating with Zendesk SDK to improve the current workflow.

[https://www.figma.com/design/aH5agvIS1W3C2KZZTCNNBo/Docupdate---Product-Design?node-id=17618-39279&p=f&t=YF3oH5rv2JFApuwj-0](https://www.figma.com/design/aH5agvIS1W3C2KZZTCNNBo/Docupdate---Product-Design?node-id=17618-39279&p=f&t=YF3oH5rv2JFApuwj-0|smart-link) 

#### *Value for our Business:*

- Sales value: ability to list Ascend clients directly in the app 
- Drive user love
- Increase Concierge team efficiencies

#### *Value for our Customers:*

- Elevated UX/UI 
- Decreased ambiguity with the Concierge service
  - introductory tutorial
  - copy & subcopy changes for increased clarity
- More control over communication preferences
  - in-app vs SMS options
  - preferred time of day & days of week for conversations to occur

#### *What’s in Scope:*

- Zendesk SDK
  - In-app messaging
  - Ticket creation on submission
- App changes
  - Concierge Tutorial
  - Single select on requests 
*** can no longer input within multiple sections within a single submission
  - Sample drop-down lists
*** relevant products by specialty
*** mix of ascend partners, integrated items, and easy-to-access products
*** List order is randomized each time it’s accessed
*** The list should be easily edited as changes arise. Reference list: [https://docs.google.com/spreadsheets/d/1UHIYydm0emjRcAP2GwfbsQ2tvG33XPT5Ig4kXoLlETQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1UHIYydm0emjRcAP2GwfbsQ2tvG33XPT5Ig4kXoLlETQ/edit?usp=sharing|smart-link) 
  - Defined rules & restrictions
*** Practice address  & LSN required for sample request submission
*** Max 3 open tickets at once
  - E-signature consent & capture for integrated products
*** TBD: captured once or each time?
- DB changes
  - TBD

#### *What’s out of Scope:*

- Integration with CED for moving support-type requests
- Adding submission boxes for specific additional capabilities (e.g., grant opportunities, clinical trials, CEU finder, etc)


### [PROD-135](https://impiricus.atlassian.net/browse/PROD-135) — Concierge - AI for Sample Ordering

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Value drivers:** Innovation, Operational Efficiency
- **Project start:** {"start":"2026-04-15","end":"2026-04-15"}
- **Project target:** {"start":"2026-07-01","end":"2026-07-31"}
- **Created:** 21/Aug/25 11:24 AM
- **Updated:** 20/Feb/26 8:15 AM

**Description**

#### Overview

Initiative to implement AI for online submission of sample and pharma rep requests. 

#### Value for our Business

- Increase the scalability of the Concierge department
  - Decreased human time spent on sample/rep requests, and can instead increase time spent on other ways we can bring value to our users
  - Improve speed & quantity with requests, so we can better accommodate expected user growth

#### Value for our Customers

- Opportunity for faster submissions & turnaround time of their request → better user experience

#### What’s In Scope

- AI pulling user data needed to place requests (& verifying as needed)
  - Possible sources:
*** Zendesk user profile
*** NPPES
*** State website for a licensure retrieval (for SLN)
- AI places online requests (forms, request boxes, etc)
  - For a pre-determined process
*** uses clearly defined steps for how to receive the resources, just has to find and place the necessary info appropriately
  - For an undefined process
*** scrapes web for more info on product & how to request the resources
*** once a source is found, then uses collected info to place the request accordingly

#### What’s Out of Scope

- Use of AI to speak directly with manufacturer reps or personnel (via phone or email)


### [PROD-137](https://impiricus.atlassian.net/browse/PROD-137) — Concierge as Brand-agnostic MSL

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 21/Aug/25 11:47 AM
- **Updated:** 13/Feb/26 4:41 PM

**Description**

#### Overview

Idea for a Concierge offering that would act as an on-demand, virtual MSL across any brands' HCPs are requesting. 

#### Value for our Business

- Selling potential with pharma clients: 
  - They could provide their articles & info into our data pool
  - We could feed gathered insights back to brands
- Potential driver for new DocUpdate users & use cases from specialty areas beyond our usual users

#### Value for our Customers

- Another free tool in their pocket
- Demonstrated desire from Concierge users (e.g., requests for clinical trial info, off-label use of medications, recent clinical findings in specific treatment areas, etc).

#### What’s In Scope

- An in-app tool that operates like a true MSL by:
  - providing education on drugs, disease states, and the latest clinical data
  - answers complex questions without selling a product
  - support clinical trials 
- Fully AI-backed?
  - TBD: controlling what is feeding the AI & what sources it pulls from
- Ability to escalate to a Concierge agent & be connected with a real MSL

#### What’s Out of Scope

- Offering medical advice
- Anything not MLR compliant


### [PROD-138](https://impiricus.atlassian.net/browse/PROD-138) — Additional Concierge Channels

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Project start:** {"start":"2026-07-01","end":"2026-07-31"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 21/Aug/25 11:52 AM
- **Updated:** 13/Feb/26 4:41 PM

**Description**

#### Overview

Discussed at 8/18/25 Product summit, as a way for our Ascend  clients to utilize the Concierge service and form deeper connections with our DocUpdate users.

#### Value for our Business

Opportunity for Ascend clients to have more direct access to our HCPs & benefit from the user-love we’re building.

#### Value for our Customers

Our HCPs should then also have easier access to our pharma partners (but on their own terms). Can provide our HCPs with more opportunities to be involved with pharma (via events, surveys, etc).

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-139](https://impiricus.atlassian.net/browse/PROD-139) — General Sample Basket

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 21/Aug/25 11:53 AM
- **Updated:** 13/Feb/26 4:41 PM

**Description**

#### Overview

For users new to Concierge, this offer would allow them to receive a “general sample basket” of products relevant to their specialty that they are eligible for. 

_This must be given a compliance green flag first_

#### Value for our Business

- Increase DocUpdate user love
- Additional driver for users to try Concierge

#### Value for our Customers

- Many users come to Concierge for the first time, asking “What kind of samples can I get?” or saying that they’d like access to all samples they’re able to get - this would largely simplify the process and match what these users are looking for in a sample provider
- Would provide simplified access to multiple samples at once 

#### What’s In Scope

- Offering access to multiple samples that HCPs are eligible for, all at once
- Meets MLR requirements
  - TBD: Could we use purchasable samples & OTC items without compliance issues?

#### What’s Out of Scope

- DocUpdate stocks or distributes the products directly


### [PROD-161](https://impiricus.atlassian.net/browse/PROD-161) — Concierge Biologic Coordinator MVP Phone Line for BCoD

- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Project start:** {"start":"2025-08-16","end":"2025-08-16"}
- **Project target:** {"start":"2025-07-01","end":"2025-09-30"}
- **Created:** 27/Aug/25 11:56 AM
- **Updated:** 15/Sep/25 6:19 PM

**Description**

Anticipated workflow:

- BCs scan QR code at RAN/BCoD 
- They are directed to a Jotform for intake
  - Full name
  - Phone number
  - Email (optional as back up for number)
  - Practice name & address
  - Practice Specialty
  - Their request
- HCP Coordinators reach out via BC OpenPhone line to complete the request


### [PROD-162](https://impiricus.atlassian.net/browse/PROD-162) — Concierge - AI Biologic Coordinator/Prior Auth Facilitation

- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 27/Aug/25 11:57 AM
- **Updated:** 20/Feb/26 8:15 AM

**Description**

#### Overview

Tool to assist HCPs & their patients with access to biologics. 

Current barriers for patients include PA processes & timelines for approval, delaying patient care. This then falls on HCPs, BCs, and office staff to coordinate back & forth with insurance to complete PAs, appeals, and work with pharma manufacturers to discover co-pay, savings cards, or bridge options to help get patients access faster. 

We’d like to help alleviate this burden in the current healthcare system. 

Detailed workflow from Product Summit: [https://docs.google.com/document/d/1g1K8XJA5QL3z-7FIhS9WASmW1U4hqAt9CCxusy2iW_o/edit?tab=t.0](https://docs.google.com/document/d/1g1K8XJA5QL3z-7FIhS9WASmW1U4hqAt9CCxusy2iW_o/edit?tab=t.0|smart-link) 

Nov F2F brainstorming:

_(image: image-20251210-150637.png)_

#### Value for our Business

- Increased DocU brand recognition across HCPs & Practices
  - “DocUpdate Non-Dispensing Pharmacy” would live inside EHRs

#### Value for our Customers

- Huge value add for frequent prescribers of these items (especially Derms & Rheums)
- Users have already demonstrated a desire for PA assistance 

#### What’s In Scope

- DU non-dispensing pharmacy
  - integrated with EHR/EMR 
*** HCPs can send prescriptions directly
*** Access to the necessary files for PA & appeals
- Platform for AI writing of PA & Appeals
- Additional resource allocation/pivot to Concierge?
  - Co-pay/savings options
  - bridge programs/samples
  - connect with a rep

#### What’s Out of Scope

- Patient notifications / Direct communication with patients?


### [PROD-170](https://impiricus.atlassian.net/browse/PROD-170) — enhancements to referral program

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2025-01-01","end":"2025-01-31"}
- **Created:** 05/Sep/25 3:24 PM
- **Updated:** 05/Sep/25 5:13 PM


### [PROD-173](https://impiricus.atlassian.net/browse/PROD-173) — Continuing Education credits 

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Created:** 05/Sep/25 3:27 PM
- **Updated:** 05/Sep/25 3:50 PM


### [PROD-174](https://impiricus.atlassian.net/browse/PROD-174) — App tour

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2025-02-01","end":"2025-02-28"}
- **Created:** 05/Sep/25 3:29 PM
- **Updated:** 05/Sep/25 4:44 PM


### [PROD-178](https://impiricus.atlassian.net/browse/PROD-178) — AI conversational prescribing

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Created:** 05/Sep/25 3:46 PM
- **Updated:** 05/Sep/25 3:46 PM


### [PROD-184](https://impiricus.atlassian.net/browse/PROD-184) — QA app logging

- **Priority:** Low
- **Reporter:** Abiy Kaltiso
- **Created:** 11/Sep/25 2:28 PM
- **Updated:** 11/Sep/25 2:28 PM


### [PROD-203](https://impiricus.atlassian.net/browse/PROD-203) — Oncologist-Focused Concierge Product

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Project start:** {"start":"2026-03-01","end":"2026-03-31"}
- **Project target:** {"start":"2026-12-01","end":"2026-12-31"}
- **Created:** 01/Oct/25 2:34 PM
- **Updated:** 30/Jan/26 10:18 AM

**Description**

#### Overview

This will be a DocUpdate product designed to provide value to Oncologists and further drive user love. 

#### Value for our Business

- Unlock a new set of users who would use/love DocUpdate
- A larger network of opted-in Oncs holds high sales value with our pharma clients

#### Value for our Customers

- Opportunity to solve a problem and provide value to additional HCPs
- Likely to be added value across all users (another free tool for all)

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-208](https://impiricus.atlassian.net/browse/PROD-208) — Rep Connect Improvement Ideas

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Created:** 09/Oct/25 4:11 PM
- **Updated:** 09/Oct/25 4:11 PM

**Description**

Another thought for future of rep connect is how do we support rep contacting that other number via rep connect

_(image: Screenshot 2025-10-09 at 1.51.30 PM.png)_


### [PROD-211](https://impiricus.atlassian.net/browse/PROD-211) — Surface cash price of medications in app

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Created:** 24/Oct/25 11:36 AM
- **Updated:** 06/Nov/25 6:27 AM

**Description**

1. Medication cash pricing
   1. users want to see branded medication cash pricing when they load up the medication
##### We frame this like "brought to by Concierge". Discuss with Joe doing an integration with RxLink where we can say "concierge can give you access to these savings offers for your patient for this medication”


### [PROD-212](https://impiricus.atlassian.net/browse/PROD-212) — Add support for ordering labs

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Created:** 24/Oct/25 11:37 AM
- **Updated:** 06/Nov/25 6:29 AM

**Description**

Order labs through through the app and send it to a lab of their choice, mainly targeting blood and comprehensive metabolic labs for initial scope.


### [PROD-213](https://impiricus.atlassian.net/browse/PROD-213) — Doc dialer - anonymous dialer for HCPs to call patients

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Created:** 25/Oct/25 11:18 AM
- **Updated:** 25/Oct/25 11:26 AM

**Description**

Given that we already have the patient’s phone number, a doc dialer would fit in well as a companion to Prescriber. Multiple HCPs have said the only thing they use Doximity for is for their doc dialer so we could potentially gain market share from Doximity. 

- Enable HCPs to anonymously call patients
- One click dialing by just selecting the patient and selecting “call patient”
- Can also support typing in a number for numbers we don’t have


### [PROD-215](https://impiricus.atlassian.net/browse/PROD-215) — Add stock/supply integration (Amazon, national mail orders)

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Created:** 06/Nov/25 6:29 AM
- **Updated:** 06/Nov/25 6:32 AM

**Description**

In addition to being a revenue opportunity ($3-4 per script routing fees), we can improve the user experience by allowing them to confirm stock/supply when ordering from pharmacy and route the order accordingly. Saves users the frustration of getting a call back from the pharmacy saying they couldn’t fill their script.


### [PROD-217](https://impiricus.atlassian.net/browse/PROD-217) — Non-dispensing pharmacy 

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Created:** 06/Nov/25 6:32 AM
- **Updated:** 06/Nov/25 6:32 AM


### [PROD-219](https://impiricus.atlassian.net/browse/PROD-219) — Add ability to compound medication when creating a new Rx

- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Created:** 10/Nov/25 4:55 PM
- **Updated:** 21/Nov/25 9:50 AM


### [PROD-221](https://impiricus.atlassian.net/browse/PROD-221) — Concierge - Oncology-focused offering

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 17/Nov/25 10:49 AM
- **Updated:** 17/Nov/25 10:55 AM


### [PROD-242](https://impiricus.atlassian.net/browse/PROD-242) — Modular Integrations - Samples Expansion

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Business Growth, Customer Engagement, Innovation
- **Created:** 09/Dec/25 4:16 PM
- **Updated:** 26/Feb/26 9:12 AM

**Description**

#### Overview

This is the ticket to cover the expansion of the sample management pilots that we are kicking off with Medvantx and QPharma. Samples drive script lift; samples ordering is clunky today; if we can provide frictionless SMS ordering via the top sample closet vendors, then we can fuel Ascend growth and improve the HCP experience. We want to setup channel partnerships so that we can plug a sample integration into the Ascend platform for any brand, any manufacturer.

#### Value for our Business

- same as above; if we can make sample ordering easier and make it available via channel partnerships, then this will boost the Ascend platform engagement offering
- Samples integration also will boost any existing channels where HCPs are asking for samples
  - VC/ SMS
  - chatbot
  - email

#### Value for our Customers

- same as above
  - samples drive script lift
  - sample closet ordering for HCPs is clunky and leads to high drop off
  - if we can make this process easier for HCPs, then it’s a win win

#### What’s In Scope

- The goal is to expand samples integrations and attack as follows.
  - set up channel partnerships with leading sample closets
  - set up integration at brand level (to implement via Brand VC)
*** modify configuration as needed to support HCP ordering via DocUpdate side

#### What’s Out of Scope

- The Ascend team is working on sample integration support via Ascend channels only; DocUpdate team handling any sample integration through their side.

----

*Update as of 10/31/25*

- 2 Integrations in progress with channel partners
  - RxS (Medvantx) - Sanofi Toujeo [https://miro.com/app/board/uXjVJBJqVAM=/](https://miro.com/app/board/uXjVJBJqVAM=/|smart-link) 
*** timing est Q1 2026
  - QPharma - Axsome (Symbravo first, but Auvelity and Sunosi to follow) [https://miro.com/app/board/uXjVJ3CgP3c=/](https://miro.com/app/board/uXjVJ3CgP3c=/|smart-link)
*** timing est Jan 2026
- Miro flows essentially complete with both partners, driving towards consistent DocUpdate flow across all vendors so an HCP order samples via SMS doesn’t have a different experience if it’s RxS as sample closet or QPharma, etc
  - Updated commercial slides demonstrating Impiricus flow
  - [https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28](https://docs.google.com/presentation/d/1Oxq0NQMZ6hsunVBL26zvmNVlH2YGTU_lSyuXZVC-W6E/edit?slide=id.g38f266cd345_0_28#slide=id.g38f266cd345_0_28|smart-link) 
- Joe working on broader level channel partnerships for DocUpdate side
- goal is to develop one technical architecture that can support singular brand sample orders via Ascend VC as well as multiple sample checkouts via DocUpdate 

----

Goal - Brands have reported that HCPs accessing samples is clunky, poor experience and often leads to HCP frustration and HCP drop off

- today sample closets are managed by 3rd parties
- we want to solve this clunky workflow for HCPs by integrating directly with samples vendors and enabling an easier experience via SMS, either through Pulse 
- We are currently scoping an Ascend samples integration with Sanofi LOE and RxS, who has been recently acquired by Medvantx
- Also in parallel, Joe Jackson to scope a broader samples strategy for impiricus with top samples vendors (notes below)

Ascend Samples Comml Slides

[^Copy of Impiricus Sample Request message performance (afe90e7e-e1b7-48ef-b9fb-a428734e8626).pdf]

Anna folder with RxS integration proposal and screenshots

[https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link](https://drive.google.com/drive/folders/1KANbj0JTk26GkUCxn8IhjdyAiO0SwJEJ?usp=drive_link|smart-link) 

9.2.25 Notes from Joe Samples kickoff (Docupdate samples + Ascend)

- largest 2 samples closet
  - knipper - dont entertain channel partners
*** they have a target list - land dr hashmi on their website or channel partner
  - in docupdate app
  - they have an iframe, import our UI
- knipper interested in us
- could lauren get a superuser login?
  - sales reps may already have this - ability to act on behalf of HCPs
- sandy's understanding - veeva doesnt have a samples interface, just used to count how many samples are sent out
- co build something with knipper
- knipper controls more of market, cardinal is larger
- ascend partnerships in near term will drive more volume than docupdate samples
- whatever plugs into ascend will drive volume
- samples are a cost center for brands;
- if we can find 3 brands that use knipper
- todd sync with sales on who would be the ideal partners
- get Joe involved to lead RxS side

####


### [PROD-243](https://impiricus.atlassian.net/browse/PROD-243) — Modular Integrations - Access Agent

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2027-03-01","end":"2027-03-31"}
- **Created:** 09/Dec/25 4:20 PM
- **Updated:** 10/Dec/25 1:18 PM

**Description**

#### Overview {This is a placeholder for now}

These will be customer dependent based on client. The Access Agent integration could be something to support patient access, patient solutions for coverage, etc. 

#### Value for our Business

TBD

#### Value for our Customers

TBD

#### What’s In Scope

- TBD

#### What’s Out of Scope

- TBD


### [PROD-244](https://impiricus.atlassian.net/browse/PROD-244) — Customized Content

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Created:** 09/Dec/25 4:21 PM
- **Updated:** 09/Dec/25 4:21 PM


### [PROD-245](https://impiricus.atlassian.net/browse/PROD-245) — Cash cards for generics

- **Priority:** Medium
- **Reporter:** Abiy Kaltiso
- **Roadmap bucket:** Intake
- **Created:** 09/Dec/25 4:34 PM
- **Updated:** 09/Dec/25 4:34 PM


### [PROD-285](https://impiricus.atlassian.net/browse/PROD-285) — Quantity type selection 

- **Priority:** Medium
- **Reporter:** Tyler Carty
- **Created:** 29/Dec/25 3:53 PM
- **Updated:** 29/Dec/25 3:54 PM

**Description**

#### *Overview*

Add support for configurable medication quantity types that allow clinicians to explicitly choose _how_ a medication quantity is prescribed. For medications with multiple packaging or unit options (e.g., creams, liquids, inhalers), users can specify quantities such as “1 × 25 mL tube” versus a raw volume amount like “500 mL.” The goal is to improve prescribing clarity, reduce downstream confusion, and deliver a meaningfully better experience than traditional EMRs and e-prescribing systems.

----

#### *Value for our Business*

- Differentiates DocUpdate by solving a long-standing, universally disliked pain point in e-prescribing.
- Positions the product as “better than what’s already there”, not just equivalent to existing EMRs.
- Reduces pharmacy callbacks and prescription errors that erode trust in prescribing software.
- Strengthens brand credibility with both prescribers and pharmacists by demonstrating workflow empathy.
- Drives retention and advocacy by eliminating a frustration clinicians have normalized but deeply resent.

----

#### *Value to our Users*

- Gives clinicians clear, confident control over how medications are dispensed.
- Prevents pharmacy clarification calls that interrupt clinical workflows and waste time.
- Reduces prescribing errors related to ambiguous units, packaging sizes, or quantities.
- Aligns prescribing intent with real-world pharmacy fulfillment realities.
- Provides a smoother, more intuitive prescribing experience that feels modern and thoughtful.

----

#### *What’s in Scope*

- Ability for users to select quantity type during prescribing (e.g., tubes, bottles, grams, milliliters, inhalers).
- Support for medications with multiple packaging options and common dispense units.
- UI enhancements that clearly present quantity choices in context of the medication form.
- Validation logic to prevent incompatible or ambiguous quantity selections.
- Ensuring quantity details flow cleanly through e-prescribing and pharmacy systems.
- Maintaining compatibility with existing prescribing standards and workflows.


### [PROD-290](https://impiricus.atlassian.net/browse/PROD-290) — Data sharing & intake from Jiro

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 02/Jan/26 2:24 PM
- **Updated:** 17/Feb/26 4:16 PM

**Description**

#### Overview

As part of a broad partnership with Jiro, we will have access to their enrolled HCPs for SMS messaging and registration for the DocUpdate application. We will also deploy a version of the Concierge module for rendering in Jiro’s native apps. 

#### Value for our Business

- Source of permissioned HCPs to allow messaging
- Additional concierge users to drive eventual monetization of sample orders and other pharma-funded engagements

#### Value for our Customers

- Provides access to our features to more HCPs

#### What’s In Scope

- Receipt of clincian data and contact information for our subsequent messaging via a daily flat file
- Provision of a version of the Concierge product via a new API (not directly via Zendesk)

#### What’s Out of Scope

- TBD


### [PROD-294](https://impiricus.atlassian.net/browse/PROD-294) — Concierge Sample Integrations

- **Priority:** Medium
- **Reporter:** Lauren Maeder
- **Value drivers:** Business Growth, Customer Engagement
- **Project start:** {"start":"2026-02-01","end":"2026-02-28"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 05/Feb/26 2:06 PM
- **Updated:** 20/Feb/26 8:06 AM

**Description**

#### Overview

Partnering with sample closet providers to offer eligible HCPs direct access to sample ordering, without needing to be diverted to an external portal. 

#### Value for our Business

- Drive user love & retention
  - will return back to us via going to the sample closet directly
- Added selling point for Ascend clients 
  - higher sampling volume
  - more visibility to eligible providers

#### Value for our Customers

- improved sampling experience for DocUpdate users
  - less redirection
  - reduces the headache of having separate sample accounts

#### What’s In Scope

- Demonstrating an integrated product name within the sample dropdown once HCP is deemed eligible for the samples (as confirmed via NPI check)
- Adding dosage, quantity, signature/OTP, & T&C into the app workflow, as required by the associated sample partner for the selected product

#### What’s Out of Scope

-


### [PROD-298](https://impiricus.atlassian.net/browse/PROD-298) — Surveys for Ascend

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-09-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-10-15","end":"2026-10-15"}
- **Created:** 17/Feb/26 5:35 PM
- **Updated:** 13/Apr/26 1:40 PM

**Description**

#### *Overview*

Development of survey platform to meet the need of the Ascend product for insights into HCP attitudes

#### *Value for Our Business*

- Provides insights to the Ascend (commercial) side of the business by surveying HCPs on their approach to treatment of conditions, perception of existing treatment protocols, etc
- Drives engagement with the DocUpdate app

#### *Value for Our Customers*

- Allows our Ascend client (initial customer) to generate insights to help manage their end user pharma clients

#### *What’s In Scope*

- This includes:
*# Rendering multi-question surveys in the DocUpdate UI to qualified HCPs. 
*# Automatically sending compensation as a gift card to qualified HCPs.

#### *What’s Out of Scope*

- TBD


### [PROD-300](https://impiricus.atlassian.net/browse/PROD-300) — LabMap (lab ordering with data validation)

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-03-15","end":"2027-03-15"}
- **Project target:** {"start":"2027-06-30","end":"2027-06-30"}
- **Created:** 17/Feb/26 6:04 PM
- **Updated:** 14/Apr/26 5:38 PM

**Description**

#### Overview

Allow ordering of lab testing via the app

For certain novel lab orders, validate that sufficient information about the patient, their past treatments, and past testing has been supplied to allow proper reimbursement

Lack of this information results in time-consuming back-and-forth communication between patient, HCP and payer

#### Value for our Business

- Provides a compelling reason for HCPs to use the DocUpdate app, driving opt-ins
- As simplifing lab ordering both increases usage of novel lab testing and saves time for staff of the lab testing provider, they may be willing to pay to be included in the DocUpdate lab ordering service

#### Value for our Customers

- Saves time for clinicians by ensuring all information is included in the initial lab request
- Saves time for clinicians by substituting for faxed paper forms in some cases
- Simplifies the ordering and reconciliation process for the lab provider

#### What’s In Scope

- Development of.a UI and API connection which will allow ordering of standard lab tests within the DocUpdate UI (LabCorp and/or Quest plug-in)
- Development of a UI and connection which will allow ordering of novel lab tests (such as genetic tests for certain cancer treatments) This will involve aggregating of current paper forms for auto-population and faxing to lap suppliers

#### What’s Out of Scope

- TBD


### [PROD-303](https://impiricus.atlassian.net/browse/PROD-303) — Controlled substance prescribing

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2027-10-01","end":"2027-10-31"}
- **Created:** 17/Feb/26 8:36 PM
- **Updated:** 14/Apr/26 4:24 PM

**Description**

#### Overview

Incorporate required changes to allow prescribing of controlled substances (scheduled drug) in the application

#### Value for our Business

- Expands our HCP universe by registering new HCPs who want to write controlled substances
- Increase stickiness of the application by allowing all drugs to be prescribed via DocUpdate
- Increase potential fee revenue by increasing prescribing volume

#### Value for our Customers

- Allow prescribing of all meds via one application, making writing simpler and easier for our HCP users

#### What’s In Scope

- Implement additional verification steps required for writing of scheduled drug during the initial verification process
- Allow for a two-tiered verification process with a lesser standard for users who do not want to prescribe controlled drugs and/or are unwilling to provide the required information
- Inclide the additional verification steps required for prescriber authentication for the writing of controlled drugs (including 2FA identity verification via OTP or authenticator app)

#### What’s Out of Scope

- TBD


### [PROD-304](https://impiricus.atlassian.net/browse/PROD-304) — Role and rules based landing page rendering

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-05-01","end":"2026-05-31"}
- **Created:** 17/Feb/26 8:59 PM
- **Updated:** 19/Mar/26 8:35 AM

**Description**

#### Overview

Render the DocUpdate application UI differently based on known data about the user and/or the traffic source driving the user to the application

#### Value for our Business

- Required for baseline functionality: As we add new features and modules to the application, it will be increasingly difficult for a user to navigate the UI without assistance; for new features to be widely utilized, the UI will need to render the features/modules most likely to be used

#### Value for our Customers

- HCP users will benefit from improved navigation based on what features they would most likely want to use

#### What’s In Scope

- A UI which renders different modules based on previous user behavior, specialty or desired module to be rendered on landing
- Default behavior should render the module which the user last used on the previous visit 
- For first time users, the first visible module should be rendered based on known information stored about the user (e.g., if the HCP’s specialty is oncology, the Trial Navigator module should be rendered)
- UI should always provide the ability for any user to access any module for which they are validated; the only service that would be restricted is Prescriber which should not be available to any user who is not Persona validated.

#### What’s Out of Scope

- TBD


### [PROD-308](https://impiricus.atlassian.net/browse/PROD-308) — Anonymous in-app dialer and SMS 

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-12-01","end":"2027-12-31"}
- **Project target:** {"start":"2028-01-01","end":"2028-01-31"}
- **Created:** 20/Feb/26 8:25 AM
- **Updated:** 13/Mar/26 7:57 AM

**Description**

#### Overview

Development of a DocUpdate module which allows calling and SMS texting from the app. 

#### Value for our Business

- Funcitionality would drive frequent app usage, keeping HCPs engaged and keep the app present on the HCP’s device.

#### Value for our Customers

- HCPs have a need to call and message patients from their mobile devices without exposing their mobile number; this functionality meets that need.
- Some HCPs using our application have indicated that they use other platforms solely for similar capabilities. Offering this functionality in DocUpdate would reduce the number of apps they have to use. 

#### What’s In Scope

- In-app functionality allowing calling and SMS texting 
- Call or message recipient should not see the users mobile number on caller ID
- HCP user must be able to display office number or no number to patient via caller ID
- HCP should be able to engage in two-way SMS texting with patient via this functionality even when mobile number is not exposed to patient

#### What’s Out of Scope

- Provision of mobile numbers for user


### [PROD-313](https://impiricus.atlassian.net/browse/PROD-313) — Campaign Risk & Delivery Tracking

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Created:** 24/Feb/26 3:12 PM
- **Updated:** 24/Apr/26 5:21 PM

**Description**

#### Problem(s) We Are Solving

1. Campaign risk & delivery status is created & updated by hand in a spreadsheet, separate from real-time data
1. Existing trackers in Pulse Runner show good message level details but it’s challenging view campaign and message performance together

#### Solution Approach

Create a new campaign level tracker that

- Indicates any risk with a given campaign
- Allows for viewing progress at a campaign level
- Includes campaign statuses
- Includes separate readiness & launch dates
- Is filterable by various statuses (active, recently launched, in QA, etc.)
  - _mock needs update here_
- groups messages by their Journey name (assigned during campaign creation)

#### To validate

- What types and levels of risk are we concerned with? examples to validate
  - On-time launch 
  - Hitting guaranteed deliveries efficiently
*** Recoverable / irrecoverable errors below X threshold
  - Achieving performance goals 
*** Engagement
*** Maintain network health (opt outs)


### [PROD-314](https://impiricus.atlassian.net/browse/PROD-314) — Rapid automated SMS testing

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-08-01","end":"2026-08-31"}
- **Project target:** {"start":"2026-09-15","end":"2026-09-15"}
- **Created:** 24/Feb/26 3:24 PM
- **Updated:** 24/Apr/26 5:18 PM

**Description**

#### Problem(s) We Are Solving

Impiricus is expecting 3x message volume in 2026 and must ensure that messages meet certain criteria before being sent

1. message copy match the MLR approved copy exactly
1. content fits into one message bubble
1. URLs are clickable and go to the correct locations
1. flow responses are correct

Testing pulses is a manual process today that is largely performed by one individual. 

Testing VC is also manual, but more time intensive and requires cross-functional participation. Changes to VC often necessitate retesting the entire flow (expected on average to be 15 messages) and can lead to decisions to accept “close enough” instead of the best possible version due to time constaints.

#### Solution Approach

Potential solutions

- Simulate the SMS flow through an API to ensure copy & responses are correct
- Simulate the SMS flow on real devices and take screenshots to confirm accuracy & send to clients


### [PROD-315](https://impiricus.atlassian.net/browse/PROD-315) — Spark setup automation

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-10-16","end":"2026-10-16"}
- **Project target:** {"start":"2026-12-15","end":"2026-12-15"}
- **Created:** 24/Feb/26 3:24 PM
- **Updated:** 24/Apr/26 5:21 PM

**Description**

#### Problem(s) We Are Solving

Spark setup is a highly manual, time intensive process today. [This video](https://us02web.zoom.us/rec/play/Rr-iDWUslQY-sF8_5plY_q1UDjuzvxBj58CevTwVUBZ8DcmuZp3W2HNRnqcX6fDAVW8A3iYTj4Ke2uzu.QVS1c4lGxl7IAFXb?eagerLoadZvaPages=sidemenu.billing.plan_management&accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&startTime=1767719793000&componentName=rec-play&originRequestUrl=https%3A%2F%2Fus02web.zoom.us%2Frec%2Fshare%2F51_dprMGKYOBu1fDK6isdMBlZ0nadWVLC_Gt5u-AC-OPmiTNYX2aLsVpr5g4Abnz.XaY13bDjbmn_Uip4%3FstartTime%3D1767719793000) covers the existing process, and rules are captured in this markdown file

[^spark_processing_rules_examples.md]

#### Solution Approach - TBD


### [PROD-316](https://impiricus.atlassian.net/browse/PROD-316) — Spark monitoring automation

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-10-16","end":"2026-10-16"}
- **Project target:** {"start":"2026-11-01","end":"2026-11-30"}
- **Created:** 24/Feb/26 3:24 PM
- **Updated:** 24/Apr/26 5:21 PM

**Description**

#### Problem(s) We Are Solving

Spark monitoring requires manual checks regularly for each spark to ensure

- Files received	
- Messages Went out
- Total Deliveries to Date (at Campaign Level)

### Solution Approach

Automate the tracking of spark related information and alert IMs in slack if 

- file is not received
- messages do not go out

CS & IM should be able to see success / failure information within the platform campaign tracker


### [PROD-317](https://impiricus.atlassian.net/browse/PROD-317) — Ascend - AI Campaign Builder V3

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-11-16","end":"2026-11-16"}
- **Project target:** {"start":"2026-10-01","end":"2026-12-31"}
- **Created:** 24/Feb/26 3:24 PM
- **Updated:** 10/Apr/26 1:25 PM

**Description**

#### Problem(s) We Are Solving

VC Studio offers a UI-based approach to constructing Virtual Coordinators.

Virtual Coordinators include the highest volume of messages compared to pulses, which is incredibly time consuming on setup and testing.

#### Solution Approach

Add VC support to campaign builder, to leverage the message extraction capabilities needed to prepare VC messages.

Integrate the VC studio UI into pulse runner so a user can access both campaign builder and VC studio in one place through a single login.


### [PROD-330](https://impiricus.atlassian.net/browse/PROD-330) — VC: Support for Rich Content

- **Priority:** Medium
- **Reporter:** Sam Thomas
- **Created:** 26/Feb/26 5:13 PM
- **Updated:** 26/Feb/26 5:27 PM

**Description**

#### Overview

This work would allow for us to offer rich content in our VC messaging prior to / separate from any work to support RCS. This would expand our capabilities for more interactive content types in SMS channels (e.g. images, font formatting, etc.) and would allow us to leverage HTML functionality for content rendered in the web chatbot. 

#### Value for our Business

This allows us to surface more engaging and appealing content in our VC channels, which should in turn enhance the engagement rates we see from HCPs. 

#### Value for our Customers

This would allow our customers to provide more engaging content to HCPs, which should boost engagement rates. It would also allow customers to leverage more engaging content that they may already have available vs. needing to convert more engaging content to text formats to fit SMS. 

#### What’s In Scope

- Builder tools / capabilities to support rich content

#### What’s Out of Scope

- Deployment / availability of RCS across our applications


### [PROD-351](https://impiricus.atlassian.net/browse/PROD-351) — Advisory Connect/Advisory Nexus

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-11-01","end":"2026-11-30"}
- **Project target:** {"start":"2027-02-01","end":"2027-02-28"}
- **Created:** 10/Mar/26 8:43 PM
- **Updated:** 13/Apr/26 7:33 PM

**Description**

#### Overview

Application to give HCPs the opportunity to participate on advisory boards, engage in content creation, and complete surveys, all for compensation. 

#### Value for our Business

- Increases engagement with the DocUpdate application and platform
- Provides a Pavlovian reason to return to the app when  opportunities occur each week
- Potential for pharma revenue for advisory boards and survey execution

#### Value for our Customers

- Revenue opportunity for our clinician users
- HCP insights and brand exposure for our pharma clients

#### What’s In Scope

- Configuration of the survey functionality to allow targeting by supplied NPIs, specialties, geography or other data points

#### What’s Out of Scope

- TBD


### [PROD-352](https://impiricus.atlassian.net/browse/PROD-352) — Independent Activity (MSL equlvalent to speaker programs)

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-07-01","end":"2027-09-30"}
- **Project target:** {"start":"2027-12-01","end":"2027-12-31"}
- **Created:** 10/Mar/26 8:48 PM
- **Updated:** 14/Apr/26 4:05 PM

**Description**

scope and concept TBD


### [PROD-354](https://impiricus.atlassian.net/browse/PROD-354) — AI Biologic Coordinator

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2027-01-01","end":"2027-01-31"}
- **Project target:** {"start":"2027-06-01","end":"2027-06-30"}
- **Created:** 19/Mar/26 8:34 AM
- **Updated:** 14/Apr/26 4:03 PM

**Description**

#### Overview

Chat-based, AI-enabled coordinator to assist in handling access issues for biologic medications with access challenges such as prior authorization, step edits, exclusive availability at a limited network of specialty pharmacies, etc.

#### Value for our Business

- USP: no similar product is currently in market
- Provides a value proposition to motivate HCPs to register for DocUpdate
- Drives deeper/more frequent engagement with DocUpdate app
- Potential to sell upgraded/customized support service to pharma

#### Value for our Customers

- Saves time for clinicians and practice staff when writing biologics
- Makes it more likely that patients will get med in possession for drug initially prescribed

#### What’s In Scope

- Facility to clinician if a specific drug has prior auth, fail first or other requirements for coverage
- Tool to access patient record (likely via an aggregator) to provide information to accompany prior auth submission
- Inform HCP of any availability issues and direct HCP to pharmacies which stock/support drug
- Scope will be enlightened by prior auth build in 2026

#### What’s Out of Scope

- TBD


### [PROD-355](https://impiricus.atlassian.net/browse/PROD-355) — Remedy OTC samples program

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-10-01","end":"2026-12-31"}
- **Project target:** {"start":"2026-11-01","end":"2026-11-30"}
- **Created:** 13/Apr/26 8:48 AM
- **Updated:** 13/Apr/26 4:54 PM


### [PROD-357](https://impiricus.atlassian.net/browse/PROD-357) — QPharma Samples Integration (Symbravo)

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-05-01","end":"2026-05-31"}
- **Project target:** {"start":"2026-06-01","end":"2026-06-30"}
- **Created:** 13/Apr/26 12:57 PM
- **Updated:** 13/Apr/26 1:00 PM

**Description**

#### *Overview*

This initiative allows in-app ordering of samples for the Symbravo brand at QPharma.

#### *Value for Our Business*

- Allows support of our Ascend business by allowing easier sample ordering for these Ascend contracted brands
- Integration with QPharma for a major brand provides a negotiating point for integrating with other sampling partners
- Initial implementation with QPharma is a first step to integration with all QPharma brands
- Allowing direct ordering of samples in-app reduces staff time required to handle related Concierge requests and makes the Concierge business more scalable. 

#### *Value for Our Customers*

- Allows easier ordering of samples for HCP users
- Provides additional sample orders for Ascend client Axsome

#### *What’s In Scope*

- Rendering URL provided by QPharma for an individual HCP as a web view in app. 

#### *What’s Out of Scope*

- Integration with any other QPharma brand


### [PROD-359](https://impiricus.atlassian.net/browse/PROD-359) — Translator enhancements

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-08-01","end":"2026-08-31"}
- **Project target:** {"start":"2026-09-01","end":"2026-09-30"}
- **Created:** 13/Apr/26 2:00 PM
- **Updated:** 13/Apr/26 2:01 PM

**Description**

#### Overview

Enhancements and upgrades to Translator module in response to use feedback. Primary changes include: adding ambient translation, evaluating and possibly changing the translation engine, and improvements to audio quality and output. 

#### Value for our Business

Provides opportunity to increase repeat usage of translator as well as leverage translator improvements as an HCP acquisition narrative. 

#### Value for our Customers

Makes translator easier to use

#### What’s In Scope

- Adding “ambient” mode to translation functionality which eliminates the need for users to press a button when done speaking to trigger translation functionality
- Evaluation and possible migration of translation engine to optimize speed and output quality
- Evaluation and possible migration of text to speech engine to improve voice quality

#### What’s Out of Scope

- Scribe functionality


### [PROD-360](https://impiricus.atlassian.net/browse/PROD-360) — Advisory Nexus: Contracting and compensation for HCPs in app

- **Priority:** Medium
- **Reporter:** Chris Leavitt
- **Project start:** {"start":"2026-09-01","end":"2026-09-30"}
- **Project target:** {"start":"2026-10-01","end":"2026-10-31"}
- **Created:** 13/Apr/26 5:11 PM
- **Updated:** 13/Apr/26 7:07 PM

**Description**

#### Overview

In preparation for Advisory Connect/Advisory Nexus and other opportunities, create an automated workflow for HCPs to contract with us on behalf of pharmaceutical companies for ad boards and other engagements

#### Value for our Business

- Automates contracting and compensation for situations where we compensate HCPs in bulk
- Ensures compliance by automating Sunshine Act compliance for programs contracted directly with pharmaceutical and biotech manufacturers

#### Value for our Customers

- Clinicians have an easy way to sign contracts with us to receive compensation
- Pharmaceutical clients have the security that our programs are compliant 

#### What’s In Scope

- User interface to allow review and signing of contracts automatically
- Review/signing of contracts can be in Rippling or other third party application
- Clinicians must be able to see their current earnings in our UI
- Clinicians can “bank” their earnings and see the current total in the UI
- Users should be able to transfer their stored earnings to their bank account or have them sent as a check
- System should drive Sunshine Act reporting annually

#### What’s Out of Scope

- Contract management system is a separate application to which user can be linked and/or can be viewed via API/web view in the application


### [PROD-363](https://impiricus.atlassian.net/browse/PROD-363) — Post Launch: Rapid automated SMS testing

- **Priority:** Medium
- **Reporter:** Ben Barone
- **Project start:** {"start":"2026-09-16","end":"2026-09-16"}
- **Project target:** {"start":"2026-10-14","end":"2026-10-14"}
- **Created:** 24/Apr/26 5:20 PM
- **Updated:** 24/Apr/26 5:21 PM

**Description**

#### Problem(s) We Are Solving

Impiricus is expecting 3x message volume in 2026 and must ensure that messages meet certain criteria before being sent

1. message copy match the MLR approved copy exactly
1. content fits into one message bubble
1. URLs are clickable and go to the correct locations
1. flow responses are correct

Testing pulses is a manual process today that is largely performed by one individual. 

Testing VC is also manual, but more time intensive and requires cross-functional participation. Changes to VC often necessitate retesting the entire flow (expected on average to be 15 messages) and can lead to decisions to accept “close enough” instead of the best possible version due to time constaints.

#### Solution Approach

Potential solutions

- Simulate the SMS flow through an API to ensure copy & responses are correct
- Simulate the SMS flow on real devices and take screenshots to confirm accuracy & send to clients


### [PROD-60](https://impiricus.atlassian.net/browse/PROD-60) — List Match & Target List Objects

- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Roadmap bucket:** Later
- **Created:** 21/May/25 11:06 AM
- **Updated:** 03/Mar/26 9:16 AM

**Description**

#### Problem context

- Manually adding versioning to List Matches/Target Lists via the naming convention whenever we make updates to the contents of a Target List
- Target Lists aren’t connected to Campaigns or Pulses in db
  - Manually upload a Target List to a Pulse based off of criteria in a JIRA card
- Ensuring that we’re leveraging the correct Target List is a time consuming and error prone process when running List Match analysis
- There is currently no concept of a LM object in PulseRunner
  - You upload a list and it gives you an output of “optimized” NPIs in our system
  - You’re able to select a previous Pulse from a dropdown to reuse that Pulses’s target list

#### Impact

- Save time by automatically creating a new version of a Target List under the same parent ID
- Avoid confusion by ensuring that we’re using the latest Target List provided by CS, or the client, etc. for the Campaign & Pulses
- Allow us to forecast against campaigns & pulses sooner and more easily

#### Desired outcome

- Object in PulseRunner that can be attached to Campaigns & Pulses
  - Do we need to allow targeting at the Segment level? Since a campaign targets a TL but a Pulse can target a subset of it?
- The different versions of a List Match/Target List will be under the same ID
  - The LM ID is connected to a Campaign or Pulse ID and if there are changes to the LM (i.e. it's refreshed) we store the changes in the List Match change log but the connection to the Pulse stays the same (i.e. TL : Pulse ID connection)
*** Should we auto update the Pulse Target List? Or keep the original Target List as when the Pulse was set live?
- Updates to List Match & Target List Functionality are already being discussed in [https://impiricus.atlassian.net/browse/INT-1526](https://impiricus.atlassian.net/browse/INT-1526|smart-link) & [https://impiricus.atlassian.net/browse/INT-1550](https://impiricus.atlassian.net/browse/INT-1550|smart-link) 
  - *5/28/25 - Confirm with Alan & Dev team if these ideas can be rolled into the work being done in the above tickets*

#### Required Actions:

- Can/should we leverage the old campaignID field to associate respective campaign to a List Match / Target List?
- Below is the current formatting for how we name List Match objects:
  - _year_brand_manufacturer_contractNum_listNum_
  - The “listNum” element is completely internal to the List Match process whereas the other elements should exactly match the contract ID that Sales/Ops/CS uses
  - We should automate the “listNum” aspect of the naming so that all of the versions (i.e. numbers) of the LM are associated to the same parent object


### [PROD-78](https://impiricus.atlassian.net/browse/PROD-78) — SMS Message Capability Expansion (RCS, Conferences, Surveys)

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Project start:** {"start":"2025-04-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-09-01","end":"2025-09-30"}
- **Created:** 18/Jul/25 1:24 PM
- **Updated:** 25/Aug/25 9:22 AM

**Description**

### 🚀 Opportunity Statement

> Transform problems into opportunities to improve people’s experiences

#### Problem context

_Describe the background or current situation that reveals the problem or unmet need._

_Example: Users are unable to provide feedback quickly and easily, leading to dissatisfaction and reduced engagement_

#### Impact

_Describe how the problem affects the customer experience. Highlight how it impacts the business objectives._

_Example:_ _This issue results in fewer feedback submissions, making it difficult to gather user insights for improvement. This results in slower iterations, affecting overall customer retention_

#### Desired outcome

_Define what success looks like if this problem is solved, using measurable metrics where possible._

_Example: A streamlined feedback submission process would increase the feedback submission rate by 30% and lead to faster product iterations_

*Resources (add your own):*

- 📝 *PRD/spec*
- 📹 *Loom* *Video*
- 👩‍🎨 *Design file*


### [PROD-80](https://impiricus.atlassian.net/browse/PROD-80) — Pulse Runner General (Pulse Creation, Reporting, Tech Impvts)

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Project start:** {"start":"2025-01-01","end":"2025-03-31"}
- **Project target:** {"start":"2025-09-01","end":"2025-09-30"}
- **Created:** 18/Jul/25 1:28 PM
- **Updated:** 15/Sep/25 12:49 PM

**Description**

### 🚀 Opportunity Statement

> Transform problems into opportunities to improve people’s experiences

#### Problem context

_Describe the background or current situation that reveals the problem or unmet need._

_Example: Users are unable to provide feedback quickly and easily, leading to dissatisfaction and reduced engagement_

#### Impact

_Describe how the problem affects the customer experience. Highlight how it impacts the business objectives._

_Example:_ _This issue results in fewer feedback submissions, making it difficult to gather user insights for improvement. This results in slower iterations, affecting overall customer retention_

#### Desired outcome

_Define what success looks like if this problem is solved, using measurable metrics where possible._

_Example: A streamlined feedback submission process would increase the feedback submission rate by 30% and lead to faster product iterations_

*Resources (add your own):*

- 📝 *PRD/spec*
- 📹 *Loom* *Video*
- 👩‍🎨 *Design file*


### [PROD-81](https://impiricus.atlassian.net/browse/PROD-81) — Spark Triggers Automation & Commercialization

- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Project start:** {"start":"2025-04-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-09-01","end":"2025-09-30"}
- **Created:** 18/Jul/25 1:29 PM
- **Updated:** 15/Sep/25 12:50 PM

**Description**

### 🚀 Opportunity Statement

> Transform problems into opportunities to improve people’s experiences

#### Problem context

_Describe the background or current situation that reveals the problem or unmet need._

_Example: Users are unable to provide feedback quickly and easily, leading to dissatisfaction and reduced engagement_

#### Impact

_Describe how the problem affects the customer experience. Highlight how it impacts the business objectives._

_Example:_ _This issue results in fewer feedback submissions, making it difficult to gather user insights for improvement. This results in slower iterations, affecting overall customer retention_

#### Desired outcome

_Define what success looks like if this problem is solved, using measurable metrics where possible._

_Example: A streamlined feedback submission process would increase the feedback submission rate by 30% and lead to faster product iterations_

*Resources (add your own):*

- 📝 *PRD/spec*
- 📹 *Loom* *Video*
- 👩‍🎨 *Design file*


### [PROD-97](https://impiricus.atlassian.net/browse/PROD-97) — Journal Summaries - PDFs for remaining Specialties (web only)

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Project start:** {"start":"2025-07-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-08-01","end":"2025-08-31"}
- **Created:** 04/Aug/25 2:46 PM
- **Updated:** 05/Sep/25 3:05 PM


### [PROD-98](https://impiricus.atlassian.net/browse/PROD-98) — Journal Summaries Podcast (web only)

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Project start:** {"start":"2025-08-01","end":"2025-08-31"}
- **Project target:** {"start":"2025-07-01","end":"2025-09-30"}
- **Created:** 04/Aug/25 2:46 PM
- **Updated:** 05/Sep/25 3:04 PM


### [PROD-99](https://impiricus.atlassian.net/browse/PROD-99) — Journal Summaries in-app experience

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Project start:** {"start":"2025-09-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-10-01","end":"2025-10-31"}
- **Created:** 04/Aug/25 2:47 PM
- **Updated:** 05/Sep/25 3:04 PM


## Done (24)

### [PROD-196](https://impiricus.atlassian.net/browse/PROD-196) — AI Voice Surveys (MVP)

- **Initiative:** AI Voice Survey
- **Priority:** Low
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Project start:** {"start":"2025-09-15","end":"2025-09-15"}
- **Project target:** {"start":"2025-10-03","end":"2025-10-03"}
- **Created:** 15/Sep/25 2:11 PM
- **Updated:** 03/Mar/26 9:15 AM

**Description**

This is the parent ticket to capture all work related to voice surveys.


### [PROD-151](https://impiricus.atlassian.net/browse/PROD-151) — DocUpdate Advertising Campaign for Out-of-Network Oncs

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-09-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-11-01","end":"2025-11-30"}
- **Created:** 25/Aug/25 11:46 AM
- **Updated:** 20/Nov/25 4:04 PM

**Description**

As part of our plan to add in net new Oncologists to grow our network, we’re going to launch a DocUpdate Advertising Campaign targeting Oncologists that we’ve seen in client Target Lists but we haven’t been able to find a Clay number for them.

An overview of the information & schema we need to provide to Simon Wool and team to launch the campaign is attached below:

[^Meta Custom Audience Guidelines.pdf]


### [PROD-153](https://impiricus.atlassian.net/browse/PROD-153) — Launch "Rewards Pulse" to Re-Engage Oncs

- **Initiative:** Growing Onc. Segment
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-10-06","end":"2025-10-06"}
- **Project target:** {"start":"2025-11-28","end":"2025-11-28"}
- **Created:** 25/Aug/25 11:55 AM
- **Updated:** 20/Nov/25 4:04 PM

**Description**

- Engaging existing Oncologists to boost disposition scores
  - Perform overlap of Klick Survey Target List (544652) and include Oncs not on this list that have < =3- DD or one’s how previously have had high engagement and have since dropped off
*** Should we have a general follow up a couple of weeks after to maintain relevancy with the HCPs?

Notes from initial conversation [here](https://docs.google.com/document/d/14VxwXdtLmRs_SVzznvg6uJt6ADl1N2xe7hadPX6VuYw/edit?tab=t.0#heading=h.iozt0c1t68si).


### [PROD-146](https://impiricus.atlassian.net/browse/PROD-146) — Automate Pulse Creation

- **Initiative:** IM AI Automation
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2025-12-01","end":"2025-12-31"}
- **Project target:** {"start":"2026-01-01","end":"2026-01-31"}
- **Created:** 25/Aug/25 9:20 AM
- **Updated:** 03/Mar/26 10:49 AM

**Description**

#### *Overview*

This epic focuses on automating the creation of Pulse objects in PulseRunner by eliminating the current manual workflow of extracting data from JIRA and manually entering it into PR. This automation will serve as a POC for broader workflow automation initiatives for PR.

#### *Value for our Business*

Automating Pulse creation significantly reduces manual effort on the IMs, minimizes human error, and accelerates campaign setup processes. Establishing this automation as a POC also builds the foundation for future scalable automations that streamline operations across CS and IMs.

#### *Value for our Customers*

Customers benefit from faster campaign initiation, more accurate configuration of campaign details, and reduced risk of delays caused by manual data transfer. Improved operational efficiency leads to smoother launches and more predictable delivery timelines.

#### *What’s In Scope*

- Building an automated workflow that pulls necessary Pulse configuration data from JIRA, transforms it into the required PulseRunner format, and creates Pulse objects programmatically

#### *What’s Out of Scope*

- Automating additional parts of the campaign setup process beyond Pulse creation

----

*Update as of 11/3/25:*

- Dev completed initial spike ticket [https://impiricus.atlassian.net/browse/INT-2291](https://impiricus.atlassian.net/browse/INT-2291|smart-link) 
- Documented recommendation page which is under Dev leadership review
  - [https://impiricus.atlassian.net/wiki/spaces/SD/pages/946831362/Pulse+Automation+Implementation+Routes+Comparison+Summary](https://impiricus.atlassian.net/wiki/spaces/SD/pages/946831362/Pulse+Automation+Implementation+Routes+Comparison+Summary|smart-link) 

----

- Current process for creating Pulses in Pulse Runner is manual
- Jira is the source of truth
- CS creates Jira tickets with all necessary information
- IM team manually enters in this information into Pulse Runner
- goal of ticket - automate information from Jira to Pulse Runner


### [PROD-86](https://impiricus.atlassian.net/browse/PROD-86) — ION Internal Price Bidding

- **Initiative:** ION
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth, Network Health
- **Created:** 23/Jul/25 11:00 AM
- **Updated:** 05/Mar/26 4:17 PM

**Description**

#### Overview

This epic focuses on enhancing ION’s decisioning logic by introducing internal “bidding” mechanisms that intelligently match high priority demand with high value inventory. The goal is to create a more programmatic, market-like system that accounts for client priority, contractual obligations, and delivery needs when allocating impressions.

#### Value for our Business

Programmatic style internal bidding improves allocation efficiency, ensures we meet high priority commitments, and maximizes yield across our inventory. This sophistication positions ION as a more dynamic and revenue optimized engine, reducing risk of underdelivery while strengthening relationships with key clients.

*Business Drivers:* Network Health, Business Growth

#### Value for our Customers

Customers benefit from more accurate fulfillment, improved pacing consistency, and preferential access to the right HCPs at the right moments based on campaign importance. Priority based decisioning increases performance in how impressions are allocated.

#### What’s In Scope

- Designing and implementing internal “bid” constructs based on priority factors such as contract terms, strategic importance, and delivery urgency
- Integrating this “bidding” logic into the ION optimization engine
- Testing how pricing signals influence allocation outcomes
- Documenting prioritization rules
- Establishing a framework for future expansion of bid variables.

#### What’s Out of Scope

- External-facing pricing changes
- Client billing updates, or commercial packaging adjustments
- Auction mechanics involving external buyers, or integrations with third-party ad exchanges


### [PROD-108](https://impiricus.atlassian.net/browse/PROD-108) — IQVIA Data Evaluation

- **Initiative:** IQVIA Data
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Business Growth
- **Project start:** {"start":"2025-08-14","end":"2025-08-14"}
- **Project target:** {"start":"2025-10-22","end":"2025-10-22"}
- **Created:** 15/Aug/25 3:52 PM
- **Updated:** 20/Nov/25 4:03 PM

**Description**

We have a 60 days evaluation period with the IQVIA data. During this time, we need to analyze the data and review tactical/product visions on what we're planning to present to IQVIA at the end of the evaluation.

Here's the [+evaluation framework+](https://www.google.com/url?q=https://docs.google.com/document/d/1U7B6eZUUHsCKFk3TnB0JtZgnS3STSAsjKY-zhqN1gVM/edit?tab%3Dt.0&sa=D&source=calendar&ust=1755694727905169&usg=AOvVaw0lU-ZIa5AtRu9uFaSzeHxn) we previously sent to IQVIA. It has a rough (and corporatized) outline of the products we can build but we can also do much more.

We should expect the data the *1st week of September* and make sure we have the capacity after that to have a 30 day intensive review period.


### [PROD-130](https://impiricus.atlassian.net/browse/PROD-130) — Independent Initiatives - Jotform Education Pemazyre

- **Initiative:** Independent Initiatives
- **Priority:** Medium
- **Reporter:** Mike Gelber
- **Value drivers:** Customer Engagement
- **Created:** 20/Aug/25 10:27 AM
- **Updated:** 10/Dec/25 2:13 PM

**Description**

- Similar to what we did for Nagish (Lauren can share example) it's an educational, almost survey-style flow that you go through to learn about something and get a gift card


### [PROD-149](https://impiricus.atlassian.net/browse/PROD-149) — Inventory Scheduler Updates (V2)

- **Initiative:** Inventory Scheduling
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Operational Efficiency
- **Project start:** {"start":"2026-01-01","end":"2026-01-31"}
- **Project target:** {"start":"2026-04-01","end":"2026-04-30"}
- **Created:** 25/Aug/25 10:15 AM
- **Updated:** 03/Mar/26 9:17 AM

**Description**

-Automate the process once we have a JIRA <> PulseRunner Integration and/or a JIRA <> HubSpot Integration.-

No longer needed as this automation of inventory forecasting will be rolled up into ION.


### [PROD-150](https://impiricus.atlassian.net/browse/PROD-150) — Updating Inventory Scheduling Tools (V1)

- **Initiative:** Inventory Scheduling
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Project start:** {"start":"2025-06-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-09-01","end":"2025-09-30"}
- **Created:** 25/Aug/25 11:31 AM
- **Updated:** 03/Mar/26 9:17 AM

**Description**

#### *Overview:*

- Update Draft Pulse Workflow in Backend
- Establish updated workflow for CS & IMs entering Draft Pulses into PulseRunner
- Update UI for the Inventory Scheduling Tool (by Specialty & List Match)

*Update as of 8/15/25:*

- We’re looking to update the workflow for inputing Pulses into PulseRunner as soon as we have TL & date estimate information
- This will allow us to forecast against Pulses with the tools that are already built
- Additional information outlined [here](https://docs.google.com/document/d/1LCCliW6aU2UzaGyww1vH_54Dw51ZdAkgWCcR2tXz6Lw/edit?tab=t.0)

*Notes from Product Summit on 8/18/25:*

- Scott to Confirm - when can get the Start & End date in the sales cycle?
  - We want to be able to populate Draft Pulses as early as possible
- Create a v2 line as well
- Get physical tools in the hands of Jenn & Todd to get actual feedback from them around how useful the tools are
- CS will be required to ask clients about flighting needs & they will come back with a duration recommendation based on the inventory tool that we have built… this will then allow us to have StartDate & EndDates early on in the process
  - Should this be a part of V2? We don’t want to wait until


### [PROD-54](https://impiricus.atlassian.net/browse/PROD-54) — Update Inventory Scheduler Logic & Workflow

- **Initiative:** Inventory Scheduling
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Roadmap bucket:** Scopt-then-refine
- **Created:** 16/May/25 2:08 PM
- **Updated:** 20/Nov/25 6:17 PM

**Description**

#### Problem Context:

We need to have a “real time” holistic view of the inventory in Impiricus’s ecosystem in order to be able to automate large portions of the forecasting, scheduling, & overlap analysis processes.

This will unlock additional capabilities we can build out in the future (i.e. pacing, pricing, etc.).

#### Desired Outcome:

We plan on building out a POC tool in Sigma that allows us to determine if the backend updates provide the desired scheduling & forecasting abilities without committing to any updates in PulseRunner.

#### Required Actions:

- Build a new table in our database to track all scheduled pulses in the future, allowing us to have a granular view of our available inventory
  - Store what days a NPI isn’t available as the assumption is this will be smaller than storing when NPIs are potentially available
- Determine if we want to recycle the Scheduler Tool logic or create net new logic
  - We will need to analyze the current logic being used & determine if this will be sufficient to meet our needs
- Establish & communicate concept of “Registered Pulses” where we create Pulse objects earlier in the go-live process and update it as we’re provided additional information
  - CS will send Pulse Card to IMs via JIRA as soon as we have a List Match output & potential date range for campaign
*** Both List Match and Date Range can be changed later on
*** IMs make the update to the Registered Pulse and whenever the scheduler process runs it will pick up the changes and re-schedule accordingly 
*** List Match Versioning updates will allow us to automatically pull in the latest List Match to use as the Target List
**** [https://impiricus.atlassian.net/browse/PROD-60](https://impiricus.atlassian.net/browse/PROD-60|smart-link) 
  - Ensure there are safe-guards in place so that these “Registered” Pulses don’t accidentally get set live
*** I.e. mandatory fields & changing of status
*** Do we add a new field called here similar to the _paused_ field?
  - We will want to automate this process in the long term
*** HubSpot → JIRA → PulseRunner
- Develop Sigma Dashboard POC
  - Leverage the backend table to create a Proof of Concept dashboard that automates a large portion of the overlap analysis process and visualizes the scheduled Pulses in our system


### [PROD-140](https://impiricus.atlassian.net/browse/PROD-140) — Define RCS Legal and Implementation Framework

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-08-01","end":"2025-08-31"}
- **Project target:** {"start":"2025-10-01","end":"2025-10-31"}
- **Created:** 25/Aug/25 9:10 AM
- **Updated:** 10/Dec/25 10:34 AM

**Description**

Update as of 10/31/25

- Completed Legal and Implementation Framework
  - [https://docs.google.com/document/d/1q3WSGXHATS4FdkJQFZ6j9Wh3AQqNplwqaw25ckL9tH4/edit?tab=t.0](https://docs.google.com/document/d/1q3WSGXHATS4FdkJQFZ6j9Wh3AQqNplwqaw25ckL9tH4/edit?tab=t.0|smart-link) 

Define Legal and overall RCS commercialization framework

- Distinguish how RCS differs from Pulse/ Spark messages today
- Determine logos and RCS senders from legal perspective
  - current plan 9/12/25
  - Ok to have the brand logo or manufacturer only (no dual logo)
  - Must include "Delivered by DocUpdate" in all initial outreach messages via Pulse, Spark, Ascend
  - Update contracts to include more language related to potential RCS liability
- Discuss with CS how to support RCS brands and different types of content
  - branded 
  - non-branded
  - unbranded
  - surveys
  - Pulse messages
  - Spark messages


### [PROD-141](https://impiricus.atlassian.net/browse/PROD-141) — RCS Demo

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-09-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-10-01","end":"2025-10-31"}
- **Created:** 25/Aug/25 9:11 AM
- **Updated:** 10/Dec/25 10:34 AM

**Description**

Update as of 11/3/25:

- Demos have been completed and are on track
  - Scott/ Or working on an updated flow for Or to present at the Bandwidth Webinar
- Dev completed Reverb Bandwidth demo
- Dev posted another demo here testing RCS via Pulse Runner [https://impiricus1.slack.com/archives/C095PKAQX53/p1761339017485289](https://impiricus1.slack.com/archives/C095PKAQX53/p1761339017485289|smart-link) 

----

Dev to build an RCS demo for a few purposes

- internal testing of all RCS features via DocUpdate RCS (completed by Dev)
- RCS Conference / VC demo for Dev presentation at Reverb (Bandwidth)
- Demo provides a glimpse into functionality that we can support in V1, V2, etc.


### [PROD-143](https://impiricus.atlassian.net/browse/PROD-143) — RCS Fallback Plan

- **Initiative:** RCS
- **Priority:** Medium
- **Reporter:** Anna McDermott
- **Value drivers:** Customer Engagement, Innovation
- **Project start:** {"start":"2025-09-01","end":"2025-09-30"}
- **Project target:** {"start":"2025-10-01","end":"2025-10-31"}
- **Created:** 25/Aug/25 9:12 AM
- **Updated:** 10/Dec/25 10:34 AM

**Description**

Update as of 11/3/25:

- Bandwidth has built in a fall-back plan so this is not something we have to handle
- However, product & dev to still confirm that Bandwidth’s fallback plan meets all product requirements and expectations for sending the fallback Pulse/Spark message
  - ex. can be reported on
  - fallback message acts and operates exactly like original style of Pulse/Spark message=

----

- Per a call with bandwidth on RCS (Rich Communication Services or RBM which is RCS for business messaging)
  - In the first version from Bandwidth, we will not have fallback function
*** If we try to push RCS to a device or carrier that doesn’t support it, they won't automatically convert it into SMS
  - So, we need to develop an internal fallback system to detect failure and send as SMS instead

 

attn: Phil (Basit) & Chris

- getting first campaign approved
- message will fail if no RCS available
- Basit - to find 2 bandwidth campaigns we aren’t currently using
  - 1 - we tell bandwidth to make our RCS campaign
  - 2 - other one keep as is
- For Dev - we need to develop a fallback system-
  - if we get a campaign 1 error code (4754)
  - we will try to trigger the message from campaign 2
  - in future, bandwidth will develop a fallback system
*** if message fails from campaign 1 with error code x, try to push message from campaign b
- no coding changes needed for initial RCS beta
- we just need to choose the bandwidth RCS account
- RCS testing only available for a set of test numbers

*9.15.25 Update from Dev*

- Bandwidth appears to have built a fallback plan into their v1 of RCS and we no longer have to build this - we will want to test and confirm


### [PROD-109](https://impiricus.atlassian.net/browse/PROD-109) — Ascend Response Flows

- **Initiative:** Response Monitoring
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Created:** 15/Aug/25 4:04 PM
- **Updated:** 03/Mar/26 9:19 AM

**Description**

This initiative is focused on establishing a new response workflow for Ascend Products. This work is being captured in [https://impiricus.atlassian.net/browse/INT-2149](https://impiricus.atlassian.net/browse/INT-2149|smart-link). 

- Notes around initial conversation [here](https://docs.google.com/document/d/16m3uT6oFkmmq468_V7JV1fYeYkY1A8JbG35lrLNa8oQ/edit?tab=t.0#heading=h.7fjieckdagug)


### [PROD-157](https://impiricus.atlassian.net/browse/PROD-157) — Response Monitoring Workflow Updates

- **Initiative:** Response Monitoring
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Created:** 25/Aug/25 12:53 PM
- **Updated:** 03/Mar/26 9:13 AM

**Description**

This initiative is focused on ensuring the logic associated with scoring provider sentiment is accurate to ensure that we’re growing & protecting our Network. Also, this focuses on updating the Response Monitoring Workflow to ensure that the manual processes are more efficient and effective, allowing us to scale the number of responses we can accurately monitor. 

*Future ideas include:*

- Establishing a new response workflow for Surveys


### [PROD-158](https://impiricus.atlassian.net/browse/PROD-158) — Update Manual Response Monitoring Workflow

- **Initiative:** Response Monitoring
- **Priority:** Medium
- **Assignee:** Scott Burian
- **Reporter:** Scott Burian
- **Value drivers:** Network Health
- **Project start:** {"start":"2025-09-01","end":"2025-09-01"}
- **Project target:** {"start":"2025-10-10","end":"2025-10-10"}
- **Created:** 25/Aug/25 12:56 PM
- **Updated:** 20/Nov/25 4:03 PM

**Description**

This epic is focused on updating the manual Response Monitoring Workflow to ensure that the manual processes are more efficient and effective, allowing us to scale the number of responses we can accurately monitor. 

We want to update the way QA reviews responses. They currently are copying & pasting data manually from PostGres into a Google Sheet, then reviewing what responses need to be updated row by row in the google sheet, and finally they run StoredProcedures to make the actual updates.

We want to update this workflow without using any engineering resources.

The spreadsheet where we store responses is [here](https://docs.google.com/spreadsheets/d/1p7BgrFHVeHTds1NJGfsw4AqxEus5s1IcyyFVM__URq8/edit?gid=1611089526#gid=1611089526), the data is under the {{Monitoring by Pulse}} tab.

Example of a potential aggregated workflow is [here](https://docs.google.com/spreadsheets/d/1TIicYrzu1ReMsSMVd-PHReunnBu7BSZUs2qwvv3--Is/edit?gid=1969372674#gid=1969372674).

*Update from 9/12/25:*
POC Dashboard of updated workflow [here](https://lookerstudio.google.com/reporting/a32fef23-19bb-42df-9e4c-85c9b56978c1/page/tIBXF).


### [PROD-87](https://impiricus.atlassian.net/browse/PROD-87) — New Signup Flow

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-03-01","end":"2025-03-31"}
- **Project target:** {"start":"2025-05-01","end":"2025-05-31"}
- **Created:** 04/Aug/25 2:38 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-88](https://impiricus.atlassian.net/browse/PROD-88) — Persona Integration

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-03-01","end":"2025-03-31"}
- **Project target:** {"start":"2025-04-01","end":"2025-06-30"}
- **Created:** 04/Aug/25 2:39 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-90](https://impiricus.atlassian.net/browse/PROD-90) — Translator - English to Spanish

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-03-01","end":"2025-03-31"}
- **Project target:** {"start":"2025-05-01","end":"2025-05-31"}
- **Created:** 04/Aug/25 2:40 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-91](https://impiricus.atlassian.net/browse/PROD-91) — Translator Multi-Language Support

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-05-01","end":"2025-05-31"}
- **Project target:** {"start":"2025-07-01","end":"2025-07-31"}
- **Created:** 04/Aug/25 2:41 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-92](https://impiricus.atlassian.net/browse/PROD-92) — Translator UI/UX Improvements

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-06-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-04-01","end":"2025-06-30"}
- **Created:** 04/Aug/25 2:42 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-93](https://impiricus.atlassian.net/browse/PROD-93) — Add SMS Text Box in App (Concierge)

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-05-01","end":"2025-05-31"}
- **Project target:** {"start":"2025-04-01","end":"2025-06-30"}
- **Created:** 04/Aug/25 2:43 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-94](https://impiricus.atlassian.net/browse/PROD-94) — Concierge v2 (multi-select options)

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-06-01","end":"2025-06-30"}
- **Project target:** {"start":"2025-07-01","end":"2025-07-31"}
- **Created:** 04/Aug/25 2:43 PM
- **Updated:** 05/Sep/25 4:32 PM


### [PROD-95](https://impiricus.atlassian.net/browse/PROD-95) — Website and logo redesign

- **Priority:** Medium
- **Reporter:** Andrew Crigler
- **Roadmap bucket:** Refined
- **Project start:** {"start":"2025-05-01","end":"2025-05-31"}
- **Project target:** {"start":"2025-08-15","end":"2025-08-15"}
- **Created:** 04/Aug/25 2:44 PM
- **Updated:** 05/Sep/25 4:59 PM

