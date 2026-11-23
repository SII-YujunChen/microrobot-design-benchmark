# Scenario Design

[All collections](../QUESTIONS.md) · [Download this collection as JSONL](../../data/scenario_design.jsonl)

| Topic | Question IDs | Count |
| --- | --- | ---: |
| Tumor microenvironment | [Q251–Q258](#q251) | 8 |
| Gut monitoring | [Q259–Q266](#q259) | 8 |
| Infection and wound monitoring | [Q267–Q274](#q267) | 8 |
| Vascular and thrombus monitoring | [Q275–Q280](#q275) | 6 |
| Environmental monitoring | [Q281–Q288](#q281) | 8 |
| Industrial biomanufacturing | [Q289–Q296](#q289) | 8 |
| Tissue engineering and biomaterials | [Q297–Q300](#q297) | 4 |

## Tumor microenvironment

### Q251

I want to design a bacterial microrobot that resides in a solid tumor region, activates under hypoxia, and retains a record that it reached the tumor for a time after leaving the hypoxic area. Propose a complete biological circuit covering sensing, memory, output, and safety control. Assess its feasibility and principal risks.

### Q252

Design a biological microrobot that monitors a tumor microenvironment solely by recording whether it has encountered acidity, hypoxia, and inflammatory signals, without directly killing tumor cells. Decide whether it needs multi-input logic gates and memory, and choose a low-risk output.

### Q253

I want a therapeutic tumor robot that navigates first and activates later. It should stay silent while an external field guides it and allow functional protein expression only after reaching the tumor region. Outline a high-level biological circuit and explain the respective roles of external control signals and endogenous tumor signals.

### Q254

Design a biological microrobot that distinguishes ordinary inflamed tissue from tumor tissue by combining several environmental inputs. Provide a sensing, logic, and output architecture and explain which input signals are prone to misclassification.

### Q255

I want a microbial robot to monitor tumor recurrence. It has no therapeutic role. After sensing recurrence-associated signals in vivo, it should form a long-term record that can be read out. Design appropriate sensing, memory, and reporting modules and assess how long-term memory affects host burden and safety.

### Q256

Design a biological microrobot that assesses whether the local immune environment in a tumor is immunosuppressive and produces a low-risk reporter signal. What categories of input signals should it use? Does it need logic gates or memory? Explain how to avoid overinterpreting therapeutic effects.

### Q257

I want a tumor robot whose output activates only when hypoxia, high lactate, and an external trigger occur together. Provide a module-level design and assess the benefits and costs of using three conditions instead of two.

### Q258

Design a biological microrobot to sense tissue stiffening or abnormal extracellular matrix in the tumor stroma. The current database may have no direct mechanosensing component. Propose an alternative sensing strategy and explain how to label gaps in the evidence.

## Gut monitoring

### Q259

I want a gut bacterial robot to monitor inflammatory bowel disease by sensing inflammation-associated signals and producing a detectable reporter signal within a short time. Design the circuit architecture and decide whether it needs long-term memory.

### Q260

Design a gut-resident living therapeutic robot that distinguishes temporary dietary disturbances from sustained inflammation and activates its output only for a persistent abnormality. Design appropriate sensing, temporal filtering, memory, or logic modules and discuss relevant caveats.

### Q261

I want engineered bacteria in the gut to adjust expression to population density, avoiding ineffective expression at low density and excessive burden at high density. Design an architecture combining quorum-sensing communication and feedback control. Assess potential effects of population heterogeneity.

### Q262

Design a microbial robot that detects gut dysbiosis by sensing metabolite changes and issuing a low-risk report without therapeutic intervention. Describe the sensing and output modules, evidence requirements, and risks of misclassification.

### Q263

I want a gut robot that retains a record after a single abnormal exposure, such as an inflammatory flare or a peak in a particular metabolite. Design a single-event memory circuit and readout, and assess whether irreversible memory is appropriate.

### Q264

Design a living diagnostic robot for the gut that responds only to the target inflammatory state amid complex background signals. Decide whether it needs an AND gate, a NOT gate, or threshold-like control. Explain why a simple sensor linked to an output may be insufficient.

### Q265

I want an engineered bacterial robot that persists in the gut over the long term with minimal disruption to the microbiota. Design its safety controls, low-burden expression strategy, environmental sensing, and periodic status reporting. Identify which elements can currently be assessed only in a high-level design review.

### Q266

Design a biological robot for early warning of intestinal inflammation in children. Given this more sensitive use case, specify stricter safety boundaries, output strategies, and evaluation criteria than for a typical adult application.

## Infection and wound monitoring

### Q267

I want a biological microrobot that recognizes bacterial infection signals in chronic wounds and produces a low-risk visual report. Design its sensing, decision logic, and reporter modules and explain how to avoid mistaking ordinary inflammation for infection.

### Q268

Design a microbial robot that recognizes early signals of biofilm formation. It should detect signals associated with collective behavior and record a single biofilm risk event. Propose quorum-sensing, memory, and output modules.

### Q269

I want a biological robot that assesses a wound by sensing pH, oxidative stress, and infection signals together and assigning a risk level. Design a multi-input circuit with graded decision logic rather than a single switch.

### Q270

Design a biological microrobot for early warning of infection on an implant surface. It provides no treatment and issues a report only when it detects infection risk. Explain how you would design surface-associated sensing, memory, and safety restrictions.

### Q271

I want a biological robot that distinguishes acute infection from chronic low-level inflammation. Design temporal control logic, considering transient responses, sustained responses, or state retention, and explain how you would evaluate the rationale for the design.

### Q272

Design a microbial robot that monitors dental plaque by detecting local acidification and changes in microbial population density and producing a nontherapeutic readout. Describe the module architecture and relevant caveats.

### Q273

I want engineered bacteria to serve as event recorders in a localized infection, logging whether they encountered high oxidative stress. Design a sensor–memory–reporter system and identify signals that could cause false positives.

### Q274

Design a biological robot for short-term monitoring of the skin microbiota. Its operation must be low-risk and reversible, and it should avoid long-term residence. Decide whether it needs memory and whether it needs a kill switch or self-limiting control.

## Vascular and thrombus monitoring

### Q275

I want a biological microrobot that recognizes the environment near a thrombus and distinguishes normal blood flow from a local coagulation or inflammatory microenvironment. Design its sensing, logic, reporter, and safety modules.

### Q276

Design a biological microrobot for fast-flowing conditions where contact with the target area may be brief. Decide whether it needs a fast-response sensor, a short-term memory module, or an external trigger, and explain the design risks.

### Q277

I want a diagnostic microrobot that travels through blood vessels. It cannot continuously express a burdensome output and should report only briefly upon detecting an abnormal signal. Design a control architecture with low background expression and low burden.

### Q278

Design a biological microrobot that detects local ischemia by sensing oxygen changes and recording whether a hypoxic event occurred. Provide a high-level circuit design and evaluation metrics.

### Q279

I want an externally driven, magnetically responsive biological robot that keeps its functional modules silent in transit and expresses them only when local signals trigger it at the target. Design the layered logic linking external control to the biological circuit.

### Q280

Design a biological robot that recognizes inflamed vascular plaques while avoiding an excessive response to systemic inflammatory signals. Design multi-input decision logic and a conservative output strategy.

## Environmental monitoring

### Q281

I want a biological microrobot that detects heavy metal pollution in water inside a closed test device and records whether it experienced high exposure. Design a sensor–memory–reporter architecture and explain why the system should be confined to the device.

### Q282

Design a microbial robot for detecting pesticide residues in agricultural soil. It must distinguish the target contaminant from ordinary nutrient changes. Describe the sensing modules, decision logic, and output strategy.

### Q283

I want a biological robot for a wastewater treatment plant that monitors the organic pollution load and adjusts reporter intensity through feedback. Design a sensing, feedback, and output architecture and discuss resource burden.

### Q284

Design a population of microbial robots that detects multiple contaminants and uses different reporters to convey different risk levels. Design multi-input classification logic and explain how to prevent interference among reporters.

### Q285

I want an environmental microbial robot that leaves a long-term record after detecting a contaminant so the event can be read out later. Assess whether irreversible memory is appropriate and discuss containment risks.

### Q286

Design a biological robot to monitor pollution associated with marine microplastics. The database may have no direct microplastic sensor. Explain how to use indirect environmental signals in the design and indicate where evidence is insufficient.

### Q287

I want an environmental robot that detects contaminants without degrading them. Design the output system and explain why you would omit degradation or remediation modules.

### Q288

Design a microbial detection system for a field sampling box. It must be inexpensive, low-risk, and easy to read, with no need for long-term survival. Which modules can be simplified, and which safety modules must be retained?

## Industrial biomanufacturing

### Q289

I want a cell-based robot that senses metabolite accumulation during fermentation and automatically reports production status. Design the sensing, output, and feedback modules and explain why memory may be unnecessary.

### Q290

Design a biological robot that monitors stress in an industrial strain, senses resource burden or stress, and reduces output when the burden becomes too high. Provide a feedback control architecture.

### Q291

I want a monitoring system for metabolic engineering in Yarrowia lipolytica that distinguishes product accumulation from cellular stress. Design the sensing and reporting modules and explain why evidence from a different species cannot be directly extrapolated.

### Q292

Design an engineered bacterial robot for biomanufacturing process optimization that switches expression states across production stages. Describe stage control, sensing, and output, and explain the challenges of timing control.

### Q293

I want a production-strain robot that records whether it experienced a sudden high substrate concentration. Design the memory module and readout and assess whether maintaining the record could affect production performance.

### Q294

Design a population of microbial robots that monitors the collective state in a fermenter. It should use communication to report the population's overall state while filtering single-cell noise. Propose quorum sensing or another form of population-level control.

### Q295

I want a production cell system that automatically reduces expression burden once the product reaches a certain level. Design a metabolic feedback control architecture and discuss the risk of oscillation or instability.

### Q296

Design a biological robot for protein production that automatically adjusts expression levels in response to cellular stress. Design a sensing, control, and output system and give evaluation metrics.

## Tissue engineering and biomaterials

### Q297

I want a biological microrobot in a tissue engineering scaffold to sense local oxygen and nutrient conditions and report the microenvironment inside the scaffold. Design a sensor–output architecture and explain whether memory is needed.

### Q298

Design an engineered cell system that forms spatial patterns inside a biomaterial by using local signals to decide whether to express proteins associated with structure. Propose a sensing, logic, and expression design and discuss spatial cross-talk.

### Q299

I want a biological robot to monitor damage in a soft material by sensing changes in its surroundings and recording damage events. Design the sensing, memory, and readout modules and identify which signals are only indirect indicators.

### Q300

Design a biological robot for monitoring the microenvironment inside an organoid. It must be minimally disruptive, impose a low output burden, and distinguish hypoxia from nutrient deficiency. Provide a complete high-level design, evaluation metrics, and caveats.
