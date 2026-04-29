# HCP Unmet Needs × Product Roadmap: Coverage Report

_Generated 2026-04-29 17:12 — 32 unmet needs × 233 roadmap Ideas_

## Executive Summary

| Covered | Partial | Gap | Total |
|---------|---------|-----|-------|
| 3 | 9 | 20 | 32 |

**Top 3 gap categories:**

- **workflow-gap** — 13 need(s)
- **content-gap** — 10 need(s)
- **channel-gap** — 4 need(s)

---

## Gap Leaderboard

_Unmet needs with zero roadmap coverage, grouped by theme. Themes derived from gap categories and reasoning._

### workflow-gap (9 needs)

- **Derrick Laughlin (Concierge)**: "Pharmacy is not listed. Can it be faxed manually?"
  _The HCP is asking about manually faxing a prescription to a pharmacy that is not listed in the system. This is a specific operational workflow need for handling unlisted pharmacies via fax. No roadmap item addresses pharmacy directory completeness, manual fax submission capabilities, or workarounds for missing pharmacy listings. The prescriber-related items focus on features like favorites, controlled substances, and SIG text automation, but none address the fundamental issue of unlisted pharmacies or manual fax alternatives._
- **Melissa Mccarthy (Concierge)**: "Custom: Can I order blood work through this app also?"
  _The HCP is asking about ordering blood work/lab tests through the app. While PROD-300 (LabMap - lab ordering with data validation) and PROD-212 (Add support for ordering labs) exist on the roadmap, both are in 'Parking lot' status with no active development planned. The need for lab ordering functionality represents a clear workflow gap as there is no committed roadmap item that would enable blood work ordering through the platform._
- **Gabriela Flit (Concierge)**: "Generate a PA for a patient synthroid rx"
  _The HCP is requesting to generate a Prior Authorization (PA) for a Synthroid prescription. While the roadmap includes PROD-171 'Prior authorizations - Integrate with a partner' and PROD-162 'Concierge - AI Biologic Coordinator/Prior Auth Facilitation', both are in 'Parking lot' status and focused on integration planning rather than active development. PROD-354 'AI Biologic Coordinator' addresses PA challenges but is also parked and targets biologics specifically, not general medications like Synthroid. No roadmap item provides immediate capability to generate or facilitate PAs for standard prescription medications._
- **Michael Flores (Inbound-SMS)**: "This is fine but I am currently running a clinic and will need to understand how to get 800 units as soon as possible."
  _Dr. Flores is asking about how to obtain 800 units of medication (likely Sunosi samples based on the pulse context) as soon as possible while running a clinic. This is an urgent, operational request for sample fulfillment logistics and guidance. While the roadmap includes sample integration initiatives (PROD-357, PROD-326, PROD-241, PROD-124) that would enable in-app sample ordering, none address the immediate need for guidance on how to expedite obtaining a specific quantity of samples. The HCP needs real-time operational support or workflow guidance for urgent sample acquisition, which no roadmap item covers._
- **Tarig Ahmed (Concierge)**: "Custom: Help obtaining revlimid for a patient with aggressive myeloma"
  _The HCP is requesting help obtaining Revlimid (lenalidomide) for a patient with aggressive myeloma. This is a specific patient access/drug acquisition request for a REMS-restricted medication. While there are roadmap items for sample integrations (PROD-326, PROD-241, PROD-124) and an AI Biologic Coordinator concept (PROD-354, PROD-162), none of these currently address obtaining specialty oncology drugs like Revlimid which require REMS certification and specialty pharmacy coordination. The Concierge team handles these requests manually today, but no roadmap item plans to systematize or automate this specific workflow for restricted oncology medications._
- **Sarah Benett (Concierge)**: "Custom: Why does Ondansetron or Zofran not show up to prescribe?"
  _The HCP is asking why Ondansetron/Zofran does not appear as an option when trying to prescribe. This is a prescriber workflow issue related to drug database availability or search functionality. While there are roadmap items for FDB Drug Database Implementation (PROD-216) and prescriber improvements, none specifically address adding missing medications or fixing drug search/availability issues. The FDB implementation is in 'Parking lot' status and focuses on broader database improvements rather than addressing specific missing drugs in the current system._
- **Mohammad Ansari (Virtual-Coordinator)**: "I was told it's not possible"
  _The HCP response 'I was told it's not possible' is too vague to determine the specific unmet need being expressed. Without knowing what was requested and deemed impossible, no roadmap item can be matched. The response appears to be a brief reply to a Virtual Coordinator interaction about Xarelto, but the actual underlying need (what the HCP wanted that wasn't possible) is not articulated. This represents a workflow or capability gap where the HCP encountered a limitation but the specific nature of that limitation is unknown._
- **Ronald Fields (Virtual-Coordinator)**: "I clicked the link. I do not see an option to just have coupon cards mailed to my office. Is that something you can do?"
  _The HCP is requesting a physical fulfillment capability — having coupon cards mailed directly to their office. While there are roadmap items for sample integrations (PROD-326, PROD-357, PROD-241) and coupon-related initiatives (PROD-353 SingleCare for generic cards, PROD-245 cash cards for generics), none of these address physical mailing of coupon cards to HCP offices. The existing integrations focus on SMS delivery, digital wallet passes, or in-app ordering — not physical mail fulfillment of coupon materials._
- **Rosemarie Tan (Concierge)**: "Custom: I need to make sure that whoever calls the prescriptions in, they need to provide my oral code per state regulation. Thanks!"
  _The HCP (Rosemarie Tan) is requesting that whoever calls in prescriptions must provide her oral code per state regulation. This is a specific prescribing workflow/compliance requirement related to how prescription call-ins are handled. The roadmap includes prescribing-related items (SureScripts ePrescribing, controlled substances, etc.) but none address the specific need for oral code transmission during prescription call-ins to meet state regulatory requirements. This is a workflow/compliance gap in the prescribing process._

### content-gap (7 needs)

- **Yan Yang (Inbound-SMS)**: "does that mean pcp or other specialist can prescribe pcsk9 inhibitors?"
  _The HCP is asking a clinical/regulatory question about whether PCPs or other specialists can prescribe PCSK9 inhibitors (like Repatha). This is a medical information/prescribing eligibility question that requires specific clinical content about drug prescribing authority. No roadmap item addresses providing this type of clinical education content about prescriber eligibility or drug access guidelines. The Virtual Coordinator items focus on platform infrastructure, not specific clinical content delivery, and there is no content initiative that would address prescribing authority questions._
- **Ofobuike Okani (Inbound-SMS)**: "I have a patient on this and she is responding"
  _The HCP's message 'I have a patient on this and she is responding' is sharing a positive real-world experience about a patient on Trodelvy. This appears to be unsolicited feedback about treatment outcomes, which represents a need for a mechanism to capture, acknowledge, and potentially share RWE (real-world evidence) or patient success stories. No roadmap item addresses collecting patient outcome feedback, facilitating RWE sharing workflows, or providing a response mechanism for HCPs reporting treatment successes._
- **Andrew Steehler (Concierge)**: "I would like to have a JOURNAVX journal club"
  _The HCP is requesting a JOURNAVX journal club, which is a specific educational/peer discussion format for a particular drug brand. While the roadmap includes initiatives like 'Independent Initiatives - HCP Peer Zoom Network' (PROD-129) for peer discussions and 'Content creation and distribution' (PROD-286), none of these specifically address journal club formats or JOURNAVX-specific educational programming. The peer network initiative is focused on general condition discussions rather than structured journal club activities around specific medications._
- **Roopa Srikantiah-Saha (Inbound-SMS)**: "Is this available in First line file duct or only second line and beyond?"
  _The HCP is asking a clinical question about Pemazyre's approved indication (first-line vs. second-line treatment for bile duct cancer). This is a request for specific drug labeling/indication information. No roadmap item addresses providing clinical indication data, approved line of therapy information, or drug labeling content to HCPs. The Virtual Coordinator and content-related initiatives focus on delivery mechanisms and MLR-approved messaging workflows, but none specifically address surfacing drug indication or line-of-therapy clinical content._
- **Evan Lang (Inbound-SMS)**: "Just wrote a prescription yesterday"
  _The HCP response 'Just wrote a prescription yesterday' is a confirmation of prescribing behavior for Pemazyre (an Incyte brand), not an unmet need or request for additional support. This appears to be a positive engagement signal rather than a gap in capabilities. However, since no specific need is expressed, there is nothing on the roadmap to match against. The message indicates successful engagement rather than an actionable product requirement._
- **Dennis Brooks (Virtual-Coordinator)**: "I'll take it all"
  _The HCP response 'I'll take it all' is ambiguous and does not articulate a specific unmet need. Without clarity on what 'it all' refers to in the context of Xarelto or the Virtual Coordinator interaction, there is no specific need to match against roadmap items. This appears to be a general expression of interest rather than an actionable unmet need that product roadmap items could address._
- **Dennis Brooks (Virtual-Coordinator)**: "Understand this!"
  _The HCP response 'Understand this!' is too vague to determine a specific unmet need. It appears to be a general expression or possibly a request for clarification/explanation about something, but without more context about what 'this' refers to, it cannot be meaningfully matched to any roadmap item. The source is a Virtual Coordinator conversation for Xarelto, but the message itself does not articulate a concrete need for content, features, or support that can be mapped to existing roadmap initiatives._

### channel-gap (2 needs)

- **Narissa Etwaroo (Inbound-SMS)**: "Can we have one in person"
  _The HCP's request 'Can we have one in person' is asking for an in-person meeting or interaction. The roadmap contains various digital engagement channels (SMS, web chatbot, virtual coordinator, RCS, email) and Rep Connect for virtual/text-based rep interactions, but there are no roadmap items addressing in-person meetings, events, or face-to-face HCP engagement capabilities._
- **Jeffrey Jones (Virtual-Coordinator)**: "any reason a rep cannot visit and bring samples. i really dont need another user name/password to forget. ive been a proponent of xarelto all along. you need to get off your asses and support me if you want continued support from me."
  _The HCP (Jeffrey Jones) explicitly requests an in-person rep visit with samples and expresses frustration about having to manage another username/password. While the roadmap includes Rep Connect (PROD-201, PROD-327) for virtual/SMS-based rep interactions and various sample integration initiatives (PROD-326, PROD-241, PROD-124), none of these address the core need for physical, in-person rep visits. The HCP specifically wants a rep to 'visit and bring samples' — a traditional field force interaction — not a digital alternative. This is a channel gap because the platform focuses on virtual/digital engagement channels rather than facilitating traditional in-person pharmaceutical rep visits._

### data-gap (2 needs)

- **Nizam Jabbour (Concierge)**: "Custom: I'm not seeing my prescriptions for the patients in this anymore"
  _The HCP Dr. Nizam Jabbour is reporting a technical issue where they cannot see their prescription data within the platform. This is a data visibility/access issue or potential bug, not a feature request. None of the roadmap items address prescription data display issues, prescription tracking visibility, or HCP-facing prescription history features. The roadmap contains prescriber-related items (PROD-76 SureScripts ePrescribing, PROD-206 Automated SigText) but these focus on prescription sending capabilities, not on displaying prescription records back to HCPs._
- **James Barr (Virtual-Coordinator)**: "Not the correct doctor have a Edd degree"
  _The HCP response 'Not the correct doctor have a Edd degree' indicates a data quality or targeting issue where James Barr was incorrectly identified or contacted—likely someone with an EdD (Doctor of Education) rather than an MD/DO. This represents a need for better HCP verification, credential validation, or targeting accuracy. While PROD-301 covers State License Validation for prescribers, no roadmap item addresses the broader issue of verifying HCP credentials/degrees or ensuring correct doctor targeting before outreach._

### Partial coverage (adjacent but incomplete)

- **Panna Shah (Concierge)** [channel-gap]: "Virtual event set up"
  _Nearest match: PROD-129. The HCP's request for 'Virtual event set up' relates to organizing virtual meetings or educational events. PROD-129 'Independent Initiatives - HCP Peer Zoom Network' mentions setting up activities for physicians to develop peer networks and discuss conditions via Zoom, which partially addresses virtual event capabilities. However, the roadmap item is focused on peer networking rather than general virtual event setup services that an HCP might need (like speaker programs, webinars, or brand-specific virtual events), making this only a partial match._
- **Ada Lee (Inbound-SMS)** [workflow-gap]: "Lol,. I just gave away my Wegovy pills.  When you stop by next week, can you drop off more of the saving cards that I can give to the patient. Thank you, Ada."
  _Nearest match: PROD-326, PROD-242, PROD-241. The HCP (Ada Lee) is requesting physical savings cards for Wegovy to give to patients during an in-person rep visit. While the roadmap includes sample integration initiatives (PROD-326, PROD-242, PROD-241) that address digital sample ordering workflows, these focus on SMS-based or in-app ordering rather than physical collateral distribution like savings cards. The request for a rep to 'drop off' cards during a visit represents a physical fulfillment/collateral distribution workflow that isn't directly addressed by the digital integration initiatives on the roadmap._
- **Danilo Del campo (Concierge)** [workflow-gap]: "Love to have samples sent over with coupons"
  _Nearest match: PROD-326, PROD-294, PROD-296. The HCP wants samples sent with coupons together. The roadmap includes several sample integration initiatives (PROD-326 Modular Integrations - Samples Partnership Expansion, PROD-294 Concierge Sample Integrations, PROD-296 Continuous development of new integrations for sample ordering) that address sample ordering, but none explicitly cover bundling coupons with sample delivery. Coupon distribution is partially addressed by PROD-353 (SingleCare for generic cards), but this doesn't integrate with the sample fulfillment workflow. The need for a combined samples-plus-coupons delivery is not directly covered._
- **Anna Waldner (Inbound-SMS)** [workflow-gap]: "Thats great.. i could use samples to bridge between ordering and pa completion"
  _Nearest match: PROD-326, PROD-357, PROD-241. The HCP needs samples to bridge the gap between ordering and prior authorization completion. While the roadmap includes sample integration initiatives (QPharma, Medvantx pilots, and broader Samples Partnership Expansion), these focus on streamlining sample ordering workflows rather than specifically addressing the 'bridge' use case where samples are needed temporarily while PA is pending. The need implies a specific workflow for urgent/interim sample fulfillment tied to the PA process, which is not explicitly covered by general sample ordering integrations._
- **Shanda Keaton (Concierge)** [content-gap]: "Information on drug"
  _Nearest match: PROD-302, PROD-286. The HCP's request for 'Information on drug' is a generic content request that could partially be addressed by initiatives like 'Concierge as MSL' (PROD-302) which provides objective medical content for brands, or 'Content creation and distribution' (PROD-286). However, these roadmap items focus on specific content delivery mechanisms rather than a general drug information service. The need is vague, but the roadmap lacks a dedicated comprehensive drug information resource that would fully satisfy an HCP seeking basic drug information on demand._
- **Kathryn Allen (Concierge)** [content-gap]: "Custom: Find financial assistance resources for Medicare and Medicaid patients for Eliquis, Xarelto, Zepbound and Jardiance"
  _Nearest match: PROD-353, PROD-211. The HCP is requesting financial assistance resources specifically for Medicare and Medicaid patients across multiple brands (Eliquis, Xarelto, Zepbound, Jardiance). PROD-353 (Integrate with SingleCare for generic card distribution) addresses generic Rx coupons but not brand-specific financial assistance for government insurance patients. PROD-211 (Surface cash price of medications in app) touches medication pricing but doesn't address the specific need for Medicare/Medicaid financial assistance programs. The roadmap lacks a dedicated initiative for surfacing brand-specific patient assistance programs, copay cards, or financial resources tailored to Medicare/Medicaid populations._
- **Ronald Fields (Virtual-Coordinator)** [workflow-gap]: "I don't want samples. I just want the coupon cards."
  _Nearest match: PROD-326, PROD-242, PROD-241. The HCP (Ronald Fields) explicitly states they don't want samples but just want coupon cards. The roadmap has multiple sample integration initiatives (PROD-326, PROD-242, PROD-241) focused on making sample ordering easier, but these are designed around sample fulfillment workflows rather than standalone coupon/savings card distribution. While the platform touches pharmaceutical access, there's no specific initiative for distributing only coupon cards independent of the sampling process. This is a workflow gap where the HCP wants a subset of the available services (just coupons, not samples) that the current roadmap doesn't explicitly address._
- **Venkatram Nethala (Virtual-Coordinator)** [channel-gap]: "What is this?? And who are you??"
  _Nearest match: PROD-277, PROD-197. The HCP's response 'What is this?? And who are you??' indicates confusion about the Virtual Coordinator outreach identity and purpose. While roadmap items like VC Orchestrator (PROD-277) and Brand-Specific VC Builds (PROD-197) address VC functionality, there is no specific roadmap item addressing improved HCP onboarding, clearer identification of the sender, or introductory messaging that would prevent this type of confused response to initial VC contact._
- **Samuel Rickerl (Virtual-Coordinator)** [content-gap]: "More info on MOA, dosing, and samples if possible"
  _Nearest match: PROD-357, PROD-326. The HCP Samuel Rickerl requests more info on MOA, dosing, and samples for Symbravo. PROD-357 (QPharma Samples Integration for Symbravo) would address the samples request if shipped. However, the MOA and dosing educational content is not explicitly covered by any roadmap item—while Virtual Coordinator builds (PROD-197) deliver brand-specific content, there is no specific initiative guaranteeing MOA/dosing materials will be created for Symbravo. The samples portion is addressable, but the clinical education content (MOA, dosing) represents a content gap._

---

## Validated Roadmap Items

_Roadmap initiatives where at least one HCP unmet need confirms real demand._

| Roadmap Item | Summary | Status | Validating Needs |
|-------------|---------|--------|-----------------|
| PROD-326 | Modular Integrations - Samples Partnership Expansion | Parking lot | Ada Lee (Inbound-SMS); Danilo Del campo (Concierge); Anna Waldner (Inbound-SMS) (+2 more) |
| PROD-201 | Connect - HCP Inbound via QR Code v1 (Intelligent Media) | Now | Samaneh Dowlatshahi (Inbound-SMS); Deomel Soriano (Inbound-SMS); Erika Regis (Inbound-SMS) |
| PROD-241 | Modular Integrations - Samples Pilot (Medvantx) | Parking lot | Ada Lee (Inbound-SMS); Anna Waldner (Inbound-SMS); Ronald Fields (Virtual-Coordinator) |
| PROD-242 | Modular Integrations - Samples Expansion | Parking lot | Ada Lee (Inbound-SMS); Ronald Fields (Virtual-Coordinator) |
| PROD-357 | QPharma Samples Integration (Symbravo) | Parking lot | Anna Waldner (Inbound-SMS); Samuel Rickerl (Virtual-Coordinator) |
| PROD-327 | Connect - Human in the Loop: Create HCP-Rep conversation via Connect automatically | Parking lot | Deomel Soriano (Inbound-SMS); Erika Regis (Inbound-SMS) |
| PROD-129 | Independent Initiatives - HCP Peer Zoom Network | Parking lot | Panna Shah (Concierge) |
| PROD-114 | Connect - Two-way Calling | Parking lot | Samaneh Dowlatshahi (Inbound-SMS) |
| PROD-294 | Concierge Sample Integrations | Parking lot | Danilo Del campo (Concierge) |
| PROD-296 | Continuous development of new integrations for sample ordering | Parking lot | Danilo Del campo (Concierge) |
| PROD-302 | Concierge as MSL | Parking lot | Shanda Keaton (Concierge) |
| PROD-286 | Content creation and distribution | Parking lot | Shanda Keaton (Concierge) |
| PROD-353 | Integrate with SingleCare for generic card distribution | Parking lot | Kathryn Allen (Concierge) |
| PROD-211 | Surface cash price of medications in app | Parking lot | Kathryn Allen (Concierge) |
| PROD-277 | VC Orchestrator v1 | Now | Venkatram Nethala (Virtual-Coordinator) |
| PROD-197 | Brand-Specific VC Builds (Manual) | Now | Venkatram Nethala (Virtual-Coordinator) |

---

## Coverage Matrix

_Roadmap initiatives × count of validating unmet needs._

| Initiative | Roadmap Items | Validating Needs | Confidence |
|-----------|--------------|-----------------|------------|
| Sample Integrations | PROD-241, PROD-326 | 5 | 8 medium |
| Connect | PROD-114, PROD-201, PROD-327 | 3 | 4 medium / 2 high |
| Unassigned | PROD-211, PROD-242, PROD-294, PROD-357 | 6 | 6 medium |
| Concierge | PROD-286, PROD-296, PROD-302 | 2 | 3 medium |
| Virtual Coordinator | PROD-197, PROD-277 | 1 | 2 medium |
| Independent Initiatives | PROD-129 | 1 | 1 medium |
| Prescriber | PROD-353 | 1 | 1 medium |
