# Advanced Biological Microrobot Design

[All collections](../QUESTIONS.md) · [Download the 100 design briefs](../../data/advanced_biorobot_design.jsonl) · [Scoring guide](../EVALUATION.md#score-a-design-brief)

Design a robot for the mission in each brief. Explain what the biological component contributes, how its state or force crosses an interface, and what the robot does when a constraint or failure changes the outcome. Treat the stated component capabilities as design assumptions. You may propose another architecture if you can justify it.

| Design topic | Questions |
| --- | --- |
| Biological sensing, memory and reporting | [Q701–Q725](#q701) |
| Locomotion, contact and manipulation | [Q726–Q750](#q726) |
| Collective and distributed design | [Q751–Q775](#q751) |
| System integration and fault recovery | [Q776–Q800](#q776) |

## Biological sensing, memory and reporting

### Q701

**A mobile recorder for the order of two local cues**

Design a biohybrid microrobot to investigate whether a benign sugar cue precedes a change in acidity within one chamber of a sealed fermentation model. The robot returns to a single dock, and there is no live telemetry. Assume encapsulated cell-free functions can recognize either input, remember a state, or emit a durable endpoint report. Each additional durable output occupies space otherwise available for sampling. Simultaneous cues, isolated cues, and cues encountered across different chambers must not count as a confirmed sequence. Specify the functional biological circuit, its interface to chamber entry and exit, and the motion or dwell behavior needed to support the distinction. State what remains unresolved when the two inputs cannot be temporally separated.

### Q702

**A probe that must know when to look again**

Design a microrobot that inspects the underside of a transparent film in a sealed packaging demonstrator. A reversible protein-based optical patch recognizes a benign coating defect, but residual binding from a previous defect can survive a move. A clean reference island on the route can indicate whether the patch has recovered. Inspection time is limited, so routing through the island after every clean observation is undesirable. Create a body–sensor architecture that decides when to continue, revisit, or declare a region unreadable. A second defect may sit immediately after the first. Explain what would allow the robot to report two distinct defects and what it should report when that evidence is unavailable.

### Q703

**A surface deposit or a cloud?**

Design a microrobot to mark deposited sugar-rich gel on coupons in a closed confectionery inspection cell. The same molecular marker can also float through the chamber in harmless soluble fragments. Assume a biological affinity patch responds to either form, and its response alone cannot identify the source. The robot can approach a surface, withdraw, or turn to present a different face. It may carry a second patch, but doing so displaces its usual contact indicator. Decide how to arrange the interfaces and movement so that the robot marks a coupon only when the evidence supports a surface deposit. Define the robot's response to a soluble cloud that follows it toward a coupon.

### Q704

**Reading a report consumes the report**

Design a reusable shuttle carrying a hypothetical cell-free optical patch through a sealed materials library. The patch retains one bit when a tagged specimen is encountered; interrogation erases that bit. The shuttle can reach either of two readers first, but the quality office needs one durable report linked to the correct route. Returns and duplicate dock contacts are common. Define the on-body and dock interfaces, the order in which they exchange route identity and biological state, and the evidence needed before the shuttle starts another route. Address a reader failure immediately after interrogation. State which outcome the system can still guarantee if no copy exists when the patch is erased.

### Q705

**Separating softness from a chemical cue**

Create a biohybrid inspection robot for a sealed gallery of soft hydrogel tiles. Its hypothetical protein-based color patch responds to a harmless marker but can also change appearance when compressed. The tile defects of interest occur on the softest tiles, where compression is most variable. The robot can spread its load using a compliant foot or observe a second face, but the extra structure reduces access to narrow recesses. Design a mechanical and biological sensing arrangement, a rule for deciding which recesses to enter, and an outward sign that distinguishes a credible chemical observation from a contact artifact. Address a case where both marker and compression are present.

### Q706

**Which side of a membrane changed?**

Design a microrobot for a sealed two-sided membrane demonstrator. A biological indicator changes color when it touches a benign marker on either face of the membrane. A compliant carrier can wrap partly around an edge; in some poses both sensing faces are visible in projection as one spot. The required result is a side-specific map of contact, including visits interrupted at the edge. Choose where identity and orientation are encoded and how the body moves, stores, and presents observations. Explain when a detected marker can be assigned to a side and when the robot must leave the assignment unresolved.

### Q707

**Remember a pause, not a delay on the way home**

A sealed microfluidic museum exhibit needs a robot that reports whether it paused on a marked tile for one uninterrupted qualifying visit. A biological contact receptor gives a reversible signal on that tile. A hypothetical integrating material can accumulate signal while exposed but relaxes only slowly, so several short visits might resemble one long visit. The return path can also be slow. Design how contact, movement, dwell qualification, and memory should interact. Select which state should survive the return trip and which should clear on departure. The visitor should be able to tell a genuine sustained visit from multiple brief contacts whenever the architecture supports that distinction.

### Q708

**A sampler that can abstain when its biological logic is unavailable**

Design a mobile biohybrid sampler for a closed fruit-processing quality model. A cell-free recognition unit reports a target sugar, but a second constituent can inhibit its signaling without removing the sugar. At the dock, each visited pocket must be labeled detected, absent, or indeterminate. Assume you can allocate space to two biological processing paths: both may observe the sample, or one may instead process a known non-target control distinguishable from the sugar. The carrier can revisit one pocket before returning. Specify what each biological path senses or checks, how their outputs are combined, and when their state should command a revisit. Explain what a valid absence claim would require if the control and target paths do not share susceptibility to inhibition.

### Q709

**A landmark that changes meaning on the return trip**

Design a shuttle robot for a sealed branching display in which the same benign affinity marker on a landmark has two meanings: outbound it tells the robot to inspect a sample bay, and inbound it identifies a handoff point. Assume the biological receptor has no sense of direction. A bend can reverse the body's orientation without reversing the mission phase, and a dock can lose its last acknowledgment. Specify how local recognition selects a phase-appropriate action, how the shuttle knows a handoff actually occurred, and what state persists if the landmark is encountered again. Show how a route reversal or lost acknowledgment avoids producing a false second inspection or handoff.

### Q710

**Two specimens touch the same sensing face**

Design a microrobot that inspects adjacent gel specimens on a sealed teaching chip. Each specimen should receive its own yes/no report for a benign biological binding marker. The recognition face is wider than the gap between specimens, so the robot can bridge the boundary. A mechanical indexing notch is available at each specimen center, but stopping there slows the route. A faster continuous pass is possible. Choose how to combine footprint design, robot motion, and recognition memory so that a positive signal can be credited to a specimen. State how the design handles a signal that starts on the boundary and persists into the next specimen.

### Q711

**A robot that writes a retrievable tactile map**

Design a biohybrid explorer for a closed model of an embossed textile. Assume a biological contact layer can distinguish a smooth patch from a rough patch, but its state relaxes before the robot returns. The requirement is to recover the order of transitions along a short route. The body can carry a tiny strip of passive writable material but has no permanent clock. The robot may slip, retrace a section, or run out of blank strip. Design the link from touch to a write action, decide how the sequence is indexed, and specify what a reader at the dock can infer after a reversal or an exhausted strip.

### Q712

**Report a dormant excursion without draining the memory**

Create a biohybrid indicator robot that is carried past sealed reference tiles, then spends most of its route in a dark transport sleeve. A light-sensitive biological patch can signal its illumination history during the outward leg. The same light used by the dock camera also activates the patch. The task is to report whether the outward exposure occurred even if return time varies. Design the allocation of sensing, memory, and optical or mechanical isolation between robot and dock. Explain how the reader differentiates an outward event from activation caused by its own interrogation, and what happens if the sleeve admits light on the return trip. The carrier can choose a protected return lane or a longer reference lane. Give it a physical response to a possibly invalid observation before the dock reads the event.

### Q713

**When two desirable cues cannot be read at once**

Design a contact-guided microrobot for a sealed biomaterials sorting chip. A specimen earns a composite mark only when both a reversible affinity cue and a soft mechanical texture are found on the same small patch. The affinity face must be unloaded for a valid reading, while texture sensing requires contact load. Assume the robot can place a passive temporary fiducial, or carry two separated sensing faces. The specimen can shift between visits. Specify how sequential observations become one local decision, how the biological interface is protected from an invalid load, and what occurs when spatial registration is lost before the second observation.

### Q714

**Choosing what the robot can remember**

Design a biohybrid inspection robot for four independently marked or unmarked fixtures in a sealed materials carousel. A reversible biological pad detects a benign coating only during contact. The robot has four stable onboard memory states, and the dock ordinarily sees it only after it completes the circuit. The operator wants the exact identity of every marked fixture. You may add one type of passive fixture-mounted witness or allow intermediate returns to the dock, but not both. Choose an architecture, show how a positive and a verified negative leave distinguishable records, and define what the robot does if it loses its fixture index mid-trip. Explain which requirement would have to change if both extensions were unavailable.

### Q715

**A humidity history that bends the recorder**

Create a biohybrid crawling inspector for a closed paper-conservation mock-up. Its passive plant-derived sensing strip curls reversibly as humidity changes; movement of the crawler also flexes its body. The client needs a persistent indication of a humid pocket without confusing a sharp turn with exposure. The strip can sit outside the load path, where it occupies clearance, or share the body contour, where turns are easier to negotiate. Design how the strip is mounted, when its deflection is admitted as evidence, and how the robot marks the mapped pocket after the strip relaxes. Include a distinct outcome for narrow regions where humidity and body bending remain inseparable.

### Q716

**A biological phase comparator in an artificial day**

Design a biohybrid scout for a sealed model greenhouse with alternating light and dark phases. It should park at a leaf-model bay only when local dimming is unexpected for that phase. Dimming at ordinary dusk should leave it mobile. Assume an encapsulated photosensitive unit responds rapidly to local light, while a slower reversible biological state can retain recent illumination history. Only a reference bay sees the chamber-wide lighting directly; internal travel and self-shadowing vary. Decide whether phase memory belongs on the scout, at the reference bay, or across both. Define the biological comparison, how its outcome controls scouting and parking, and how the robot recovers after a long unscheduled blackout.

### Q717

**Detect damage without causing the evidence**

Design a microrobot to flag delamination in fragile, transparent starch layers in a closed packaging test cell. A hypothetical bioadhesive contact pad shows a reversible optical change at an already lifted edge. Pressing the robot against an intact weak edge can lift it and generate the same change. The body can image a region before touching it, but the image reveals only sufficiently large gaps. Specify the approach, sensor placement, and decision architecture for marking pre-existing damage. Preserving the sheet has priority over exhaustive coverage. Explain how a microscopic gap below optical resolution affects the strongest conclusion a robot may write to its map.

### Q718

**A detachable nose with a memory of its own**

Design a reusable microrobot whose removable biological sensing nose inspects a benign adhesive marker in a sealed microassembly line. A reversible signal lives on the nose, while the mechanical body carries trip identity. A worn nose may be exchanged mid-route at a service station, and a previously used nose can arrive carrying residual marker. The line needs an attributable report for each inspected fixture even across a swap. Allocate identity, readiness checks, event storage, and acceptance of a replacement between the nose, body, and station. Describe how the robot resumes inspection and when the operator should see an incomplete trip.

### Q719

**Choosing a branch when the background changes**

Create a biohybrid guide robot for a contained fluidic puzzle. It must choose the branch leading toward a benign dissolved cue. Its receptor reports local concentration reversibly; the signal has a lag, and the background can change across time even at a fixed point. The carrier can alternate between two branch mouths or present two separated sensing tips, but a wide span cannot enter both narrow branches. No map identifies the stronger branch in advance. Choose a sensing and movement scheme, define when the robot commits or waits, and give a condition under which a directional decision is physically unsupported.

### Q720

**A selective stop on a patterned repair model**

Design a microrobot for a sealed soft-material maintenance demonstrator. It should stop at a marked tear in an inert membrane, but keep moving past a harmless printed marker or an unmarked indentation. A biological binder recognizes the marker irrespective of whether a tear is present. A compliant edge follower senses a discontinuity independently. The two sensing elements cannot occupy the same point on the body, and a turn can reverse their order of encounter. Propose a layout and decision rule that requires both cues at the same defect. Specify the evidence that permits stopping and what the robot does if spatial association is uncertain.

### Q721

**A reporter that consumes what it senses**

Create a microrobot for a sealed food-gel demonstrator that maps whether a benign sugar is present along a narrow channel. Assume its cell-free enzymatic patch consumes some of the local cue when producing a visible signal. The goal is to mark meaningful boundaries in the original sample. A second pass immediately behind the first may see an artificially depleted trail. Design how the body exposes the sensing element, manages its route, and stores boundary evidence. Specify how the robot should treat a reversal onto its own path and what level of map it can claim if fresh material cannot be distinguished from disturbed material.

### Q722

**Turn a local stress signal into a protective reflex**

Design a biohybrid microrobot that carries a fragile encapsulated biological optical sensor through a closed rough-walled test channel. The outer shell can use either a retractable guard or a sacrificial compliant rim. A stress-sensitive element in the capsule can indicate deformation, but its signal arrives after the first impact and does not reveal which side contacted the wall. The report is valid only if the optical sensor remained usable during a site visit. Choose a protective architecture, explain how biological stress and physical contact govern motion and sensing, and define how an operator can tell lost coverage from a clean environmental reading.

### Q723

**A warning must remain local to one defect**

Create a microrobot for a sealed gel-inspection stage that leaves a removable visual warning next to a detected adhesion defect. A bioaffinity tip recognizes the defect, but the robot must move its own body away before an inert marker tab can be placed. While backing away, the tip can pick up a second positive site. Tabs are scarce, and a misplaced tab is worse than a missed one. Design the handoff from biological detection to a specific physical mark, including robot pose, what memory is locked during retreat, and the rearming condition. State how the robot should handle loss of the first site's location.

### Q724

**Two jobs compete for the same optical window**

Design a biohybrid inspection robot for a closed transparent microfactory. A cell-free recognition patch must face a product to inspect it. The robot's orientation mark and the patch can be seen through the same tiny window, but the mark obscures the patch whenever both occupy the window together. The product can slide relative to the chamber during inspection. The dock needs a result associated with a specified face of the product. Propose how the robot establishes a product-relative frame and obtains the biological readout despite this optical conflict. Include a situation in which the requested face-specific result must be withheld.

### Q725

**Build a robot that can honestly say it missed a layer**

A sealed laminate-inspection cell contains several transparent sheets that may separate briefly as a microrobot crosses them. A biological recognition pad detects a harmless residue whenever it contacts a contaminated sheet, but it cannot identify the sheet itself. The job is to report status for each sheet, explicitly distinguishing clear, contaminated, and uninspected. A roomier robot can carry a contact witness; a slimmer one can enter more gaps. Design one complete architecture, including how the body selects gaps, verifies which sheet face was contacted, stores a verdict, and handles a sheet that closes before a valid reading. Explain one claim a more compact design could make and one it would have to give up.

## Locomotion, contact and manipulation

### Q726

**Turning at a junction without an onboard compass**

Design a biohybrid swimmer for a sealed, transparent model canal. It must take either branch of a symmetric fork on command, even after it enters the fork facing backward. A ciliary surface provides thrust in a fixed direction relative to its mounting. The overhead camera sees the robot's outline and the branch labels, but a circular hull looks the same at every heading. You may change the hull, the arrangement of the ciliary surfaces, or the observation interface. Explain how your design establishes orientation, changes direction, and recovers when the camera temporarily loses the hull near the fork.

### Q727

**Carrying a rigid sample through an asymmetric constriction**

A sealed model conduit has a wide approach, a shallow slot, and an open receiving bay. A flat inert sample fits through the slot edge-on. The sample cannot bend and its marked face must arrive facing up. Design a carrier microrobot using a hypothetical cell-free contractile strip that can pull a joint; the strip cannot actively push it back. The carrier and sample must both clear the slot and remain retrievable. Describe how the geometry, return motion, and retention mechanism work together. Explain how the robot would recognize a failed passage without forcing the sample farther into the slot.

### Q728

**Docking when a bead can roll in the gripper**

Design a biohybrid microrobot that carries a patterned inert bead to a keyed socket in a closed tabletop display. The bead can roll inside the gripper during travel, so knowing the carrier heading does not establish whether the bead's notch faces the key. The socket rim may be touched, but the carrier must not push against a misaligned key. A reversible biological bending element is available for contact manipulation. Develop the end effector and docking sequence, justify where alignment is established, and explain how the bead can be recovered after an interrupted handoff. What physical event would count as successful placement?

### Q729

**Inspection above a contact-sensitive membrane**

A biohybrid inspection robot must bring a small optical face close to the center of a compliant membrane in a sealed phantom. The membrane cannot support the robot or tolerate a probe touching it. Its rigid perimeter can bear contact, and the membrane may bow upward after the robot arrives. A contractile ribbon can position the optical face within the carrier. Design an architecture that supports the robot, maintains a usable view, and withdraws when the clearance is uncertain. Identify the design trade-off between an unobstructed view and a reliable clearance reference.

### Q730

**Stepping between adhesive and nonadhesive floor panels**

An inspection robot must traverse alternating smooth panels and rough ridges inside a sealed materials tray. Its hypothetical biological foot pads adhere to the smooth panels, while on a ridge the same pads may slide. The instrument face must remain oriented toward the floor, including during transitions. The tray can be modified at its edges but the panels themselves must remain untouched except for reversible foot contact. Design a locomotion system that crosses the boundaries and can return along the same path. Explain how it decides when a new support can bear the load and what it does if the leading foot slips.

### Q731

**Parking on an incline after power is lost**

Design a biohybrid crawler that carries an inert calibration tile up a sloped insert in an enclosed chamber and parks beside a viewing window. When power is lost the biological shortening element relaxes; it cannot hold a sustained pulling force. After restart the crawler must be able to descend by choice. The chamber has smooth side rails that may be used as interfaces, and the tile must stay captive even if the chassis changes attitude. Propose the drivetrain and parking mechanism, explain how powered descent differs from a fault, and identify a visible check that the robot is actually holding its position.

### Q732

**Placing a sleeve over a cantilevered peg**

In a sealed assembly mock-up a soft inert sleeve must be placed around a peg with one free end. The peg's base is inaccessible and excessive sideways contact bends it. A cell-free contractile band can close a tool, but a closed tool around the peg may become trapped after placement. Design the carrier and end effector for the complete pickup, approach, placement, and escape cycle. Explain how you separate the forces needed to hold the sleeve from those transmitted to the peg, and specify what the robot can do if the sleeve catches before reaching its seat.

### Q733

**Handing an object to a moving receiving platform**

Design a biohybrid shuttle that moves an inert reference chip between two platforms inside a closed teaching cartridge. The receiving platform drifts sideways within a limited guide, so aligning with a mark on the stationary chamber wall does not guarantee a valid handoff. The shuttle uses a ciliary drive for translation, and it can carry one passive mechanical accessory. You may shape the receiving dock, but neither platform can send electronic acknowledgements. Specify the accessory, the sequence that transfers the chip, and the observation or physical constraint that prevents the shuttle from leaving the chip between the platforms. Include an abort path if the receiver drifts away.

### Q734

**Traversing a gap without shedding the bridge**

An enclosed micro-workbench has two ledges separated by a gap. A cell-free bending bilayer on a microrobot can arch its body, but it cannot propel the body across open space. The robot must carry a rigid witness tile to the far ledge, later return, and leave no structural part in the gap. Contact with either ledge is allowed. Design the body and transfer sequence, identifying how the system bears the tile during the least-supported phase. State a geometric or support condition under which the robot must refuse the crossing and how the tile can be brought back to the near ledge after a failed reach.

### Q735

**Turning over an inspection coupon without scratching its face**

A biohybrid manipulator in a shallow covered tray must turn over a thin inert coupon so a camera can inspect both faces. Neither polished face may touch the floor or the gripper; contact on the unpolished rim is allowed. The gap above the tray is too shallow for the coupon to rotate freely upright in the main lane, but a recessed turning bay is available. A biological contractile strip pulls but does not push. Design a robot that moves the coupon into the bay, turns it over, and returns it for imaging. Explain how orientation and custody are maintained across the move.

### Q736

**Towing a compliant marker without winding up the tether**

A biohybrid tug must carry a soft reference marker around a post in a closed model basin. Directly gripping the marker obscures its optical face, so the tug attaches to an edge loop. Its biological swimming surface produces thrust but the tug can rotate while turning. Earlier concepts let the tow line wrap around the post or twist the marker face away from the viewing window. Design the tow architecture and route-management strategy. Explain how the tug distinguishes its own progress from progress of the marker, and how it can reverse a failed turn without cutting or abandoning the line.

### Q737

**Writing a contact pattern with a reusable stamp**

Design a biohybrid microrobot that uses a reusable inert relief stamp to press an ordered pattern into a removable soft witness sheet. A pull-only biological element can move the stamp, while translating the robot with the stamp down would smear a mark. Some intended locations are deliberately blank, so an absence of marks alone cannot show whether the robot skipped the correct sites. Specify the motion and contact architecture, how the robot stays registered to the pattern after stopping, and how it recovers if contact ends halfway through a mark. Define a completion indication that distinguishes an intentional blank from a missed operation.

### Q738

**A crawler for both inside and outside corners**

Inside a closed mock-up, a microrobot must inspect a raised block by following a continuous path from the floor onto a vertical face and then over its top edge. Its biological attachment pad holds only while contacting a locally flat patch. The floor-to-wall corner is concave, whereas the wall-to-top corner is convex. Design the crawler's articulated body, means of progression, and contact-transfer sequence. Explain why one fixed body posture cannot be assumed to work at both corners. Describe a condition at either corner that makes retreat preferable to attempting the next transfer.

### Q739

**One command channel for travel and pickup**

A sealed exhibit allows a microrobot only one repeating command waveform, which drives all of its biological contractile elements together. It must travel to an inert token, pick it up, pass an identical-looking empty station, and release the token only at a designated destination. You may design the carrier and give the pickup and destination fixtures distinct passive shapes; no fixture can issue a command. Design an embodied mechanism that interprets the same actuation differently through the task. Explain how the robot recovers after a missed pickup and how the design prevents an empty intermediate station from triggering release.

### Q740

**Carrying a tile while keeping a calibration face in view**

A biohybrid carrier must transport an opaque inert tile past two viewing windows in a sealed cartridge. At each window the camera must see a calibration patch on the carrier and a witness mark on the tile in the same image. The windows look from opposite sides of the cartridge. A directional ciliary pad can move the carrier along the wall it touches; the opaque tile can block either mark depending on how it is held. Design an architecture that presents both marks at both windows without releasing the tile. Explain how you would detect an apparent successful transit that never produced a valid second view.

### Q741

**Centering a fragile ring on a floating platform**

Design a biohybrid manipulator that centers a light inert ring on a freely sliding platform within an enclosed planar chamber. Pushing the ring from one side can move the platform instead of centering the ring. The robot has opposed compliant biological bending surfaces and a view of a reference printed on the platform. The ring may be touched at its outer edge only; the chamber walls are too distant to serve as braces. Specify how the robot establishes a reaction path and judges centering after it has disengaged. Explain how your design handles a platform that is initially moving.

### Q742

**Changing tools without losing the working datum**

A single biohybrid microrobot in a sealed assembly tray must first inspect the inside rim of an inert socket and then place a soft alignment spacer against that same rim. Its biological bending element can drive either a probe or a placement tool, but its mount holds only one at a time. A tool rack lies away from the socket and the socket platform may rotate between visits. Design the tool interface and the method for returning to the original working location. Explain how the robot prevents accumulated orientation error from becoming a wrong-side placement and how it handles an incompletely seated tool.

### Q743

**Following a material boundary with a slow contact response**

In a sealed educational chamber, a passive colored line marks a boundary between two floor materials. A biohybrid vehicle must follow the boundary while carrying a small inert optical target so that its center stays on the line. A responsive gel feeler bends differently on the two materials during contact, but retains its previous bend briefly after leaving a surface. Repeated corrections can therefore steer the vehicle away from a real turn. Design the feeler placement, steering interface, and response to intersections or loss of contact. Explain which observations distinguish a real corner from a delayed response of the feeler.

### Q744

**Leaving a reference token in a blind recess**

A carrier must set an inert reference token in a recess under an overhang in a sealed fixture and return empty. The camera can see the entrance and the carrier tail, but the gripper disappears from view inside the recess. A bio-derived compliant finger opens on bending and relaxes closed. Tokens sometimes adhere weakly to the finger after it opens. Design the carrier, recess interface, and sequence that lets an observer distinguish a seated token from a token that returned on the finger or fell at the entrance. Explain how a failed attempt can be recovered without assuming a second camera.

### Q745

**Holding a protruding load through a tight turn**

An enclosed model track includes a right-angle passage. A rigid inert reference rod fits lengthwise through each straight section, but a carrier with the rod fixed across its body cannot turn through the corner. The clear corner pocket is large enough to rotate the rod if the carrier does not occupy its center. A cell-free contractile linkage can pivot the carrier's gripper about one joint. Design a coordinated carrier, gripping geometry, and corner maneuver that keeps the rod captive. Identify the motion that is impossible under your chosen architecture and the condition under which the robot should back out.

### Q746

**Separating a jam from a completed soft closure**

Design a biohybrid gripper for carrying a deformable inert reference bead between two marked nests in a closed bench cartridge. The biological closing element shortens both when it captures the bead and when a finger catches on a nest rim. Increasing closure beyond the working stroke could deform the bead enough to erase its reference shape. The only live camera view is from above. Specify gripper morphology, acceptance of a grasp, and how locomotion is enabled after pickup. Explain how the robot clears a jam and what independent observation demonstrates that the delivered bead remains fit for use.

### Q747

**A rolling shell with a stationary observation window**

An inspection robot must roll through a closed cylindrical teaching channel and stop at several labeled ports. A natural-fiber bilayer provides reversible bending that can be converted into shell motion. At each stop an interior optical element must face one selected port while the shell remains stationary. Simply rolling until the element points at the port may move the robot away from that port. Design the relation between shell, optical element, and drive so positioning and pointing can be controlled separately when required. Define what must be observable to recover after the shell rolls unexpectedly during inspection.

### Q748

**Moving a pair of tiles while preserving their spacing**

A sealed materials demonstration uses two identical inert tiles whose relative spacing encodes a reference pattern. A biohybrid carrier must move them from a supply platform to a display platform without swapping their positions or squeezing them into contact. The platforms have different support ridges, and a carrier footprint that fits the supply does not fit between the display ridges. A compliant biological actuator can change the carrier shape, but the tiles themselves cannot bend. Design the load path and shape transition. Explain which feature preserves spacing while the carrier transforms, and how the display can receive both tiles without a swap.

### Q749

**Retrieving a disabled carrier from a dead-end inspection bay**

Design a biohybrid robot for inspecting a sealed dead-end materials bay. It carries a removable inert reference plate. The bay permits forward entry but is too narrow for a turn. The robot's biological traveling surface provides forward propulsion only and may fall silent before completion. No second robot can enter alongside it. Specify a normal return architecture and a recovery architecture that still works after loss of propulsion deep inside the bay. Explain how recovery forces reach the chassis rather than the plate and how a user can distinguish a recovered empty chassis from a complete retrieval.

### Q750

**A mobile workcell that must leave the fixture reusable**

A sealed demonstration cartridge contains an entry dock, a narrow channel, and a rotatable worktable. A biohybrid microrobot must carry an inert spacer through the channel, hold it temporarily against a marked table edge while the table turns, then return with the same spacer. The biological actuator can support either travel or active holding at a given moment, not both. The worktable provides no electronic interface, and a loose spacer would prevent the next demonstration. Design the complete workcell, including custody during the transition from travel to holding, how motion of the table is accommodated, and how the system recovers from interruption at its least reversible stage.

## Collective and distributed design

### Q751

**A removable crossing for a soft specimen replica**

Design a team of biohybrid microrobots to carry a soft, inert specimen replica across a gap in a sealed inspection chip. No individual spans the gap. Each unit has a reversible biological contractile element and two docking faces; a dock reports contact but cannot distinguish a firm attachment from a slipping one. Routes exist along both banks, and access from below is unavailable. The chip must be clear for the next specimen. Give the architecture for forming, qualifying, using, and removing the crossing. Explain what would make a different arrangement preferable and how the team protects the replica if one attachment loses support.

### Q752

**Local tissue response under a shared inlet signal**

Design a team of biohybrid microrobots that marks which of two tissue-model chambers shows a local stress response in a closed organ-on-chip exhibit. A hypothetical cell-free sensing face responds to a soluble indicator that can also arrive from the shared inlet. A second face recognizes a reversible surface change on the model tissue, but only while the robot rests at a contact window. Either cue alone is ambiguous. The two faces cannot share a robot, and a chamber can recover before a traveling observer reaches the dock. Design the roles, movements, and memory needed to display a chamber-specific conclusion. Explain what the display should show when the observations cannot distinguish local response from transported signal.

### Q753

**A map that survives the swap of two sampling robots**

Design a fleet for mapping soft and stiff regions on an opaque, reusable material coupon inside a sealed cassette. Each robot has a reversible bio-derived contact pad that distinguishes two compliance classes only while touching the coupon. The docking station can read a returned robot; robots can return in any order and two can swap paths unseen. The cassette has identifiable contact landmarks around its rim and no interior tracking. Define the spatial resolution your design can defend, decide where location and compliance are bound together, and explain how a missed region is recovered without turning an unvisited region into a reported soft region.

### Q754

**Handing off a fragile alignment bead**

A sealed optical alignment cartridge has an opaque bend between a supply pocket and a viewing window. The bead must arrive without rolling against the walls. Assume a supply-side biohybrid robot can grip a bead with a reversible protein-based contact face and move to a handoff recess. A window-side robot can cradle the bead but cannot reach the supply pocket. Both can feel contact locally, and neither can see through the bend. Design their handoff and return cycle. Account for contact between empty grippers, simultaneous gripping that could squeeze the bead, and a stalled recipient. State how the cartridge establishes that a bead reached the intended window.

### Q755

**Carrying a sheet whose edges can disagree**

Design a team of contractile biohybrid carriers to present a thin inert film flat against a readout window in a closed cartridge. Each carrier can grip a patch along the film edge and sense local tension. Local tension can mean either that the film is flat or that a diagonal wrinkle is pulling tight. The window can reveal one alignment mark at a time. Describe how your collective coordinates grip, motion, and release while protecting the film. Identify the evidence for accepting the presentation, the response to one carrier losing grip, and the condition under which you would change the distribution of roles.

### Q756

**A traveling deformation around a ring**

A teaching cartridge should show a single traveling deformation around a flexible ring. Design a collective of small biohybrid robots whose nonreplicating contractile pads can press and release neighboring sections. Each unit sees only its two neighbors and its local surface strain. A pad can remain pressed after its command state changes. The ring may contain one empty docking site. Specify how the motion is initiated, how direction is preserved through a complete lap, and which failures require stopping the display. Explain how a visitor would tell a successful lap from a sequence of command lights moving around a stationary ring.

### Q757

**A fleet of retrievable indicator tiles**

A sealed display has several shallow alcoves, each with a distinct mechanical key at its entrance. A team of biohybrid microrobots must leave one reusable indicator tile in each accessible alcove, permit a visual inspection, and then recover all tiles and robots. A tile has a cell-free color-changing face that responds only after it lies against the alcove floor. Robots cannot read that face while carrying it. Some alcoves look occupied from the entrance even when a tile rests sideways. Design allocation, seating confirmation, and reverse collection. Explain how the team records an inaccessible alcove and what physical condition permits ending the cycle.

### Q758

**Two witnesses before a sample drawer opens**

Design a pair or small group of biohybrid microrobots that authorizes a drawer to present a dyed calibration coupon inside a closed instrument. Presentation is allowed only if the coupon has contacted the sampling pad and the drawer is fully seated. A disposable biological contact witness and a reusable strain-sensitive biohybrid foot are available as abstract modules. Drawer motion can strain the pad and make its optical contact indicator flash without a coupon. No witness may command the drawer on its own. Define which robots observe which events, how an authorization stays attached to the same drawer visit, and how ambiguous or missing witnesses leave the drawer.

### Q759

**Assembling a two-sided mosaic**

Design a collective of biohybrid microrobots that arranges reversible tiles into a prescribed two-sided mosaic on a transparent plate inside a sealed display. Each tile has the same visible top edge. A cell-free indicator on one face changes appearance on contact with the plate, but is hidden once neighbors close around it. Robot grippers can turn a free tile; lifting one from the middle of a finished mosaic risks displacing neighbors. Decide how roles, orientation information, and assembly order are distributed. Explain how the team handles a late ambiguous placement and how the final display can be dismantled for reuse.

### Q760

**Joining two short-lived observations across a partition**

A closed teaching chip has two bays separated by an opaque divider. The goal is to color a central display only when both bays experienced a benign contact event during the same inspection cycle. At each bay a biological sensing patch gives a transient visual change and then relaxes. A docking corridor admits one small robot at a time, and the reader at the center cannot see either bay. Design a biohybrid robot collective that captures, transports, and combines the two observations. Explain what permits a positive display, how late arrivals are assigned, and how resetting one bay affects the other bay's outstanding evidence.

### Q761

**Tuning a compliant support without a force map**

A sealed positioning fixture supports a delicate inert lens blank on several biohybrid microrobots. Their nonreplicating compliant feet can change support state and sense local deformation. A central viewing head can check lens tilt, but cannot detect a twisted support pattern that happens to leave the center level. Design a collective that distributes support while changing the lens orientation between two indexed presentations. Explain how a robot determines whether it may unload a foot, what independent evidence distinguishes a stable presentation from a precarious one, and how the fixture returns to rest if a neighbor cannot respond.

### Q762

**Sharing an intersection while holding different loads**

In a sealed model factory, biohybrid microrobots with contractile crawling pads transport inert beads and flat tags along crossing lanes that narrow to one shared intersection. Loaded bead carriers cannot reverse in the narrow section; tag carriers can. Each robot senses contact and a local floor marker, with no overhead map. A temporary obstruction can make an empty intersection appear permanently reserved. Design the bodies, approach zones, and collective right-of-way mechanism together. Justify how a stalled robot can be distinguished from a lost reservation, how both load classes eventually make progress, and how recovery avoids pushing a loaded carrier backward.

### Q763

**Sealing around a changing outline**

Design a reversible gasket made from a group of biohybrid microrobots in a closed liquid display. The gasket surrounds an inert insert whose outline varies between cartridges. Each unit has a compliant bio-derived sealing face, can dock to neighbors, and can report local contact. Neighbor contact can be positive even when a gap remains between the seal and a concave part of the insert. Explain how the group discovers the boundary, decides whether its coverage is sufficient, and relaxes the gasket without losing a unit in a recess. State which insert geometry would exceed the capability you claim.

### Q764

**Maintaining an index while passing a ribbon**

A closed cartridge must present successive labeled sections of a fragile inert ribbon at an inspection window. A line of biohybrid microrobots can alternately grip and release using soft contractile jaws. Two sections can look identical at the window; the ribbon contains occasional distinct landmarks. A worker request may pause the display halfway through a handoff. Design the collective transport mechanism and the representation of ribbon position. Explain how motion resumes without counting an uncompleted handoff, how a slip is distinguished from a completed advance, and when the system has to return to a landmark.

### Q765

**Surveying a chamber with a continuous biological duty cycle**

A sealed bead-coating demonstrator needs continuous observation at its viewing port while an inert bead stream moves past. A mobile robot carries a reversible biological indicator that gradually loses contrast during use. Its sensing face can be checked against a protected reference only at a separate dock. Leaving the port exposes a blind interval, and two robots trying to occupy the same seat can block the bead stream. Design a collective that maintains credible coverage while members alternate between observation and reference checking. Specify what allows an outgoing observer to hand over, how a degraded spare changes the claim of continuity, and when the demonstrator must pause.

### Q766

**Sorting objects that look identical at the gate**

A reusable closed sorter receives one inert bead at a time. Soft and rigid beads have indistinguishable outlines when unloaded. A biohybrid robot can apply a reversible compliant contact and feel its own deformation, but a freely rolling bead can mimic softness. A second robot can restrain or redirect a bead, not both simultaneously. Design a cooperative sorter that routes confirmed cases into two visible bins and has a defined disposition for unresolved cases. Explain the transfer from examination to routing, how a bead that rolls during assessment is handled, and what evidence permits the team to release it into a bin.

### Q767

**A collective maturation indicator for a sealed food line**

Design a biohybrid microrobot team for a sealed teaching model of a yogurt production line. Its display should distinguish acidification consistent with ongoing fermentation from acid introduced upstream. Assume one hypothetical cell-free pad reports acidity reversibly; another reports a change in the balance of milk sugar and fermentation product only while docked at a sample window. The latter cannot distinguish ongoing conversion from mature product carried in from upstream. Robot carriers can visit the inlet and outlet windows but cannot touch the food or carry liquid between windows. Design the division of sensing and motion, how observations are matched to the same passing portion, and the indication when a run contains mixed or unmatched portions.

### Q768

**A mobile spacer team for a breathing model**

A transparent, sealed model lung uses two compliant lobes to illustrate reversible motion. Inside the display, a collective of small biohybrid robots may use hypothetical cell-free contractile pads to support the lobes from below. The exhibit designer wants both lobes to appear to expand together even though one lobe is stiffer and the shared base transmits motion between them. The robot team must also remove all support for a rest view. Design the role assignment, feedback, and support geometry. Explain how the team distinguishes local motion from base motion and whether equally strong commands or matched surface displacements would better express the intended demonstration.

### Q769

**Peeling a flexible strip without tearing its corners**

A closed robotics exhibit uses a reusable soft strip attached by weak, uneven contact to a viewing plate. Design a group of small biohybrid robots with reversible gripping pads to remove the strip and lay it intact on a nearby support. The robots can sense local pad deformation but cannot see under the strip. Advancing one corner too far concentrates stress; pulling evenly on every robot can also trap an adhered island. Specify how the team chooses roles along the advancing boundary, what signs authorize a change of front, and how a local failure can be isolated while preserving the strip.

### Q770

**A collective that keeps two liquids apart**

A sealed transparent display has adjacent wells containing two benign dyes. The same team of biohybrid microrobots must make a visible pattern in both wells by positioning reusable inert masks. The robots' protein-based gripping faces can retain an invisible droplet after leaving a well. The only shared asset is a transfer dock that handles one mask at a time; external viewing sees mask position, not residue. Design the team allocation, mask custody, and transfer interface so an apparent correct pattern cannot stand in for separation of the two wells. Explain how the system reacts to an unassigned mask at the dock.

### Q771

**A rotating display that cannot lose its reference**

A circular material display in a sealed cartridge should rotate to bring a chosen engraved sector to a window. The disk is pushed in turn by several microrobots with contractile biological feet. Each foot senses local contact but can slip. Sector boundaries look alike except for one physical home mark. The fixture permits adding passive reference features but no overhead camera. Design a collective drive and indexing architecture. Explain how the group reconciles disagreeing indications of progress, handles a robot that remains coupled after its turn, and specifies which sector identities remain defensible after a loss of reference.

### Q772

**A collective display that does not mistake its own shade for algal stress**

Design a reversible collective display for a sealed microalgae ecology exhibit. Each mobile tile holds an optically isolated algae sample whose biological fluorescence changes with light history and relaxes after shade is removed. The display should visibly mark regions affected by an external moving shade. Tiles can rotate a display face and travel between marked seats, but a raised face itself shades the neighboring sample; even a brief self-shadow can leave a biological response after that face lowers. Work out how the team divides observation and display, distinguishes external shade from a shadow it created, and handles a recovering tile. Specify when the exhibit can present a new regional pattern as current.

### Q773

**Delivering a mechanical message without consuming the original**

A closed kinetic sculpture has a left-hand slider whose final position can occupy one of several detents. The display must reproduce that position on a second slider around a corner while leaving the original untouched after reading. Local biohybrid robots have reversible contractile fingers. One finger touching the first slider can distinguish detents, but sideways drag during departure can change the source position. A robot carrying a mechanical record cannot actuate the destination until another robot supports the record. Design a collective copying mechanism, explain how it separates sensing from writing, and specify how it detects corrupted transfer without silently moving the original to match the copy.

### Q774

**Dividing work between a scout and a heavy carrier**

Design a collective biohybrid system to move an inert glass coupon between two seats in an enclosed chip. A lightweight scout with a reversible biological contact pad can pass through a narrow service route and identify which receiving seat is unoccupied. The loaded coupon carrier uses a different, wider route and cannot inspect a seat until committed to its approach. A second independent task can occupy a seat after the scout leaves. Specify the physical coordination at the receiving seat and the information that must survive a scout handoff. Explain how stale information affects the carrier and when the job should remain unfinished.

### Q775

**Sharing the last recovery dock**

Design a team for inspecting an enclosed relief map with tactile biohybrid microrobots. Some robots carry compliant biological sensing feet; others can carry a folded or inactive teammate back. Active and inactive robots look identical to the overhead viewer. The exit dock accepts one robot at a time and closes after the final departure. During inspection a robot can lose its local contact readout while still moving. Present a collective architecture for coverage, diagnosis, and recovery. Resolve the trade-off between using every unit for survey and keeping enough capacity for recovery. Define separate evidence for map coverage and for safe dock closure.

## System integration and fault recovery

### Q776

**An inspection robot for a deforming tissue scaffold**

Design a biohybrid microrobot that can flag a persistent low-oxygen pocket in a soft scaffold inside a research cassette. The scaffold changes shape as the cassette moves. A reusable optical reader sees the cassette at its dock but cannot see into the scaffold. Assume a cell-free oxygen reporter can show the current local condition, and a soft carrier can acquire a reversible location mark from labeled scaffold regions. A result must refer to a region of the scaffold, not simply to the robot's final position. Propose the robot and its route through the cassette, decide what must travel with it, and explain how it would handle a brief pocket or a lost location mark.

### Q777

**A valve inspector that must leave a soft flap free**

A transparent organ-on-chip model contains a compliant flap that normally opens and closes. Design a removable biohybrid inspector that can distinguish a flap that sticks from one that simply has not been loaded. The inspector must leave the flap free between inspections. Assume a thin protein-based contact pad can report local contact and relax after unloading; the channel wall can carry reference marks. The camera can observe motion or contact on a given pass, but not both at once. Describe the robot's body, sensing and observation sequence, explain how to separate a flap fault from interference by the inspector, and define the behavior if the pad fails to withdraw. Loads need not repeat. A passive witness can retain the identity of a loading cycle if the design requires it.

### Q778

**Separate a tissue response from the interference of the observer**

Design a mobile biohybrid scout for a closed, transparent plant-tissue model. The research question is whether a harmless shared cue evokes a local response at a particular tissue region. Assume a sealed non-reproducing indicator unit can report the shared cue and a second biological path can recognize a distinct tissue-response proxy. Moving the scout can itself distort the proxy briefly. The external camera sees its location only when it pauses, and the tissue may move between visits. Specify how sensing, integration, and behavioral control divide between biological logic and the carrier. Design an outcome that nominates a region for follow-up without attributing every coincident signal to the tissue. Identify a condition under which even a stationary response must remain provisional.

### Q779

**A two-branch organ-chip sampler with one return path**

Design a biohybrid robot for a closed model of two tissue chambers. It must return a separate qualitative acidity observation for each branch through a single shared outlet. Assume a cell-free indicator can be read reliably in its branch but changes color again in the outlet. The cartridge can provide branch-specific docking features, and the outside reader sees only the returning robot. No sample liquid may be carried from one branch into the other. Choose between one reusable body, separate bodies, or another architecture. Explain how branch identity, biological sensing, and the returned result stay linked, and how a missing return appears to the operator.

### Q780

**A serviceable soft robot inside a sealed teaching heart model**

A teaching model repeatedly deforms a transparent chamber. A soft biohybrid robot is to follow one moving wall and indicate when local motion no longer follows the chamber cycle. A replaceable protein-based strain element gives a reversible signal, but replacing a stretched element can shift the robot's mechanical baseline. The instructor must be able to swap it without opening the chamber or relabeling earlier observations. Design the body–sensor interface, the service path and the changeover logic. State which history belongs to the body versus the replaceable element and what observation would allow the robot to resume reporting.

### Q781

**Finding which layer of a laminate has lifted**

Design a recoverable biohybrid inspection robot for a transparent model laminate. An edge channel lets a small crawler contact either the upper interface or the lower one, but it cannot touch both simultaneously. Assume a soft protein adhesion pad reports loss of contact, and that normal surface texture occasionally breaks contact even on intact material. The output must identify the suspect interface and a region worth re-inspecting, without applying a permanent mark or pulling loose layers farther apart. Describe locomotion and contact, how the robot records which face it inspected, and how it decides to revisit or withdraw when evidence is ambiguous.

### Q782

**A diagnostic state machine for a closed fermentation bypass**

Design a biohybrid shuttle that visits two enclosed observation pockets along a food-fermentation bypass. Its job is to distinguish a short feed disturbance from a persistent process change and to identify which pocket first requires follow-up. Assume available cell-free sensing functions can report transient sugar availability and reversible acidity; neither alone identifies the process state. The shuttle cannot see both pockets at once, and the dock can read only one compact status symbol per pocket. Choose the biological integration and memory functions, the information kept by the carrier, and the revisit policy. Specify what would justify a follow-up symbol and when the time order of pocket changes must be left unresolved.

### Q783

**A dye-free inspection robot for a soft casting**

Design a biohybrid crawler that can distinguish a shallow surface seam from a soft patch in a finished gel casting. The part must leave inspection free of dyes and detachable labels. Assume the crawler has access to a reversible bio-derived tactile pad that changes shape on loading; no continuous image of the pad is available beneath the casting lip. A seam and a soft patch can produce the same single deflection. Choose what motions and references make the two hypotheses distinguishable. Describe how observations become an actionable region map and when the operator should receive an unresolved classification.

### Q784

**An inspector that must pass a fragile witness strip**

Design a retrievable biohybrid microrobot for a sealed, reusable sample holder. It must inspect deformation of a fragile witness strip from both sides without leaving the strip pinned between visits. A bio-derived elastic jaw can hold a reference edge without continuous input, but a jaw that stays closed after a fault could obstruct the next sample. The downstream pocket permits recovery from only one side. Propose a mechanical and sensing architecture that meets the inspection and clearance requirements. Explain how a valid second-side observation is distinguished from a replay of the first and what happens if the robot cannot complete its return.

### Q785

**A reference that ages with the robot**

A reusable biohybrid inspection shuttle visits reference and sample pockets on a slide. Its protein film loses sensitivity with use, and optical window staining can imitate the same loss of signal. The new design must let a user replace a spent film while deciding whether the slide window also needs service. Only the film may be replaced during a run; the windows stay sealed. Propose an architecture for the shuttle, reference path, and maintenance decision, specifying what observations distinguish the two faults, how histories remain traceable across replacement, and which observations would force an indeterminate result.

### Q786

**A bend-powered robot in a sealed wearable patch**

Design a biohybrid microrobot inside a skin-external, sealed patch that takes in an isolated sweat sample. Bending moves a shuttle between the sample and a reading window. A cell-free indicator on the shuttle changes state on sample contact. The patch must distinguish an exposure record from a day with no bending, and it may not report a person's health status from that signal. The indicator is also sensitive to drying. Decide where motion, sample validity, memory and visible output belong in the system. Explain what the user would see after an incomplete trip and how that differs from a valid negative sample.

### Q787

**A private, single-session readout with a resettable reporter**

An external training patch contains a small biohybrid shuttle that visits two isolated model-fluid reservoirs in sequence. Its protein reporter resets on leaving either reservoir. The user wants to compare those visits during a session, then erase all evidence of the session on removing the patch. The reader has no network connection and must not retain the result. Design a body, local state and user interface that support the comparison, identify who or what authorizes erasure, and specify what the display does if the patch is detached halfway through the second visit.

### Q788

**An overwrite rule for a living-material teaching robot**

Design a sealed desktop robot that demonstrates how biological memory can change a later decision. At one station, a removable cell-free logic cassette encounters either of two benign cue classes. At a later fork, the robot should select the branch associated with the last independently confirmed cue. A brief contradictory cue during transit must not overwrite the stored decision, while a genuine replacement at the next teaching station must be able to do so. The display may show the selected branch and one additional status indication. Design the write, hold, revise and read functions, assign them between cassette and carrier, and explain how an interrupted revision would be made visible without sending the robot down an unsupported branch.

### Q789

**A gripper that must return an object on loss of power**

Design a biohybrid tabletop manipulator for sorting soft reference objects in a sealed accessible exhibit. Its cell-free contractile strip provides pulling motion while energized and relaxes afterward. The manipulator must keep an object supported during transfer, yet a power interruption must return it to an identifiable safe receptacle without requiring the visitor to reach inside. Objects can be picked up successfully but subsequently slip. Specify how the body, gripper, passive features and feedback divide responsibility. Show how the robot distinguishes grasp, arrival and release, and justify a design change that would make one fault safer at a cost elsewhere.

### Q790

**A robot whose monitoring behavior changes what its sensor remembers**

Design a biohybrid robot inside a sealed sampler for an inert material that leaves brief, harmless vapor traces. A reversible biological recognition unit can signal a trace, but a slow biological adaptation process suppresses repeated responses during prolonged exposure. The task is to find distinct emitting regions without counting every short revisit as a new source. The robot can choose to stay, leave, or return to a designated clean pocket; travel consumes part of its inspection opportunity. Specify how the fast and slow states are used, when external location information must override or qualify the biological state, and what drives each motion choice. Explain how the robot can avoid calling a continuously exposed but adapted region clean.

### Q791

**A mobile inspector for a retained water sample**

Design a biohybrid microrobot that inspects an already collected water sample inside a closed cartridge. Suspended benign particles can cloud a protein indicator and their distribution is part of the spatial structure that must be preserved. The requested output is a map of regions with a dissolved-marker response and a separate indication of where the map is unreadable. Removing all particles would destroy the sample's spatial structure. Propose an embodied inspection strategy that preserves the structure, keeps coverage information and separates optical obstruction from a negative marker response. Explain where the device should stop claiming a complete map.

### Q792

**Distinguishing a new fault from the chemical trace of repair**

Design a biohybrid inspection robot for a closed demonstrator built from self-recovering, nonliving gel tiles. A harmless molecular cue appears at a fresh surface break and can also linger after the gel has resealed. A second reversible biological interface can distinguish sustained contact with an intact surface from loss of support. Each tile must receive a useful status: new break suspected, recovery observed, or still unresolved. The carrier can leave a removable location marker but cannot store a full time series. Specify the biological logic and minimal history needed to distinguish an active break from chemical aftermath. Describe a change in robot behavior when support returns, and explain how you would handle two adjacent breaks encountered between visits.

### Q793

**A light-responsive carrier with a light-sensitive sample**

In a sealed teaching cartridge, an unmodified light-responsive biological mover is confined inside the body of a small robot. Its behavior can provide motion; it is not a sensor for the sample. The robot must carry an inert marker past two inspection windows containing light-sensitive reference material. The only available viewing path is also the path through which light reaches the mover. Design the body, task sequence and division between biological motion and external observation so that the act of reading does not change the reference material enough to invalidate a visit. Explain what the robot should do if motility and observation cannot be adequately separated.

### Q794

**A robot for comparing two sealed ecological samples**

A museum wants visitors to compare how a bio-derived humidity-sensitive strip bends over two enclosed soil samples. The strip itself remains in a separate headspace compartment, and the soils must never share air. A moving pointer must show the difference and return to neutral when either compartment is opened. A single strip carried directly between chambers could import moisture history from the first chamber. Design a biohybrid mechanism that performs the comparison, explains what material or signal crosses each boundary, and prevents a stale state from being displayed as a difference. Define a condition under which the device must decline a comparison. Make a valid zero difference distinguishable from an unavailable comparison.

### Q795

**A field cartridge that can report failure after a long return**

A sealed environmental sample cartridge is read in a laboratory only after transport. Inside, a biohybrid shuttle examines an inert witness surface using a cell-free contact reporter. A positive contact response may fade during the return journey, and a transport shock may release the shuttle from its dock even if sampling never happened. Design a system that can later distinguish a valid positive visit, a completed negative visit and a cartridge that never completed sampling. Choose which information should persist mechanically or biologically, where evidence of docking belongs, and how to prevent a shock from creating the appearance of a completed visit.

### Q796

**One reader shared by incompatible robot heads**

A laboratory can buy one reusable desktop reader for two recoverable biohybrid robot heads. Head A is a contact probe with a protein film visible only while pressed against its target. Head B is a soft manipulator whose biopolymer latch retains its final position after release. A single unqualified display labeled “completed” would mean different things for the two heads. Design the docking interface, power-loss behavior and reporting contract so a user can swap heads without reinterpreting old records. Specify where head-specific decisions occur, what evidence is required for each completion claim, and how an unrecognized head is handled.

### Q797

**An event-driven robot with no usable global clock**

A sealed microfluidic model has an inlet witness, an inspection alcove and a return bay. A mobile biohybrid robot must record whether a soft reference membrane changed state after the inlet witness was crossed and before the alcove was left. A protein reporter responds reversibly only while touching the membrane. Travel times vary and the robot has no useful clock. Design the robot's physical route, memory and reset behavior. A visit may be interrupted at any point and a robot may revisit the alcove without returning to the inlet. Explain how the report distinguishes a valid event from an old or out-of-window signal. If observation is broken while the window is open, specify which positive and negative claims remain supportable.

### Q798

**A robot that can surrender a blocked lane**

Two reusable accessories share a sealed microfluidic inspection lane, but only one may occupy it at a time. One is a biohybrid soft robot that uses a contractile biological element to present an inert coupon to an optical window. The other is an independent service carriage. A dim window might indicate a lost coupon, a robot stuck between stations, or an optical fault. Design the robot and its lane interface so servicing cannot proceed on a false assumption of clearance. Address coupon support, where to place a clearance witness, how a stalled robot is isolated or recovered, and how a user can resume after the cause is identified.

### Q799

**A prototype whose biological actuator may be unavailable**

Design a sealed teaching microrobot that normally uses a confined biological actuator to carry a soft bead between two marked sites. The exhibit must remain understandable if the actuator becomes temporarily inactive. A passive return spring is available, and an instructor can reposition the robot at a dock, but a successful demonstration is meant to show work attributable to the biological actuator. Decide what should keep operating during a fault, how the architecture separates useful fallback motion from an actuated transfer, and what evidence requalifies biological operation. A student looking only at the final bead position must not be shown a false success.

### Q800

**A complete system for inspecting a replaceable scaffold insert**

Design a recoverable biohybrid microrobot for a shared organ-on-chip instrument. Its mission is to report whether an isolated reference insert experienced sustained deformation at a specific scaffold region during a completed visit. The insert may be swapped while the reader is offline. A reversible protein film can sense strain at contact; a mechanical witness can retain a state through the return trip but cannot identify a region on its own. The mission must leave the insert usable and report “unknown” when attribution fails. Propose an end-to-end design, compare it with one simpler architecture, and walk through both a valid visit and a visit interrupted by an insert swap. Identify an observation that would force you to revise the design.
