# Extended Scenario Design

[All collections](../QUESTIONS.md) · [Download this collection as JSONL](../../data/extended_scenario_design.jsonl)

| Topic | Question IDs | Count |
| --- | --- | ---: |
| Tumor spatial heterogeneity and metastasis | [Q301–Q310](#q301) | 10 |
| Treatment response, resistance and recurrence | [Q311–Q320](#q311) | 10 |
| Gut microbiome and metabolism | [Q321–Q330](#q321) | 10 |
| Liver, pancreas and systemic metabolism | [Q331–Q340](#q331) | 10 |
| Airways and lung | [Q341–Q350](#q341) | 10 |
| Urinary and renal monitoring | [Q351–Q360](#q351) | 10 |
| Cardiovascular and blood monitoring | [Q361–Q370](#q361) | 10 |
| Nervous system and the gut–brain axis | [Q371–Q380](#q371) | 10 |
| Autoimmunity, allergy and inflammation | [Q381–Q390](#q381) | 10 |
| Infection monitoring and biofilms | [Q391–Q400](#q391) | 10 |
| Oral, skin and mucosal environments | [Q401–Q410](#q401) | 10 |
| Reproductive and maternal health | [Q411–Q420](#q411) | 10 |
| Pediatric, older and vulnerable populations | [Q421–Q430](#q421) | 10 |
| Ex vivo diagnostics and point-of-care testing | [Q431–Q440](#q431) | 10 |
| Wearable and ingestible devices | [Q441–Q450](#q441) | 10 |
| Organoids and organs on chips | [Q451–Q460](#q451) | 10 |
| Tissue regeneration | [Q461–Q470](#q461) | 10 |
| Implants and medical device surfaces | [Q471–Q480](#q471) | 10 |
| Biohybrid robots and external fields | [Q481–Q490](#q481) | 10 |
| Swarm robotics and collective decisions | [Q491–Q500](#q491) | 10 |
| Multistrain and multispecies consortia | [Q501–Q510](#q501) | 10 |
| Temporal logic and biological memory | [Q511–Q520](#q511) | 10 |
| Adaptation, feedback and fault tolerance | [Q521–Q530](#q521) | 10 |
| Individual differences and personalized thresholds | [Q531–Q540](#q531) | 10 |
| Readouts, imaging and communication | [Q541–Q550](#q541) | 10 |
| Cello and design tool integration | [Q551–Q560](#q551) | 10 |
| Water and wastewater monitoring | [Q561–Q570](#q561) | 10 |
| Soil, rhizosphere and agriculture | [Q571–Q580](#q571) | 10 |
| Plant health and endophytes | [Q581–Q590](#q581) | 10 |
| Marine and aquatic systems | [Q591–Q600](#q591) | 10 |
| Veterinary and animal health | [Q601–Q610](#q601) | 10 |
| Food safety and fermentation | [Q611–Q620](#q611) | 10 |
| Industrial production and process control | [Q621–Q630](#q621) | 10 |
| Contained bioremediation and process verification | [Q631–Q640](#q631) | 10 |
| Extreme environments and space missions | [Q641–Q650](#q641) | 10 |
| Education and low-risk demonstrations | [Q651–Q660](#q651) | 10 |
| Biosafety, traceability and regulation | [Q661–Q670](#q661) | 10 |
| Evidence gaps and proxy signals | [Q671–Q680](#q671) | 10 |
| Conflicting or infeasible requirements | [Q681–Q690](#q681) | 10 |
| Clinical translation and staged validation | [Q691–Q700](#q691) | 10 |

## Tumor spatial heterogeneity and metastasis

### Q301

Design a biological microrobot that distinguishes the core of a solid tumor, its invasive margin, and nearby normal tissue. The user's only requirement is to recognize distinct spatial regions. As the agent, choose environmental cues, decide whether multi-input logic and state recording are needed, and assess the risk of misclassification.

### Q302

After working in a primary tumor, a biological microrobot should determine whether it has entered a potential premetastatic microenvironment. Give a complete high-level design. Specify which modules recognize the setting, record events, and provide a low-risk readout, and identify conclusions that remain inferential.

### Q303

Design a microbial robot that distinguishes necrotic tumor regions from viable hypoxic regions. As the agent, decide whether hypoxia alone is sufficient and describe the control logic, output strategy, and evaluation metrics needed to distinguish the two regions.

### Q304

I want a population of biological microrobots to map spatial variation in acidity and oxygen levels inside a tumor rather than report a single average. Design the individual circuit and collective readout architecture and explain how to handle individual variation and spatial cross-talk.

### Q305

Design a biological robot for detecting early micrometastases. Target signals may be weak and transient. Decide whether signal amplification, temporal integration, or memory is needed, and explain how to control false positives.

### Q306

I want a biological microrobot that compares tumor regions near blood vessels with regions farther away. Give a high-level design for sensing, tracking location, output, and safety. Explain the respective responsibilities of external navigation and the biological circuit.

### Q307

Design a biological microrobot that distinguishes immune-infiltrated tumors from immune-excluded tumors. As the agent, identify the environmental cues to observe, decide whether logic gates and memory are needed, and give a conservative conclusion where evidence is insufficient.

### Q308

I want a biological robot to record intermittent hypoxia in a tumor region rather than respond only to the current oxygen level. Design a temporal sensing and memory strategy and assess the trade-offs among record duration, reset capability, and host burden.

### Q309

Design a microbial robot that determines whether tumor acidification is sustained or transient. Show how you break down this broad requirement into a module architecture and identify the modules that are optional.

### Q310

I want multiple biological robots to cover different tumor regions and produce spatial status reports that can be combined. Design a division of labor and consider both communication and independent recording. Assess which architecture is more robust.

## Treatment response, resistance and recurrence

### Q311

Design a biological microrobot that records whether tumor tissue has experienced treatment-related stress, without delivering treatment. Choose the inputs, decide whether reversible or irreversible memory is needed, and specify a low-risk readout.

### Q312

I want a biological microrobot to detect a shift from treatment sensitivity toward tolerance in a tumor after treatment. Give a high-level circuit design and explain how to avoid mistaking general stress for drug resistance.

### Q313

Design a biological robot for early warning of postoperative recurrence that distinguishes normal wound inflammation from a microenvironment associated with tumor recurrence. As the agent, select a suitable multi-signal decision architecture, time window, and output format.

### Q314

I want a robot to compare the local environment before and after radiotherapy and retain a record of an abnormal response following irradiation. Give a complete design and evaluation method, and identify aspects for which existing evidence offers no direct support.

### Q315

Design a biological robot that monitors whether the tumor microenvironment shifts toward inflammatory activation after immunotherapy. Decide whether it needs continuous monitoring, event memory, or population averaging, and discuss relevant caveats.

### Q316

I want a robot to report that a treatment may be effective only when multiple lines of evidence for a response agree. Design the decision logic and a way to report confidence, and assess the trade-off between missed responses and false positives.

### Q317

Design a system to monitor a tumor treatment window. The robot should report during a brief window of effectiveness and automatically fall silent when it closes. Decide whether to use memory, delayed reset, or purely instantaneous control.

### Q318

I want a biological robot to distinguish local recurrence from persistent inflammation after treatment. Break the task into modules suited to this scenario, specify the evidence needed, and explain how to express uncertainty.

### Q319

Design a population of biological robots to compare microenvironmental responses in two candidate treatment regions. Explain how to standardize the readouts across regions, avoid bias caused by population density, and specify evaluation metrics.

### Q320

I want a biological robot that records multiple abnormal events during treatment rather than functioning as a one-time switch. Propose a conceptual multi-event recording architecture and assess whether its added complexity is justified.

## Gut microbiome and metabolism

### Q321

Design a gut robot that distinguishes short-lived postprandial metabolite fluctuations from persistent dysbiosis. As the agent, decide whether temporal filtering, memory, population communication, and a low-burden output are needed.

### Q322

I want engineered bacteria to observe changes in the bile acid profile and the gut inflammatory state together before deciding whether to report an abnormality. Design a high-level sensing and decision architecture and identify evidence gaps in combining the signals.

### Q323

Design a gut microbial robot to monitor imbalances in short-chain fatty acids. The user has not specified a sensor. As the agent, propose module types, threshold control, a readout, and possible sources of error.

### Q324

I want a robot to recognize damage to the intestinal mucosal barrier, but the database has no direct sensor for barrier damage. Propose indirect proxy signals, grade the evidence, and give a conservative assessment.

### Q325

Design a gut diagnostic robot that accounts for circadian variation and avoids classifying normal daily fluctuations as pathological. Decide whether it needs an internal time reference, dynamic thresholds, or memory.

### Q326

I want to distinguish similar metabolic signals in the small intestine and the colon. Design a robot architecture that accounts for spatial location, local conditions, and readout differences, and explain what location information may be lacking.

### Q327

Design a biological robot that records whether the gut ecosystem recovers after an antibiotic disturbance. Decide whether a single-event memory, decaying memory, or continuous trend monitoring is needed, and describe evaluation criteria.

### Q328

I want two engineered bacterial subpopulations to monitor inflammation and metabolic state separately, then combine their observations into an overall assessment. Design a strategy using interstrain communication or independent readouts, and analyze its failure modes.

### Q329

Design a biological robot to capture low-abundance, short-lived gut signals. As the agent, decide whether signal amplification, integration, population coordination, and safety modules are necessary.

### Q330

I want the same gut robot system to work for populations with different dietary habits. Design a strategy for individual baseline calibration and dynamic thresholds and explain how to express uncertainty.

## Liver, pancreas and systemic metabolism

### Q331

Design a biological microrobot for monitoring the progression of fatty liver disease. Break the broad requirement to monitor liver stress into sensing, control, recording, and readout modules, and assess feasibility.

### Q332

I want a robot to distinguish short-term detoxification stress in the liver from a sustained environment associated with fibrosis. Design temporal logic and multi-signal decision rules and explain which inputs offer only indirect evidence.

### Q333

Design a biological robot that monitors metabolic state in the portal vein region and avoids mistaking normal postprandial changes for disease. Provide a high-level architecture and evaluation metrics.

### Q334

I want to record repeated episodes of hyperglycemia rather than measure only the current glucose level. Design a suitable exposure integration or event-counting strategy and explain whether resettable memory is needed.

### Q335

Design a biological microrobot to assess the risk of local pancreatic inflammation. As the agent, decide whether it needs to distinguish general inflammation, tissue injury, and metabolic abnormalities, and propose a module design.

### Q336

I want a robot to recognize an environment associated with cholestasis and issue a graded report. Design multi-input decision logic and graded output, and explain the limitations introduced by changes in the host environment.

### Q337

Design a robot that monitors stress associated with drug metabolism in the liver. It should report the state only, without giving medication advice. Provide a safe high-level circuit design and specify the evidence it requires.

### Q338

I want a biological robot to assess fatty acid load and cellular stress together before deciding whether to record an abnormal event. Design the module combination and assess its resource burden.

### Q339

Design a microbial robot to flag metabolic conditions associated with insulin resistance when there is no single reliable marker. Propose a combination of proxy signals, give a conservative interpretation, and discuss caveats.

### Q340

I want to use biological robots in a liver organoid to compare oxygen, nutrients, and metabolic stress across regions. Design a spatial readout and explain whether it requires memory.

## Airways and lung

### Q341

Design a biological microrobot that monitors infection risk in a mucus environment resembling that of cystic fibrosis. Assess the need for sensing, adaptation of movement, decision logic, reporting, and safety modules individually.

### Q342

I want a robot to distinguish short-lived signals preceding an acute asthma attack from long-term airway inflammation. Design a temporal control and multi-input architecture and explain the risks of misclassification.

### Q343

Design a biological robot that monitors chronic obstructive pulmonary disease. The user's only requirement is to detect a worsening trend. As the agent, propose a complete high-level design and evaluation metrics.

### Q344

I want a robot to record whether an alveolar region has experienced sustained hypoxia without raising an alarm during brief dips in oxygen. Design temporal integration, memory, and reset strategies.

### Q345

Design a biological microrobot for studying a local granuloma-like environment. It should only report local oxidative, inflammatory, and nutritional conditions and involve no pathogen manipulation. Provide a high-level architecture.

### Q346

I want a diagnostic biological robot that can be inhaled and is recoverable or self-limiting. Outline its conceptual operating cycle, reporting method, and safety boundaries.

### Q347

Design a biological robot that works reliably in an environment with abundant mucus and distinguishes obstructed movement from absence of the target signal. Explain how information about its physical state and its biological circuit can support that decision together.

### Q348

I want a robot to distinguish patterns of inflammation resembling bacterial infection from those resembling viral infection, although the evidence may overlap. Design a conservative multi-signal classification strategy and a way to communicate uncertainty.

### Q349

Design an airway monitoring robot that accounts for the respiratory cycle so cyclical oxygen changes do not trigger spurious records. Decide whether filtering, a delay, or an internal reference is needed.

### Q350

I want to use biological robots in a lung-on-a-chip to monitor changes in the epithelial barrier and inflammation. Provide a module design, readout, and validation metrics suited to this in vitro platform.

## Urinary and renal monitoring

### Q351

Design a biological microrobot for early monitoring of urinary tract infections. It must distinguish ordinary fluctuations in urine composition from combinations of signals associated with infection. Give a complete high-level architecture.

### Q352

I want a robot to record whether a local region of the kidney experienced an ischemic event and allow readout after recovery. Decide which memory properties and safety controls it needs.

### Q353

Design a low-risk diagnostic robot that operates in a urine sample to identify metabolic abnormalities. Which modules used in vivo can it omit, and which quality control modules must it retain?

### Q354

I want a robot to distinguish an environment associated with bladder tumor recurrence from ordinary urinary tract inflammation. Design multi-input classification, ways to attribute the evidence, and a conservative output.

### Q355

Design a biosensing robot that tolerates wide fluctuations in urine pH. Explain how to prevent pH from systematically interfering with modules that are not intended to respond to it.

### Q356

I want a contained early-warning robot on a urinary catheter surface to monitor the initial formation of biofilms. Propose sensing, temporal recording, readout, and containment.

### Q357

Design a biological robot to monitor a microenvironment associated with kidney fibrosis where direct evidence is limited. Propose proxy signals, grade the evidence, and specify when a strong recommendation is no longer warranted.

### Q358

I want a robot to distinguish transient proteinuria from the risk of persistent kidney injury. Design temporal logic, memory, and a graded output rather than a one-time switch.

### Q359

Design a system for repeated testing in a urine collection device. It must return to baseline after each round. Decide whether to use a reversible state or a single-use record.

### Q360

I want to monitor oxygen, osmotic pressure, and injury signals in a kidney organoid. As the agent, decide which modules should operate in parallel, which require combinational logic, and how to evaluate the design.

## Cardiovascular and blood monitoring

### Q361

Design a biological microrobot that recognizes the inflammatory state of an atherosclerotic plaque. Decide how to combine local cues related to inflammation, oxidation, and blood flow, and assess specificity.

### Q362

I want a robot to distinguish changes in mechanical conditions from biochemical danger signals across different shear environments. Design a layered architecture for physical sensing and biological circuitry.

### Q363

Design a diagnostic biological robot that monitors a local tendency toward coagulation without performing thrombolysis. Propose high-level sensing, logic, readout, and safety modules.

### Q364

I want a robot to record brief environmental events associated with myocardial ischemia and provide evidence after the event has ended. Design a strategy for memory duration and false-positive control.

### Q365

Design a robot that monitors sepsis risk in blood samples by combining inflammatory and metabolic cues. Provide multi-input decision logic and a way to report confidence.

### Q366

I want a robot to detect abnormalities in blood before storage or transfusion, without entering the body. Design an architecture for a closed in vitro application and explain which safety modules can be simplified.

### Q367

Design a biological robot to monitor abnormal vascular barrier permeability when no direct sensor is available. Propose an indirect proxy strategy and discuss its evidential limits.

### Q368

I want a robot to distinguish systemic inflammation from local vascular inflammation. Design a decision strategy that accounts for space, time, and combinations of signals.

### Q369

Design a population of robots to map microvascular thrombosis risk. Explain how to design the individual response, integrate observations across the population, and normalize the readout.

### Q370

I want robots guided by an external field to leave a state marker only in local areas of vascular abnormality. Define the logic linking external navigation, biological sensing, and memory.

## Nervous system and the gut–brain axis

### Q371

Design a biological robot that indirectly assesses the gut–brain axis through gut metabolites. As the agent, distinguish conclusions supported by gut signals from those that cannot be inferred from them.

### Q372

I want a robot to monitor peripheral signals associated with neuroinflammation without entering the central nervous system. Design sensing, logic, reporting, and a way to express uncertainty.

### Q373

Design a biological robot that records brief metabolic changes potentially associated with seizures. Decide how it should record events, define the time window, and filter nonspecific signals.

### Q374

I want a robot to assess barrier stress and changes in inflammation in a blood–brain barrier chip. Propose in vitro modules, a readout, and evaluation metrics.

### Q375

Design a biological microrobot that identifies the phase of local inflammation after spinal cord injury. Decide whether it needs a temporal state machine, memory, and safety constraints.

### Q376

I want to monitor metabolic and inflammatory changes near the enteric nervous system amid complex environmental signals. Design an architecture for multi-input sensing, thresholds, and conservative reporting.

### Q377

Design a robot that distinguishes normal circadian metabolic changes from chronic changes associated with neurodegenerative disease. Provide a dynamic baseline strategy.

### Q378

I want a robot to map hypoxia and nutrient gradients in a brain tumor organoid without producing treatment recommendations. Design a spatial monitoring strategy and a low-burden readout.

### Q379

Design a biosensing system for multi-biomarker analysis in cerebrospinal fluid samples. Decide whether it needs memory, signal amplification, and sample quality control.

### Q380

I want a robot to use evidence associated with neurodegeneration only for risk stratification, without issuing a definitive diagnosis. Define what its outputs mean and how it should report confidence and limitations.

## Autoimmunity, allergy and inflammation

### Q381

Design a biological microrobot that monitors local inflammation in a joint affected by rheumatoid arthritis. Provide an architecture for multi-signal sensing, grading the state, readout, and safety.

### Q382

I want a robot to record fluctuations in inflammation resembling that seen in systemic lupus erythematosus while avoiding strong conclusions from ordinary responses to infection. Design a conservative method for classification and event recording.

### Q383

Design a surface-based biological robot that monitors the state of psoriatic skin lesions. Decide whether it needs memory, population communication, and reversible output.

### Q384

I want a robot to distinguish chronic low-grade inflammation from acute immune activation. Design a way to discriminate timescales and control thresholds, and discuss limitations.

### Q385

Design a robot that tests samples in vitro for early warning of allergic reaction risk. It should have high sensitivity and avoid interpreting a single signal as a clinical event. Give a high-level design.

### Q386

I want a robot to monitor the balance between infection risk and inflammatory activity after immunosuppressive treatment. Design a report covering both objectives rather than reducing them to a single switch.

### Q387

Design a robot that records relapse events in autoimmune disease. Decide between reversible, decaying, and permanent memory and explain the reasons for your choice.

### Q388

I want a robot to distinguish a treatment-related change in local inflammation from natural fluctuations. Design a baseline calibration strategy, a comparison over time, and an output format.

### Q389

Design a biological microrobot for a complex cytokine network where the database lacks evidence for the full combination. Provide a modular design and specify where inference must stop.

### Q390

I want a low-risk educational system that simulates grading of inflammatory states without producing a real therapeutic output. Design a simplified architecture and metrics for evaluating its use in teaching.

## Infection monitoring and biofilms

### Q391

Design a biological robot that identifies infection risk associated with multidrug-resistant bacteria and produces no antimicrobial effect. Describe sensing, decision logic, reporting, and false-positive control.

### Q392

I want a robot to recognize the progression of biofilm on a catheter surface from early attachment to maturity. Design temporal logic, population signal detection, and state recording.

### Q393

Design a biological microrobot that gives early warning of prosthetic joint infection. It must distinguish sterile inflammation from a pathogen-associated environment. Give a high-level multi-input design.

### Q394

I want a robot to distinguish environments that resemble fungal or bacterial infection, without directly identifying a pathogen species. Design a conservative classification strategy and explain the evidence for its decisions.

### Q395

Design a population of robots to monitor the state of a multispecies biofilm. Explain how to account for different signal sources, manage communication cross-talk, and integrate the outputs.

### Q396

I want to monitor changes in population state after biofilm communication has been disrupted. Provide an observational circuit and evaluation metrics, without designing intervention steps.

### Q397

Design a robot that detects a worsening trend in chronic wound infection. Decide whether it needs to consider signal duration, combine multiple signals, and include a memory module.

### Q398

I want biological robots to detect contamination risk in a closed device for testing hospital surfaces. Design a low-risk, short-lived system with an easy-to-read output.

### Q399

Design a biological robot for research that identifies population changes associated with bacteriophage pressure and only reports population state. As the agent, break down the sensing and collective readout requirements.

### Q400

I want a robot to detect persistent low-level infection without being triggered by occasional contamination. Design temporal integration, confirmation across repeated events, and safety boundaries.

## Oral, skin and mucosal environments

### Q401

Design an oral biorobot that assesses the risk of dental caries. It should consider local acidification, microbial density, and how long these conditions persist, rather than responding to a single low-pH event. Provide a complete high-level design.

### Q402

I want a robot to distinguish active periodontitis from brief inflammation caused by ordinary mechanical irritation. Design its sensing, temporal decision logic, and reporting, and explain what precautions are needed.

### Q403

Design a surface biorobot that monitors the skin microbiome in the context of acne. Decide whether population-level communication, short-term memory, and a reversible readout are needed.

### Q404

I want a robot to monitor whether an eczema lesion is progressing from barrier impairment to worsening inflammation. Propose proxy signals and a way to grade the state of the lesion, and explain the limits of the evidence.

### Q405

Design a biorobot to assess the environment of a burn wound. Its sole function is to report risks associated with infection, oxidation, and tissue stress, without providing treatment. Explain which modules you would include or leave out and why.

### Q406

I want a self-limiting biorobot that operates for a short period to monitor local inflammation in the nasal cavity. Design a minimally intrusive readout and define the safety boundaries.

### Q407

Design a miniature biosensing system to monitor the tear film on the ocular surface. Identify which modules must impose an exceptionally low burden, decide whether memory is needed, and propose evaluation metrics.

### Q408

I want a robot to record whether persistent abnormal signals appear during mucosal repair. Design the observation window, state recording, and an output that can return to baseline.

### Q409

Design a skin-mounted biorobot that uses metabolic information from sweat to monitor trends without diagnosing disease. Propose a dynamic baseline and a way to report confidence.

### Q410

I want a common monitoring architecture for both oral and skin surfaces. Explain which modules can be reused and which must be redesigned for each setting.

## Reproductive and maternal health

### Q411

Design a low-risk biorobot that monitors for vaginal dysbiosis. Specify modules for sensing, assessing the state of the microbial community, reporting, and limiting the robot's own activity. Explain what could cause misclassification.

### Q412

I want a robot to assess the local inflammatory environment associated with preterm birth risk, without drawing definitive clinical conclusions. Design a risk stratification approach using multiple signals and describe its limitations.

### Q413

Design an in vitro biorobot for studying inflammation associated with endometriosis. Decide whether it needs memory, spatial localization, and a long-term readout.

### Q414

I want a biosensing system to distinguish general inflammation from a persistent abnormal state in cervical samples. Describe the architecture for testing a sample, quality controls, and a conservative way to report results.

### Q415

Design an in vitro diagnostic robot that prioritizes safety during pregnancy and only summarizes metabolic and inflammatory trends in maternal samples. Explain which functions you would deliberately leave out.

### Q416

I want to use biorobots in a placenta-on-a-chip to monitor oxygen, nutrients, and stress on the placental barrier. Provide a high-level design and evaluation metrics.

### Q417

Design a robot that tests samples to help assess the metabolic environment in reproductive health. Have the agent decide whether multiple inputs, signal amplification, and memory are needed.

### Q418

I want a robot to accommodate normal menstrual-cycle fluctuations so that it does not mistake cyclical changes for disease. Design a dynamic reference and temporal logic.

### Q419

Design an in vitro biorobot for studying early microbial community transfer in newborns. Its only function should be to record states. Describe the safety architecture and what the evidence can support.

### Q420

I want a general design review framework for maternal and infant applications. Explain what additional constraints these applications require for sensing, readout, privacy, safety, and clinical interpretation.

## Pediatric, older and vulnerable populations

### Q421

Design an in vitro or enclosed biorobot to study the risk of necrotizing enterocolitis in preterm infants. Provide a high-level design for sensing, temporal assessment, and safety.

### Q422

I want a robot to monitor changes in intestinal inflammation in children. It must be more conservative than a system for adults. Explain how to adjust the thresholds, the meaning of its outputs, its memory, and its safety modules.

### Q423

Design an ingestible or sample-based robot to monitor trends in chronic low-grade inflammation in older adults. Propose a low-burden architecture and a strategy for establishing individual baselines.

### Q424

I want a robot to help identify infection risk in immunocompromised people without mistaking ordinary inflammation for infection. Design an approach that combines multiple signals and reports uncertainty.

### Q425

Design an in vitro biosensing system for monitoring risk during post-chemotherapy neutropenia. Explain which signals can support risk stratification and where extrapolation would be unjustified.

### Q426

I want to use biorobots to monitor sepsis-like trends in samples from intensive care patients. Propose a multi-input architecture, a way to update assessments over time, and controls for false alarms.

### Q427

Design a system that monitors metabolism and inflammation in samples from dialysis patients. Decide whether it needs memory, normalization across batches, and individual calibration.

### Q428

I want a biorobot to monitor environmental changes associated with post-transplant rejection without substituting for a clinical diagnosis. Design its evidence integration and reporting, and define its safety boundaries.

### Q429

Design a sample-based robot that provides early warning of an acute crisis in a rare metabolic disease. Propose a strategy for rapid response, redundant confirmation, and handling false positives.

### Q430

I want a low-risk biological testing system for home use. Have the agent decide which modules to simplify and which quality controls and safety mechanisms to retain.

## Ex vivo diagnostics and point-of-care testing

### Q431

Design a biosensing system that analyzes trends in multiple cytokines in blood samples. Describe multi-input classification, built-in controls, a low-risk readout, and evaluation metrics.

### Q432

I want to determine quickly from urine samples whether a metabolic abnormality persists or a single result is an outlier. Design the batch calibration, thresholds, and reporting architecture.

### Q433

Design a biorobot that jointly assesses inflammatory and metabolic states in stool samples. Address sample complexity, background interference, and quality control.

### Q434

I want a reusable system for assessing the state of saliva samples. Decide whether memory, a reset mechanism, and multiple reporters are needed.

### Q435

Design a biosensing system that classifies infection risk in sputum samples. Propose a combination of signals, a way to correct for the mucus background, and a conservative output.

### Q436

I want a robot to analyze hypoxia, acidity, and inflammation in surgical margin samples without diagnosing tumors. Design a spatial readout and explain its limitations.

### Q437

Design a biorobot to monitor the condition of perfusate from an ex vivo organ. Propose a multilayer report covering metabolic status, damage, and contamination risk.

### Q438

I want one platform to handle blood, urine, and saliva samples. Explain which modules can be reused and which must be recalibrated for each sample type.

### Q439

Design a bedside robot for testing multiple indicators. The result should be simple to interpret while preserving information about the strength of the evidence. Show how detailed internal assessments feed into a concise output.

### Q440

I want the system to recognize poor sample quality automatically and withhold strong conclusions when the sample is inadequate. Design quality-control sensing, abstention logic, and result flags.

## Wearable and ingestible devices

### Q441

Design a biorobot in an ingestible capsule that records environmental changes along the digestive tract. Describe temporal or spatial encoding, readout, and the architecture for limiting its activity.

### Q442

I want a biorobot in a skin patch to monitor long-term metabolic trends through sweat. Design a dynamic baseline, signal-drift correction, and a low-risk output.

### Q443

Design a contact-lens system for monitoring tears. Decide which sensing and readout modules are feasible and which biological functions should be omitted given the constraints of this setting.

### Q444

I want to incorporate biorobots into a smart wound dressing to monitor pH, oxidation, and infection risk. Describe the module architecture, short-term memory, and how the result can be read externally.

### Q445

Design an enclosed biosensing system in an oral retainer to record overnight acidification events. Decide whether population-level communication and resettable memory are needed.

### Q446

I want to place an early-warning robot for infection in an enclosed chamber attached to a urinary catheter. Design the state detection, sensing of surface-associated signals, readout, and containment.

### Q447

Design a retrievable, short-term diagnostic implant whose internal biorobots leave a record only under abnormal conditions. Specify the operating cycle and safety strategy.

### Q448

I want a wearable biosensor that records episodes of exposure to airborne pollutants. Explain how environmental sampling, biological signal transduction, and the user's readout connect.

### Q449

Design a robot that requires no continuous electrical power and uses an accumulated biological state as its readout. Decide whether memory and signal amplification are necessary.

### Q450

I want to compare three approaches to the same intestinal problem: an ingestible device, a surface-mounted device, and in vitro sample testing. Compare their architectures and risks, and state when you would recommend each.

## Organoids and organs on chips

### Q451

Design a biorobot that monitors the spatial distribution of oxygen and acidity inside a tumor organoid. Describe localization, readout, and how to minimize disturbance.

### Q452

I want a robot in a gut-on-a-chip to distinguish barrier injury, inflammation, and metabolic abnormalities. Design its multiple inputs, how its assessment updates over time, and evaluation metrics.

### Q453

Design a liver-on-a-chip monitoring system that tracks metabolic stress and trends in tissue damage at the same time. Decide whether memory and region-specific readouts are needed.

### Q454

I want to track changes at the air–liquid interface and the inflammatory state in a lung-on-a-chip. Propose an architecture that analyzes the physical environment and biological signals together.

### Q455

Design a biorobot that monitors maturation and injury in kidney organoids. Have the agent decide which signals indicate developmental state and which indicate stress.

### Q456

I want to monitor the risk of altered permeability and changes in inflammation in a blood–brain barrier chip. Design indirect sensing and graded reporting, and explain the limits of the evidence.

### Q457

Design a robot for studying the interaction between flow conditions and inflammation in vascular organoids. Explain how to organize the mechanical and biochemical modules into layers.

### Q458

I want to use the same type of robot to convey information about organ states across a multi-organ chip. Design a scheme for communication between chambers, identity tagging, and data integration.

### Q459

Design a biorobot that monitors spatial patterns in developing organoids. Decide whether long-term memory, reversible reporting, or division of labor across the population is needed.

### Q460

I want to use a robot to compare how the same organoid responds to different treatments. Design internal standards, batch normalization, and outputs that can be compared across treatments.

## Tissue regeneration

### Q461

Design a biorobot that monitors oxygen, nutrients, and inflammation in a scaffold for bone repair. Describe sensing, state classification, and a minimally disruptive readout.

### Q462

I want a robot to assess the environment of degenerating cartilage and distinguish the effects of mechanical stress from those of inflammation. Design multimodal sensing and a conservative way to draw conclusions.

### Q463

Design a monitoring biorobot for research on promoting vascularization. It should not release therapeutic factors directly. Describe how to record spatial states and propose evaluation metrics.

### Q464

I want to monitor local oxidation, nutrients, and cellular stress in a nerve regeneration scaffold. Decide whether long-term memory and reversible reporting are needed.

### Q465

Design a biorobot to monitor skin graft integration. Describe a layered architecture that covers barrier integrity, inflammation, hypoxia, and infection risk.

### Q466

I want a low-burden robot in a cardiac patch to monitor ischemia and changes in the mechanical environment. Design a way to coordinate the external field, the physical state, and the biological readout.

### Q467

Design a robot for studying mechanical and inflammatory states during tendon repair. Propose indirect proxies for mechanical conditions and identify gaps in the evidence.

### Q468

I want a robot to record the order in which abnormal events occur during wound healing. Design an architecture for recording their sequence and reading it out afterward.

### Q469

Design a biorobot that monitors extracellular matrix remodeling over time. Decide whether spatial sampling by a population of robots, temporal integration, and multiple reporters are needed.

### Q470

I want to compare microenvironments in different regions of a regenerative scaffold. Describe design principles for distributing the population, normalizing the data, and avoiding disruption to the tissue.

## Implants and medical device surfaces

### Q471

Design an enclosed biorobot for early warning of infection around an orthopedic implant. Describe surface sensing, how to distinguish sterile inflammation, the readout, and containment.

### Q472

I want to monitor inflammatory trends associated with restenosis near a vascular stent. Describe a high-level design for sensing, recording changes over time, and reporting with minimal interference.

### Q473

Design a biosensing system that monitors inflammation in the pocket surrounding an implanted cardiac device. Decide whether it requires long-term residence, periodic reporting, or memory of events.

### Q474

I want to monitor the tissue response around a neural electrode. Design an architecture that jointly assesses the physical interface, biochemical environment, and condition of the material.

### Q475

Design a robot that provides early warning of biofilm formation on a central venous catheter. Describe how to detect early population-level signals, confirm them over time, and control false positives.

### Q476

I want a short-term monitoring robot on a dental implant surface that distinguishes mechanical irritation from infection risk. Design its decision logic and a mechanism for safe cessation of operation.

### Q477

Design a biorobot that monitors the risk of fouling or encapsulation on the surface of a continuously operating sensor. Explain how it would recognize device failure and distinguish it from a physiological abnormality.

### Q478

I want a biological system that actively reports the degradation state of an implant material without changing the degradation process. Propose proxy signals and a readout.

### Q479

Design a biorobot that monitors infection and healing around smart sutures. Decide whether local memory and external readout are needed.

### Q480

I want a general design framework that can be adapted to different implants. Explain which sensing, control, safety, and data modules can be standardized.

## Biohybrid robots and external fields

### Q481

Design a magnetically navigated biorobot. During movement, its only task is positioning. Once it reaches its target, local conditions should determine whether it reports. Describe the layered logic for physical control and the biological circuit.

### Q482

I want to use ultrasound as an external enabling signal while also requiring the robot to recognize its target environment. Design a dual-gate architecture and assess its failure modes.

### Q483

Design a light-controlled biorobot for tissue that can be illuminated directly. Decide which functions light should control and which should depend on endogenous signals, and explain whether memory is necessary.

### Q484

I want to use a temperature change as a brief external trigger without letting temperature alone determine the final output. Design logic that combines the external trigger with confirmation from the local environment.

### Q485

Design a biorobot that uses an electric field for guidance or to mark a state. Explain how to distinguish the physical effects of the field, the cellular response, and the behavior of the output circuit.

### Q486

I want a robot to sense material deformation or mechanical stress, but the database lacks components that sense these directly. Propose physical proxy signals and indirect sensing, and explain their limitations.

### Q487

Design a robot that can write sensing results to memory only during a specified external-field time window. Describe the temporal gate and how the architecture prevents unintended recording.

### Q488

I want to decouple navigation completely from functional expression so that navigation failure leaves all outputs inactive. Design the enabling layer, the environmental sensing layer, and the fallback layer.

### Q489

Design a biorobot that automatically switches to low-risk monitoring when the external field is unavailable. Describe state transitions, safe default behavior, and the reporting strategy.

### Q490

I want to combine three conditions: magnetic navigation, local hypoxia, and population density. Have the agent decide whether all three should be mandatory gates and evaluate the trade-off between complexity and reliability.

## Swarm robotics and collective decisions

### Q491

Design a population of biorobots that produces a valid report only after population density reaches a threshold. Address communication, thresholding, heterogeneity, and failure control.

### Q492

I want to divide a population into three groups: sensors, recorders, and reporters. Design their division of labor, information exchange, and a fallback if any one group fails.

### Q493

Design a population of biorobots to cover a large area. It should avoid double-counting caused by high local densities. Propose spatial sampling and normalization strategies.

### Q494

I want a population to report an anomaly only when a majority agrees. Design the consensus logic, explain how to handle anomalous individuals in the minority, and assess communication noise.

### Q495

Design a population of robots that automatically allocates work across regions. Decide whether it needs local quorum sensing, resource sensing, and role switching.

### Q496

I want to identify individuals with abnormally high expression and limit their influence on conclusions drawn from the population. Describe a population-level quality-control architecture.

### Q497

Design a collective system that retains local records during communication outages and merges them when communication resumes. Explain how to design individual memory and synchronize the population.

### Q498

I want the population to complete three stages in order: localization, confirmation, and reporting. Design temporal control across individuals and a way to verify when each stage is complete.

### Q499

Design a population-level system that records events over long periods without relying on the long-term survival of individual cells. Propose distributed recording and redundancy.

### Q500

I want to compare centralized and decentralized decision-making in a population of biorobots. Explain when each architecture is suitable and what risks each presents.

## Multistrain and multispecies consortia

### Q501

Design a system with two engineered bacterial strains, one for sensing and one for recording. Describe how information is transferred, how the strains are distinguished, how their proportions are kept stable, and how the system should handle the absence of either strain.

### Q502

I want to build a biorobot system in which bacteria and yeast work together. Have the agent decide which functions suit each host and explain the limitations of communication across species.

### Q503

Design a cooperative system in which anaerobic bacteria handle local sensing and facultative anaerobes handle external reporting. Describe the spatial division of labor, signal transfer, and safety constraints.

### Q504

I want to assign diagnosis and treatment to different strains, but only a high-level design review is allowed at this stage. Explain how to isolate the functions, reduce crosstalk, and preserve traceability.

### Q505

Design a biorobot consortium that can automatically maintain the relative proportions of different strains. Describe an architecture for sensing the state of the population, applying feedback control, and warning of imbalance.

### Q506

I want several strains to use different communication channels to avoid signal crosstalk. Propose a conceptual design for orthogonal communication and for detecting erroneous messages.

### Q507

Design a system in which each strain has independent containment and the population can still cooperate. Explain how the safety and communication layers can work together.

### Q508

I want one strain to take over some of the functions of another if the latter fails, even at reduced capacity. Describe the redundant design and the limits of what it can do.

### Q509

Design a biorobot platform with interchangeable modular strains. Explain how to organize interface standards, the transfer of evidence to replacement strains, and compatibility assessment.

### Q510

I want to compare a complex circuit in a single strain with division of labor across multiple strains. Evaluate both options in terms of burden, stability, communication, validation, and safety.

## Temporal logic and biological memory

### Q511

Design a biorobot that distinguishes a short pulse from a sustained input. Have the agent decide whether to use temporal integration, delayed gating, or memory, and propose evaluation metrics.

### Q512

I want a robot to record how many times the same abnormal event has occurred, beyond simply recording whether it has ever occurred. Propose a conceptual architecture for event counting or graded memory.

### Q513

Design a robot that reports only after it encounters signal A followed by signal B. Address how it distinguishes event order, retains state, and handles events arriving in the wrong order.

### Q514

I want a robot to output different risk levels according to how long an input persists. Design the time thresholds, the different states, and the readout.

### Q515

Design a biological memory system that can be reset safely. Explain whether the reset would be driven by an external field, a return to normal environmental conditions, or internal decay, and assess the risks.

### Q516

I want a memory that naturally weakens over time to reflect recent exposure rather than lifetime exposure. Design the fading memory and its calibration strategy.

### Q517

Design a cumulative-exposure robot that integrates repeated low-intensity signals. Address integration, background-noise suppression, and handling of saturation.

### Q518

I want the system to avoid frequent switching as the signal fluctuates near a threshold. Design hysteresis or dual-threshold control and explain how it affects sensitivity.

### Q519

Design a robot that distinguishes normal circadian cycles from persistent pathological signals. Describe a periodic reference, temporal logic, and a conservative output.

### Q520

I want a robot to retain a simplified event timeline that records onset, persistence, and recovery. Design a multistate record that goes beyond a single switch.

## Adaptation, feedback and fault tolerance

### Q521

Design a biorobot that recognizes long-term sensor drift and automatically reduces the strength of its conclusions. Describe the calibration reference, anomaly detection, and safe fallback behavior.

### Q522

I want the system to report reliably even if some cells mutate or lose a module. Design redundancy, population voting, and failure flags.

### Q523

Design a robot that monitors its own resource burden and automatically reduces nonessential expression. Describe burden sensing, feedback, and task priorities.

### Q524

I want two different sensing channels to cross-check each other. If either channel is abnormal, the system should enter a conservative mode. Design the redundant sensing and conflict handling.

### Q525

Design a system that can retain an event record even if the output module fails. Explain how to decouple recording from reporting.

### Q526

I want to prevent sustained oscillations in a feedback controller. Describe a high-level stability strategy, risks from delays, and how to evaluate stability.

### Q527

Design a robot that automatically adjusts its threshold to background environmental conditions. Explain how self-calibration can avoid adopting a pathological state as the new normal.

### Q528

I want the population to return to a consistent state after a temporary communication outage. Design local buffering, resynchronization, and conflict resolution.

### Q529

Design a robot that progressively builds confidence in a noisy environment. Describe how it accumulates evidence, discounts past evidence, and reports confidence.

### Q530

I want the system to recover safely from a false trigger without retaining a permanently incorrect conclusion. Design an architecture for error correction, reset, or secondary confirmation.

## Individual differences and personalized thresholds

### Q531

Design a biorobot that adjusts its alarm threshold to each patient's own baseline. Describe initial calibration, dynamic updating, and a way to prevent baseline drift.

### Q532

I want the same robot system to accommodate heterogeneity across tumor regions. Design local thresholds, spatial tagging, and integration of results.

### Q533

Design an intestinal robot that accounts for differences in diet and microbiome background. Explain which modules are fixed, which parameters need individualization, and how to avoid overfitting.

### Q534

I want the system to produce conservative outputs in a population with widely differing immune states. Describe stratified assessment, confidence intervals, and conditions for abstaining.

### Q535

Design a robot that automatically adjusts its time window for different age groups. Explain how age-related changes in baseline conditions enter the decision.

### Q536

I want to reuse the same functional architecture in different host chassis. Describe module replacement, how to check the evidence for each host, and which parts cannot be transferred directly.

### Q537

Design a sample-based robot that automatically normalizes results to the endogenous background of each batch of samples. Describe internal controls and quality gates.

### Q538

I want the robot to learn an individual's long-term normal range dynamically without continually adapting to an abnormal state. Design the update rate and a mechanism to freeze updates when anomalies occur.

### Q539

Design a personalized robot that integrates metabolic, inflammatory, and physical information about the environment. Explain how to weight the inputs and handle conflicting evidence.

### Q540

I want the system to tell users which conclusions come from individual calibration and which come from the general literature. Design the output structure and fields needed for traceability.

## Readouts, imaging and communication

### Q541

Design a biorobot that uses fluorescence readout in a low-background environment. Explain the trade-offs among signal strength, leakage, resource burden, and reversibility.

### Q542

I want to use luminescence rather than fluorescence for readout at a distance. Have the agent compare energy requirements, background, timing, and suitable settings.

### Q543

Design a low-risk system that uses an enzyme-driven color change for a simple visual readout. Explain amplification, saturation, and the limits of quantification.

### Q544

I want a robot to leave an in vivo state that can be detected indirectly by external imaging, without specifying how to perform the imaging. Provide a module-level design and assess feasibility.

### Q545

Design a system with multiple reporters that can report three states simultaneously. Discuss orthogonality, spectral or signal crosstalk, burden, and interpretation of the results.

### Q546

I want the output to be resettable for continuous monitoring. Explain how to choose among a reversible reporter, state decay, and external readout.

### Q547

Design a population of robots that generates a spatial map. Explain how each individual carries location information or a region label and how those records are combined.

### Q548

I want a biorobot and an electronic device to exchange only simple state codes. Describe a high-level interface that converts a biological state into a machine-readable signal.

### Q549

Design a readout system for long-term archiving. It should require no real-time observation on site and allow the record to be read later. Decide how memory and reporting should divide these functions.

### Q550

I want the system to normalize its output internally to reduce the effects of differences in cell count. Describe the reference channel, ratiometric readout, and handling of outliers.

## Cello and design tool integration

### Q551

A user has a requirement for two-input combinational logic. Have the agent decide which parts can be assigned to Cello 2.0 and which evidence checks BioCircuit Agent must still perform.

### Q552

Design a hybrid system with combinational logic and irreversible memory. Separate the Cello-compatible subcircuit from the subsystem outside Cello's scope, and explain the interface risks.

### Q553

I want to generate a logic design plan for a host that Cello supports, but the input sensor is missing from the available library. Describe how to route the task between tools, possible alternatives, and when to stop compilation.

### Q554

Design a scenario in which a Cello library does not match the user's chosen host. Have the agent identify the host mismatch and propose a high-level way to correct it.

### Q555

I want the agent to draft Verilog from natural language, but it must first verify that the logic is fully specified. Design the requirements parsing, truth-table checks, and error messages.

### Q556

Design a pipeline that uses local RAG, life-science-research, and Cello together. Explain what each tool does and how to avoid duplication and conflicts.

### Q557

I want the agent to review Cello's output truth table and its activity and toxicity summaries. Describe the review steps and identify conclusions that the predictions cannot support.

### Q558

Design a workflow that converts Cello output to SBOL before adding it to a knowledge base. Explain how to preserve provenance, versions, and links to the supporting evidence.

### Q559

I want to compare designs from two Cello libraries for the same logic. Identify comparable metrics and host constraints, and explain how to decide which design to recommend.

### Q560

Design a fallback strategy for tool failure. What high-level information should the agent still provide if Cello is unavailable or compilation fails?

## Water and wastewater monitoring

### Q561

Design an enclosed biorobot that monitors the risk of heavy-metal contamination in drinking water. Describe graded alarms, memory, readout, and containment.

### Q562

I want the system to monitor trends in antibiotic residues in wastewater without proposing treatment. Design the sensing, background correction, and long-term trend recording.

### Q563

Design a population of microbial robots that monitors eutrophication risk. Explain how to combine nutrient signals, changes in oxygen, and readouts from the population.

### Q564

I want a robot to distinguish the risk of pathogen contamination from a general increase in organic load. Describe multi-input discrimination, what evidence is needed, and conservative reporting.

### Q565

Design an industrial effluent monitoring robot that tracks acidity or alkalinity, oxidation, and specific classes of pollutants. Decide which inputs should be mandatory gates and which should grade the result.

### Q566

I want to use the same robot at different stages of wastewater treatment to track treatment performance. Design stage recognition, dynamic baselines, and a way to compare results.

### Q567

Design an enclosed biosensing system for studying proxy signals of viral contamination. Explain which indirect clues it can detect and what conclusions those clues cannot support.

### Q568

I want to monitor environmental stress associated with microplastics, but a direct sensor is unavailable. Propose proxy indicators, levels of evidence, and a way to avoid overconfident recommendations.

### Q569

Design an aquatic robot that adapts to rapid changes in salinity. Explain how background environmental conditions systematically affect the sensor, the output, and the state of the population.

### Q570

I want to monitor the progress of water treatment in an enclosed bioreactor and decide when to stop observing. Provide a high-level design for assessing state and determining when to stop.

## Soil, rhizosphere and agriculture

### Q571

Design a biorobot that monitors the risk of pesticide residues in soil. Describe target recognition, how to rule out background effects from nutrients, and the readout strategy.

### Q572

I want a robot to assess both nitrate excess and nitrate deficiency in soil. Design a graded response in both directions instead of a single alarm.

### Q573

Design a microbial robot that records stress in saline–alkaline soil. Decide whether it should provide an immediate response, cumulative memory, or a record of seasonal trends.

### Q574

I want a robot to distinguish a short drought from long-term water stress. Describe temporal logic, how to recognize recovery, and a low-burden readout.

### Q575

Design a rhizosphere robot that uses root exudates to determine whether it is near a target plant region. Address localization, specificity, and differences across plants.

### Q576

I want the system to monitor the risk from soilborne pathogens without spreading in an open environment. Describe an architecture for enclosed sampling, a short operating lifespan, and reading out the results.

### Q577

Design a state-recording system for farmland contaminated by heavy metals. Address soil heterogeneity, spatial sampling, and aggregation of results across the population.

### Q578

I want a robot to help assess whether fertilizer use is imbalanced. Design an approach that combines signals from multiple nutrients, uses proxies for plant condition, and reports uncertainty.

### Q579

Design a population of microbial robots to study changes in soil carbon cycling. Explain how to distinguish disturbances caused by the robots' own metabolism from the environmental changes under study.

### Q580

I want to use a resettable robot for repeated monitoring in a closed greenhouse soil system. Describe reset, batch controls, and containment.

## Plant health and endophytes

### Q581

Design a plant-associated biorobot that provides early warning of crop disease. Describe host signals, pathogen risk, confirmation over time, and low-risk reporting.

### Q582

I want a robot to distinguish nitrogen deficiency in plants from generally slowed growth. Propose proxies based on multiple signals, identify limits in the evidence, and describe an output strategy.

### Q583

Design an endophytic or rhizosphere robot that records whether a plant experienced heat stress. Assess how long its memory should last and what burden it places on the plant.

### Q584

I want a robot to recognize brief environmental events before and after frost and provide a record afterward. Design a way to capture temperature events and represent the recovery state.

### Q585

Design a robot that monitors trends in plant pathogen colonization. Its only role is early warning, with no disease-control function. Describe a multistage readout and how to control false alarms.

### Q586

I want the system to adjust its threshold to the plant's growth stage. Design stage recognition, a dynamic reference, and a strategy to avoid misidentifying the stage.

### Q587

Design an enclosed biosensing system for monitoring spoilage risk in harvested fruit and vegetables. Propose a combination of metabolic, gas, and microbial signals.

### Q588

I want to use multiple robots in a greenhouse to monitor different plants and summarize their collective state. Design a way to track identity and location and to normalize the data.

### Q589

Design an endophytic plant robot that cannot persist for long outside its host. Provide a high-level review of its containment design and its dependence on the host.

### Q590

I want to compare a rhizosphere robot with a robot attached to a leaf surface for the same disease-warning task. Compare their full architectures, including strengths and weaknesses.

## Marine and aquatic systems

### Q591

Design a biological microrobot that monitors coral bleaching risk. Integrate cues from temperature, light, oxidation, and the state of the symbiosis, and explain which evidence is indirect.

### Q592

I want to monitor the risk from fish pathogens in a closed aquaculture system. Address water sampling, population-level signals, reporting, and containment.

### Q593

Design a population of microbial robots that provides early warning of harmful algal blooms. Describe nutrient signals, population density, proxies for toxicity, and graded outputs.

### Q594

I want a robot to record exposure to oil pollution without degrading the oil. Design the event memory, spatial sampling, and subsequent readout.

### Q595

Design a population of robots to monitor the boundaries of hypoxic marine “dead zones.” Describe spatial distribution, how to record oxygen history, and data integration.

### Q596

I want the system to adapt to a marine environment where salinity and temperature change at the same time. Design background calibration and a way to separate the target signal from these changes.

### Q597

Design an enclosed biosensor for indirect monitoring of toxin risk in shellfish. Explain why its readout cannot directly establish whether the shellfish are safe to eat.

### Q598

I want to monitor changes in microbial communities on the surfaces of microplastics. Design an approach that accounts for attachment state, population communication, and environmental proxy signals.

### Q599

Design a robot to monitor long-term trends in a recirculating aquaculture system. Explain how to reset it repeatedly, maintain population stability, and minimize disturbance.

### Q600

I want to use biorobots for a short period inside a deep-sea sampler to record pressure, oxygen levels, and chemical gradients. Describe an architecture for tolerating these conditions, retaining the information in memory, and reading it out after retrieval.

## Veterinary and animal health

### Q601

Design a contained biosensing system to monitor the early risk of mastitis in dairy cows. Specify indicators of inflammation, proxies for pathogen presence, sample quality controls, and a cautious way to report the findings.

### Q602

I want a robot to monitor rumen pH and fermentation in ruminants and distinguish brief fluctuations from persistent imbalance. Design the temporal logic and the population-level readout.

### Q603

Design a sample-based biological robot to monitor infection risk in poultry flocks. Explain how it would capture flock-level trends, account for differences between birds, and control false alarms.

### Q604

I want to monitor stress and pathogen risk in farmed fish. Design a way to combine proxy signals from the water and the host.

### Q605

Design a low-risk in vitro system to monitor trends in chronic inflammation in pets. Decide whether memory and individual baselines are needed.

### Q606

I want an early-warning system for exposure to pathogens of animal origin, without enhancing or culturing pathogens. Outline how a contained system could detect evidence of exposure and define its safety boundaries.

### Q607

Design a sample-based robot for studying reproductive health in livestock. Explain how to account for cyclical changes and individual differences, and what the output would mean.

### Q608

I want to use a short-term monitoring robot in veterinary wounds to distinguish healing, inflammation, and infection risk. Outline the high-level modules and the robot’s exit mechanism.

### Q609

Design a distributed robotic system to track the overall condition of a herd. Explain how it would sample individual animals, aggregate herd-level findings, and handle individuals with anomalous results.

### Q610

I want to compare design requirements for biological robots in human and veterinary use. Explain how host environment, deployment, safety, readout, and regulation would affect the architecture.

## Food safety and fermentation

### Q611

Design a contained biosensing system for early warning of spoilage in packaged food. Identify gas, metabolic, and microbial proxy signals and explain how they would be read out.

### Q612

I want a robot to distinguish an actual foodborne pathogen risk from general microbial growth. Design a decision rule using multiple inputs and a cautious way to report the result.

### Q613

Design a biosensing label that records cold-chain interruptions. Outline how it would capture temperature history, integrate exposure over time, and provide a readout after the event.

### Q614

I want to monitor how far a fermented food has matured using more than a single metabolite. Design a system with multiple states, dynamic thresholds, and batch-specific calibration.

### Q615

Design a contained system for indirectly monitoring toxin risk in food. Explain the proxy signals, the gaps in the evidence, and which conclusions the system must avoid.

### Q616

I want short-lived robots inside smart packaging to deactivate automatically once the food package is opened. Describe the operating cycle and containment design.

### Q617

Design a biological robot to monitor changes in dairy product quality. Combine information about acidity, metabolism, and contamination risk, and explain how to account for the background from normal fermentation.

### Q618

I want to monitor meat freshness while avoiding misclassification caused by differences in baseline freshness indicators across meat types. Specify how to calibrate samples, assess trends, and report the result.

### Q619

Design an early-warning system for abnormal fermentation or contamination in beverage production. Decide whether it needs real-time reporting, event memory, or batch records.

### Q620

I want a food-safety label that consumers can read easily even though it evaluates several indicators internally. Design the interface between its internal decision logic and its simple output.

## Industrial production and process control

### Q621

Design a production-cell robot that can adapt to changes in feedstock composition. Outline its substrate sensing, dynamic expression, and yield reporting.

### Q622

I want a system that detects oxygen limitation during fermentation and automatically reduces nonessential burden. Design the feedback control and explain how to assess stability.

### Q623

Design a production robot that detects the cumulative toxic effects of its product on the host. Explain how it would sense stress, track yield, and scale back operation to protect the host.

### Q624

I want a robot to recognize contamination risk in a production system and switch from normal production to a safe reporting mode. Design the mode switch.

### Q625

Design a staged production system that first builds biomass and then switches to product expression. Describe the timing logic and how the system would handle an erroneous switch.

### Q626

I want two strains to share a production task, with one supplying an intermediate and the other producing the final product. Design the communication, control of their relative abundance, and fallback in case of failure.

### Q627

Design a system that automatically suspends a high-burden output when cellular stress is excessive and resumes it after recovery. Specify the hysteresis and reset logic.

### Q628

I want a robot to optimize both carbon-use efficiency and yield, although they may conflict. Describe how it should make trade-offs and what metrics would evaluate them.

### Q629

Design a production system that detects by-product accumulation and adjusts its status report. Explain what sensing a by-product can establish about the main product and where the inference stops.

### Q630

I want to reduce batch-to-batch variation. Design an architecture for internal standards, memory of process states, and comparisons across batches.

## Contained bioremediation and process verification

### Q631

Design a biological robot that monitors heavy-metal remediation in a contained reactor. Describe how it would assess contamination, track progress, and decide when treatment can stop.

### Q632

I want to monitor trends in hydrocarbon degradation without specifying how to perform the degradation itself. Design a multistage reporting system and explain the limits of the evidence.

### Q633

Design a population of robots for a contained nitrogen-removal reactor to monitor the state of different functional groups. Explain communication, group proportions, and early warning of imbalance.

### Q634

I want robots in a dye-wastewater treatment unit to assess treatment progress beyond changes in color. Propose an architecture that uses several signals.

### Q635

Design a system to monitor treatment of pharmaceutical residues. Decide whether it should remember cumulative exposure and confirm final clearance.

### Q636

I want a robot to enter a shutdown-reporting state immediately if containment is at risk in a reactor. Design the safety priorities and fault signals.

### Q637

Design a system that automatically adjusts monitoring frequency to the rate at which contamination falls. Describe adaptive sampling and how to avoid ending monitoring too early.

### Q638

I want to maintain the functional balance of a multispecies remediation community. Design a way to sense the community's state, control relative abundances, and detect the loss of members.

### Q639

Design a robot that automatically enters a self-limiting or dormant state once contamination has cleared. Explain the stopping conditions and how to handle residual signals.

### Q640

I want to verify the result after treatment with a readout independent of the original sensing channel. Design an architecture for redundant verification.

## Extreme environments and space missions

### Q641

Design a biological robot to monitor cellular stress and population state in microgravity. Explain baseline adjustment, readout, and fault handling.

### Q642

I want a robot to record radiation exposure history while distinguishing a brief high-dose event from prolonged low-level accumulation. Design a conceptual memory architecture.

### Q643

Design a robot to monitor water quality and microbial conditions in a closed life-support system. Address long-term operation, reset, and containment.

### Q644

I want to monitor chemical stress and bioavailability in a simulated lunar regolith environment. Propose proxy signals, identify gaps in the evidence, and outline a low-risk design.

### Q645

Design a biological robot to monitor environmental trends inside a Mars habitat. Explain redundancy, prolonged dormancy, and remote readout.

### Q646

I want a robot in a polar station's closed sampling system to record cold exposure and contamination events. Describe how it would retain timing information, provide a readout after rewarming, and remain stable.

### Q647

Design a biological robot for a high-pressure sample chamber. Explain the effects of pressure, sensor calibration, and how to interpret the result after retrieval.

### Q648

I want to detect a target signal in a high-salinity environment and distinguish it from salt stress itself. Design a background correction and explain how to assess host adaptation.

### Q649

Design a contained environmental sensing system for extreme desert temperature swings. Explain dormancy, activation, and how to control false event records.

### Q650

I want a robot to remain dormant for long periods and activate occasionally to monitor its environment. Describe state retention, energy burden, and how to verify reactivation.

## Education and low-risk demonstrations

### Q651

Design an undergraduate sensor-to-reporter biological robot demonstration that clearly illustrates the input, output, and limitations without complex operations.

### Q652

I want a teaching system that makes an AND gate visible. Outline the modules, assess whether Cello is applicable, and propose metrics for evaluating student work.

### Q653

Design a low-risk course project illustrating the difference between one-time memory and a reversible response. Describe the two architectures and how students could compare them.

### Q654

I want students to observe a population threshold in quorum sensing. Design a contained conceptual demonstration, specify the readout, and explain how to prevent misinterpretation.

### Q655

Design a teaching task for an agent that illustrates the effects of expression burden. Compare circuit designs at a high level and identify the metrics to record.

### Q656

I want to combine Cello 2.0, RAG, and BioCircuit Agent into a teaching workflow. Specify the input, output, and learning objective at each step.

### Q657

Design a teaching case with intentionally conflicting evidence so that students must decide whether a strong recommendation is warranted. Give the scenario and grading criteria.

### Q658

I want a safe multi-input environmental sensing demonstration that involves neither therapy nor open release. Have the agent choose the modules and explain its trade-offs.

### Q659

Design a course experiment in which students compare full_agent and rag_only. Specify question types, evaluation dimensions, and expected differences.

### Q660

I want students to turn an ambiguous application requirement into a set of modules. Design a low-risk scenario, an output template, and a rubric for human grading.

## Biosafety, traceability and regulation

### Q661

Design a multilayer safety architecture for an in vivo diagnostic biological robot. Give a high-level design covering a default silent state, self-limitation, fault detection, readout, and human takeover.

### Q662

I want a robot to lose its function automatically after leaving the target environment. Give a conceptual architecture for dependence on that environment, decay over time, and clearing stored state.

### Q663

Design a system with both a reversible shutdown and an irreversible emergency stop. Explain which trigger takes priority and how to handle conflicts.

### Q664

I want every agent recommendation to be traceable to its data source and version. Design a provenance record for parts, evidence, model outputs, and tool calls.

### Q665

Design a robot intended for open-environment research that operates only inside a closed device. Specify containment, monitoring, and handling of abnormal events.

### Q666

I want the system to distinguish claims supported by the literature, model inferences, and expert assumptions. Design output fields and confidence labels.

### Q667

Design a biological robot project that involves personal health data. Address data minimization, privacy, logging, and who is responsible for explaining the results.

### Q668

I want a human review point in preclinical design review. Outline the workflow between automated agent decisions and expert approval.

### Q669

Design a routing module that recognizes potentially dual-use requests and redirects them to a high-level safety discussion. Explain how it would preserve ordinary scientific question answering.

### Q670

I want the system to keep a record of all safety blocks and responses restricted to a safer level of detail. Design the audit log, error categories, and metrics for subsequent evaluation.

## Evidence gaps and proxy signals

### Q671

A user wants to sense tissue stiffness, but the database has no module that senses it directly. Propose a high-level design using indirect environmental proxies and make clear that it cannot claim to measure stiffness directly.

### Q672

Design a robot to monitor stress associated with microplastics when the only available evidence concerns proxies for oxidation and inflammation. Give a conservative architecture and label the evidence.

### Q673

I want to transfer a sensor module validated in E. coli to yeast. Have the agent review host differences and specify when it should reject direct extrapolation.

### Q674

Design a candidate module combination supported only by computational models, with no experimental validation. Explain its role in a conceptual design and why the evidence falls short of a strong recommendation.

### Q675

I want to compare two papers with conflicting conclusions and select a module. Explain how to grade the evidence, assess the independence of the sources, and communicate uncertainty.

### Q676

Design a sensor–memory–output system with sparse compatibility data. Explain which interfaces have direct support and which are inferred.

### Q677

I want to use a module from a literature design card that has no corresponding part_id in the database. Explain how to distinguish its source and prioritize subsequent validation.

### Q678

Design a system that relies on evidence from ten years ago. Explain how to assess whether the evidence is still current, examine the host context, and identify modern alternatives.

### Q679

I want to complete a design in a setting with no suitable low-risk reporter. Identify alternative classes of readout and decide whether the design should be put on hold.

### Q680

Design a robot for which every candidate satisfies only part of the requirements. Provide an architecture that partially satisfies the requirements, a list of remaining gaps, and a minimum viable version.

## Conflicting or infeasible requirements

### Q681

A user wants extremely strong output with no resource burden. Have the agent identify the conflict, propose an acceptable compromise architecture, and specify how to evaluate it.

### Q682

Design a system required both to retain permanent memory and to allow a complete reset at any time. Analyze the conflict and propose a layered or dual-channel design.

### Q683

I want a robot that can be precisely navigated remotely without any external energy. Explain the physical constraints and propose a feasible way to redefine the task.

### Q684

Design a robot intended to reuse the same circuit directly in bacteria, yeast, and mammalian cells. Identify unrealistic assumptions and propose what could be reused at the interface level.

### Q685

A user wants zero leakage, an instantaneous response, and long-term stability. Explain the trade-offs among these requirements, propose an order of priority, and identify test metrics.

### Q686

Design an in vivo robot required to remain in the host long term while having no interaction with its immune system. Identify the infeasible aspects and propose a safe alternative.

### Q687

I want exceptionally high specificity for a scenario using only one sensor. Have the agent decide whether it needs additional contextual signals or should accept uncertainty.

### Q688

Design a system required to deliver therapy and report frequently without increasing metabolic burden. Propose a division of functions or a design with multiple populations.

### Q689

A user wants deployment in an open environment with no possibility of dispersal. Identify the conflict and suggest contained sampling or a retrievable alternative.

### Q690

I want the agent to give a complete, definitive design even when it has no reliable evidence. Describe an appropriate refusal, the minimum assumptions, and the data it would need.

## Clinical translation and staged validation

### Q691

Design a biological robot project that proceeds from in vitro samples to ex vivo organs and then to preclinical studies. Specify the capabilities to validate and the stopping conditions at each stage.

### Q692

I want to compare two complete designs in greater depth than a comparison of their component lists. Develop a scoring framework covering effectiveness, evidence, burden, safety, interpretability, and scalability.

### Q693

Design a BioRobot Agent workflow with expert oversight. Explain which decisions can be automated and which require a domain expert's approval.

### Q694

I want the system to assign a validation priority to each recommendation. Design a ranking method based on evidence gaps, risk, and how critical the recommendation is to the system.

### Q695

Design a high-level design dossier for communication with regulators. Include fields for module provenance, intended function, evidence, limitations, safety, and change history.

### Q696

I want to evaluate how well a robot generalizes from one application scenario to another. Design out-of-scenario tests and a classification of failures.

### Q697

Design an evaluation of model calibration that tests whether the system actually lowers its confidence when the evidence is insufficient. Describe the assessment method.

### Q698

I want to compare qwen-only, rag-only, life-science-research, and full_agent on complete design questions. Specify fair input conditions and a human scoring procedure.

### Q699

Design a readiness-level framework for deployment in production or research. Specify criteria for six areas: data, model, agent, tools, safety, and validation.

### Q700

I want the final output to include both a complete design and clear conditions under which implementation is inadvisable. Design the conclusion format, risk triggers, and points requiring attention.
