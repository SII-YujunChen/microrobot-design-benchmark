# Basic Design

[All collections](../QUESTIONS.md) · [Download this collection as JSONL](../../data/basic_design.jsonl)

| Topic | Question IDs | Count |
| --- | --- | ---: |
| Tumor microenvironment | [Q201–Q208](#q201) | 8 |
| Gut monitoring | [Q209–Q215](#q209) | 7 |
| Infection and wound monitoring | [Q216–Q221](#q216) | 6 |
| Vascular and thrombus monitoring | [Q222–Q225](#q222) | 4 |
| Environmental monitoring | [Q226–Q230](#q226) | 5 |
| Industrial biomanufacturing | [Q231–Q235](#q231) | 5 |
| Tissue engineering and biomaterials | [Q236–Q239](#q236) | 4 |
| Agriculture and soil | [Q240–Q243](#q240) | 4 |
| Collective systems | [Q244–Q247](#q244) | 4 |
| Design tool interoperability | [Q248–Q250](#q248) | 3 |

## Tumor microenvironment

### Q201

I want to design a biological microrobot that can tell whether it is in a hypoxic region after entering a tumor microenvironment. Outline a high-level biological circuit. Which sensing, control, memory, and reporter or output modules does it need? Which are optional?

### Q202

A robot passes only briefly through a region with a characteristic tumor signal. How would you design its sensing, memory, and expression modules so that I can later tell whether it was there? Explain why memory is more appropriate than a reporter alone.

### Q203

I want a microrobot to emit a signal only when two tumor-associated conditions, hypoxia and acidity, occur together. Break this down into a biological circuit design and assess whether Cello-compatible combinational logic is sufficient or an additional memory module is needed.

### Q204

I want to design a therapeutic biological microrobot that activates in a tumor region. For now, I only need a design review, with no experimental steps. Which sensing, control, expression, and safety modules should take priority, and what evidence is still needed before proceeding?

### Q205

Suppose a microrobot is intended to support immunotherapy without directly killing tumor cells. Design a biological circuit limited to localization, recording, and low-risk reporting. Explain which therapeutic outputs should be excluded from an early demonstration.

### Q206

I want to use a magnetic field or heat as an external trigger and have a bacterial circuit record that the trigger occurred. Distinguish the responsibilities of the physical actuation layer and the genetic circuit layer.

### Q207

Ordinary inflamed tissue may exhibit some of the same signals as a tumor. How would you design a biological robot circuit to reduce false positives? Consider multi-input logic, thresholds, whether memory is needed, and the design's limitations.

### Q208

Design a tumor microrobot that stays silent outside its target region and reports its state only inside it. Focus on the safety and off-state controls and the output module. Leave out experimental procedures.

## Gut monitoring

### Q209

I want to design a gut microrobot that distinguishes a normal intestinal environment from inflammation. Outline a high-level circuit covering sensing, logic, reporting, and containment.

### Q210

An engineered bacterial robot must sense the density of the surrounding microbial community before deciding whether to express a reporter. How would you organize the quorum-sensing input, control, and output modules? Is memory necessary?

### Q211

How would the circuit of a gut diagnostic robot differ between short-term detection and long-term resident monitoring? Explain the need for memory, a kill switch, or control of long-term expression in each case.

### Q212

I want to transfer a sensor–memory circuit validated in E. coli directly to a Bacteroides chassis for a gut robot. Review the design. Which modules can inform the new design, and which findings cannot be directly extrapolated?

### Q213

Design a robot circuit that records whether a particular inflammation-associated signal has occurred in the gut. The only output needed is a low-risk reporter. No therapeutic output is required.

### Q214

The output should activate only when low oxygen and a particular metabolite occur together in the gut. Design a high-level logic circuit and explain whether Cello could be used for its combinational logic submodule.

### Q215

Design a population of gut robots in which individual cells sense their local environment and the population communicates to decide whether to report. Break down the roles of quorum-sensing communication, local sensing, collective control, and output.

## Infection and wound monitoring

### Q216

I want to design a biological microrobot for early recognition of wound infection. It should sense infection-associated environmental changes and produce a detectable signal. Provide a module-level design without an experimental protocol.

### Q217

A robot is to detect quorum-sensing signals from pathogenic bacteria to assess infection risk. How would you design quorum sensing, signal filtering, and reporting? Identify risks of misclassification.

### Q218

A robot encountering a biofilm infection needs to determine whether its surroundings resemble a biofilm. Design a high-level sensing, control, and output architecture. Explain which observations about biofilms cannot establish that the robot's behavior can be controlled.

### Q219

After encountering an infection signal, a robot should retain its state for later readout even if it leaves the area. Design the memory and readout logic.

### Q220

Evaluate a proposed biological robot for treating wound infection. Which sensing, control, expression, and safety modules would it need? Which therapeutic outputs should be reserved for future work and excluded from a low-risk demonstration?

### Q221

How would you design multi-input biological circuit logic to distinguish ordinary inflammation, bacterial infection, and fungal infection? Identify which elements are best treated as high-level concepts rather than candidates for direct implementation.

## Vascular and thrombus monitoring

### Q222

I want to design a biological microrobot that recognizes a thrombus-associated microenvironment solely for localization and reporting, with no therapeutic function. Break down its sensing, control, output, and safety boundaries.

### Q223

In a flowing environment, a robot may encounter its target signal only briefly. Propose a high-level circuit for capturing the transient signal, storing it in memory, and reading it out with a reporter.

### Q224

An intravascular robot may pass through non-target tissues. How would you design a circuit that is silent by default and reports only when it encounters a specific combination of signals? Consider AND and NOT logic and safety.

### Q225

Magnetic actuation handles navigation, while the biological circuit handles only target recognition and status reporting. Propose a layered design that distinguishes motion control from gene expression.

## Environmental monitoring

### Q226

Design a biological microrobot that detects contaminants in water and produces a readable signal. Give a module-level design and define its safety boundaries. Exclude plans for release into open environments.

### Q227

The task is to record whether heavy metal exposure has occurred in a body of water, rather than to detect it in real time. Propose a high-level design for a biosensing robot with memory.

### Q228

I want an environmental monitoring robot to distinguish organic pollution, heavy metals, and abnormal nutrient levels. Design a sensing strategy and a way to encode the outputs, without detailed engineering steps.

### Q229

How do circuit design and safety modules for a robot that tests environmental samples only inside a closed microfluidic chip differ from those for release into open water?

### Q230

Design a population-threshold alarm that triggers only when a pollution signal persists across multiple microrobots. Consider local sensors, quorum-sensing communication, memory, and output.

## Industrial biomanufacturing

### Q231

I want to design a biological microrobot to monitor metabolic state during fermentation. Which sensing, metabolic-state reporting, memory, or feedback control modules might it need?

### Q232

A robot circuit contains a sensor, logic, memory, and a strongly expressed reporter. How would you assess the risk of resource burden at the design stage? Describe the review criteria and leave out experimental optimization parameters.

### Q233

Propose a high-level monitoring robot for a Yarrowia lipolytica metabolic engineering application. It should sense metabolic state and report abnormalities. Do not assume that E. coli modules transfer directly.

### Q234

A cell-based robot should remember whether a product ever reached a high level. Design its sensing, memory, and readout and explain how this differs from a real-time reporter.

### Q235

I want the robot to reduce expression automatically in response to metabolic burden. Propose a conceptual feedback control circuit and assess whether Cello 2.0 can directly compile such a feedback system.

## Tissue engineering and biomaterials

### Q236

Design a biological microrobot for a tissue engineering scaffold. It must sense whether it is inside the material and produce a localization signal. Break down the material-sensing, control, and reporter modules.

### Q237

I want cell-based robots to produce spatial patterns of expression in a material rather than express uniformly. Propose high-level spatial control that accounts for local signals, communication, and output modules.

### Q238

I want a robot to report damage to a material or a change in mechanical stress. Outline a possible sensing, memory, and output design and identify signals for which direct evidence may currently be lacking.

### Q239

In a tissue engineering application, the robot should avoid continuous high reporter expression. Design a high-level circuit that keeps the burden low and enables control over expression.

## Agriculture and soil

### Q240

Design a biological microrobot that senses plant root signals in the rhizosphere and reports soil conditions. Consider the chassis, sensors, output, and environmental safety.

### Q241

The goal is early warning of plant infection without therapeutic intervention. Design a low-risk sensing and reporting circuit and explain how to avoid drawing conclusions beyond the evidence.

### Q242

I want a soil robot to record signals that a plant has experienced drought or salt stress. Propose a reporting design that uses memory.

### Q243

Evaluate a proposed biological robot intended for an open soil environment. Focus on safety boundaries and containment. Leave out specific release plans or culture procedures.

## Collective systems

### Q244

Design a voting system for a population of biological microrobots. Each robot senses local signals, and the population communicates to decide whether to issue a collective report. Break down local sensing, communication, threshold control, and output.

### Q245

Subpopulations of a robot community handle sensing, memory, and output separately. How would you divide their responsibilities and design their communication interfaces? Discuss compatibility and failure modes.

### Q246

I want a biological robot to sense a signal, wait for an interval, and then express a reporter. Propose a design covering timing control, memory, and expression.

### Q247

Several engineered bacterial populations share similar quorum-sensing signals. How would you design a circuit to reduce cross-talk? Consider signal orthogonality, logic filtering, and limitations.

## Design tool interoperability

### Q248

A user wants a two-input AND gate to control reporter output. As the BioRobot Agent, assess whether this task can be assigned to Cello 2.0 and provide a high-level plan at the Verilog level.

### Q249

A user wants a biological robot with sensing, memory, and output that remembers past exposures. Which parts cannot be assigned directly to Cello 2.0, and which combinational logic submodules could still use Cello?

### Q250

All I know is that I want a biological microrobot that records its state after entering a particular environment and reports it under safe conditions. First break down the requirements, then decide which sensing, control, memory, output, and safety modules are necessary. Do not assume it needs them all.
