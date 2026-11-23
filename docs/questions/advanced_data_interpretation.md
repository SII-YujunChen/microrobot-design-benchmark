# Advanced Data Interpretation Challenge

[All collections](../QUESTIONS.md) · [Download the question-only JSONL](../../data/advanced_data_interpretation.jsonl) · [Scoring guide](../EVALUATION.md#score-a-challenge-case)

These 100 English-language cases use synthetic archived microrobot measurements, image tracks, and evaluation records. All the evidence required to attempt a case is in its prompt. Support each decision with the relevant records or calculation, and specify what remains uncertain.

| Topic | Questions |
| --- | --- |
| Measurement and calibration | [Q701–Q725](#q701) |
| Tracking and time series | [Q726–Q750](#q726) |
| Evidence and study validity | [Q751–Q775](#q751) |
| Decisions and benchmarking | [Q776–Q800](#q776) |

## Measurement and calibration

### Q701

**A color ratio under a moving black level**

In two archived images of the same stationary optical microrobot, the reporter/reference channels read (154, 106) and (245, 173) digital counts. Masked pixels next to the robot read (10, 10) and (29, 29), respectively. Both channels share the same multiplicative gain within an image. A response requires an increase of at least 5% in reporter intensity relative to the reference after background correction. Determine whether a response occurred. The image header also claims the gain doubled. Assuming the reference emitter was constant, test that claim independently and explain whether the response decision depends on it.

### Q702

**Did the reporter patch broaden or did the optics blur?**

A fluorescent patch on a biohybrid microrobot looks wider in an archived second scan. Model both its intrinsic lateral profile and the optical point-spread function as Gaussian; their variances add. In the first scan, the observed standard deviation was 5 micrometers and a point reference gave an optical standard deviation of 3. In the second, the observed standard deviation was 10, but the optical standard deviation lies between 7.5 and 8.5 micrometers. Other errors are negligible. Bound the intrinsic width change, decide whether broadening of at least 40% is established, and give the critical second-scan optical width for that claim.

### Q703

**A clipped hotspot and an unpaired second exposure**

An archived microrobot image clips each pixel at 255 counts. At unit exposure, three preselected pixels read 140, 170, and 255. Matched dark pixels read 20 each. The qualification rule requires their mean true dark-corrected count to exceed 170 strictly. A second image at half exposure contains an unclipped bright feature, but the robot moved and no registration links that feature to the three original pixels. Derive the tight lower bound on the first mean, state whether qualification is forced, and specify the minimum integer pre-clipping value of the third pixel that would satisfy the rule.

### Q704

**A ratiometric correction with unequal attenuation**

In a microrobot imaging archive, matched shallow and deep views have reporter/reference ratios of 2.0 and 1.6 after dark subtraction. Calibration beads with constant intrinsic ratio give deep-to-shallow transmission multipliers of 0.60 for the reporter band and 0.75 for the reference band. Use a multiplicative attenuation model. Estimate the change in the robot's intrinsic ratio, then repeat the inference when the reporter multiplier is known only to lie in [0.55, 0.65] and the reference multiplier is exact. Can the archive establish a fall of at least 10% in the intrinsic ratio?

### Q705

**One reading, two hysteresis branches**

A microrobot readout channel was calibrated against a dimensionless mechanical-load index x between 0 and 10. On a steadily increasing load it obeyed y = 10 + 4x counts; on a steadily decreasing load it obeyed y = 18 + 4x. An archived trace ends at y = 34 with its last three counts equal. Earlier frames are missing. The classification threshold is x ≥ 5. Report all branch-consistent loads and their classifications. An earlier time-stamped frame from the same uninterrupted monotonic segment is recovered at y = 38. Reassess, treating the final plateau as compatible with either preceding direction.

### Q706

**A calibration that looks linear at its endpoints**

A microrobot force-readout archive uses an optical scale x in arbitrary reference units. Standards at x = 0, 2, 4, 6 yielded 10, 28, 50, 76 counts. A proposed affine calibration passes through the two endpoints; acceptance requires a residual magnitude of at most 2 counts at every interior standard. Decide whether to accept it. For an unknown at 39 counts, compare the endpoint-fit estimate with piecewise-linear interpolation between the adjacent standards and determine whether switching methods changes the call x ≥ 2.8. Separate that numerical comparison from the evidence for interpolation between standards.

### Q707

**Worst-case bounds after spectral unmixing**

Two optical channels on a biohybrid microrobot produce dark-corrected counts L = R + 0.5F and H = 0.2R + F, where R is reporter output and F is a reference contribution. A frame reads L = 120 and H = 84; each recorded count can differ from its true value by up to 2, independently. The archive labels a frame positive only if every compatible R exceeds 90. Recover the nominal contributions and the worst-case interval for R, then adjudicate the label. Show which pair of measurement errors produces the lowest possible R.

### Q708

**A rotation frequency that changes under resampling**

The projected marker on a microrobot replay follows a single cosine with unknown positive frequency below 10 Hz. A 10 Hz camera estimates an apparent frequency of 2 Hz. An independent 12 Hz camera observing the same steady motion estimates an apparent frequency of 4 Hz. Frequencies are exact. Define apparent frequency as the smallest distance between the true frequency and an integer multiple of the sample rate. Reconstruct all candidates from each camera, determine whether the two records resolve the true frequency, and decide whether the direction of rotation can be recovered from these frequency magnitudes alone.

### Q709

**Displacement after rotation of the image plane**

A stationary pair of fiducials A and B appears at (0, 0) and (4, 0) micrometers in frame 1 of a microrobot track, then at (10, 5) and (10, 9) in frame 2. Assume an orientation-preserving rigid camera transform with no scale change. The robot appears at (1, 2) in frame 1 and (9, 7) in frame 2. Estimate its displacement vector in frame-1 coordinates and decide whether it moved more than 1.5 micrometers. Explain why correcting only for the motion of fiducial A yields a different decision.

### Q710

**The precision of a shared-reference difference**

Two synthetic microrobot readout estimates are 31 and 26 units after calibration to the same reference. Their uncertainties each contain one identical additive reference error with standard deviation 3 units and independent readout errors with standard deviations 2 and 1 units, respectively. Flag a difference only when its absolute value exceeds twice its standard uncertainty. Compute the standard uncertainty of the difference and the flag. Repeat under the counterfactual that the two references were independent, with the same 3-unit standard deviation each. Explain the change using covariance rather than changing the recorded values.

### Q711

**Comparing two event detectors with partial adjudication**

Two detectors classified the same 100 prerecorded microrobot flashes. Both flagged 10 events, only A flagged 8, only B flagged 12, and neither flagged 70. An independent reference reviewed all disagreements: 6 of the 8 A-only events and 3 of the 12 B-only events were real flashes. Agreements were never reviewed. Compute the exact difference in overall accuracy (A minus B), and give the tightest possible interval for the difference in sensitivity. Explain which comparison can be reported as a point estimate without assuming that detector agreement establishes truth.

### Q712

**An incomplete paired readout archive**

A qualification report claims that over half of 60 individual microrobots showed a strict increase in optical signal between two archived views. Of the 42 units with both measurements, 26 increased and 16 did not. In six additional units the second reading clipped at 90 counts and the first was below 85. In the other twelve, the second reading is missing and no ordering information survives. Treat clipping as a lower bound and trust the identity pairing. Bound the increase fraction for all 60. Then assess the claim if the six clipped records could instead represent duplicate views of other units, leaving six distinct units unobserved.

### Q713

**Applying detection and quantification thresholds on the correct scale**

A stored microrobot fluorescence trace has raw value 63 counts. Its matched local blank has mean 45 and standard deviation 3 counts. A legacy review used a global blank of mean 35 and standard deviation 2 counts. The archived rule detects when net signal exceeds 3 blank standard deviations and quantifies when it exceeds 10. The appropriate local calibration slope, in net counts per signal unit, is only known to be between 4 and 6. Audit the legacy classification, give the range implied by the local slope ignoring other errors, and decide what quantitative claim the stated reporting rule permits.

### Q714

**A duty estimate with unequal frame lengths**

A microrobot reporter replay contains three nonoverlapping integrations lasting 1, 1, and 8 s. After calibration their mean readings are 90, 90, and 30 counts/s. During each integration the reporter switches only between 20 counts/s (off) and 100 counts/s (on); integration returns the time average. There is a 2 s recording gap between integrations, with no information about state. A decision memo claims that at least 40% of the full 12 s elapsed time was on. Derive the tight duty-fraction interval and check whether averaging the three frame readings equally would support a misleading conclusion.

### Q715

**A direct-versus-ratio normalization audit**

An archived panel contains two microrobots, with corrected reporter/reference photon totals (12, 4) and (45, 30). The intended measurand is the mean of the two individual reporter/reference ratios, with each identified robot weighted equally. The dashboard instead divides total reporter by total reference. The acceptance cutoff is a mean ratio of at least 2.0. Compare both estimates and qualification decisions. A reviewer then learns the high-reference robot was counted twice with identical totals in the stored export. Quantify the dashboard's new estimate and explain which correction actually restores the intended measurand.

### Q716

**Photon counting across detector settings**

A stored optical microrobot record spans a detector setting change. Before the change, total and blank count rates were 400 and 100 per second with dead time 0.001 s. After the change they were 500 and 100 per second with dead time 0.0005 s. For an observed rate m, use true rate r = m/(1 - m times dead time). Blanks were acquired separately at the relevant setting, with the same underlying background as their paired totals. An increase requires the corrected net rate to rise by at least 5%. Audit the raw-rate claim and explain the required order of operations.

### Q717

**A site effect entangled with a camera effect**

Two archived chamber sites, east and west, were imaged with two cameras. Reported microrobot signal means are east/A = 43, east/B = 35, west/A = 38, and west/B = 30 counts. The original comparison included only east/A and west/B. Assume an additive site effect and camera offset, no interaction, and one unknown common origin. Decide how much of the original contrast belongs to site and how much to camera. Check the no-interaction assumption using all four cells. If west/A is later corrected from 38 to 34 while the other cells stand, determine which contrast can no longer be described by a single camera-independent site effect.

### Q718

**Can three blurred reporter readings come from one pulse?**

An archive models a microrobot readout as y[t] = 0.5x[t] + 0.5x[t-1], with nonnegative latent light outputs and x[-1] = 0. Three successive measured outputs y[0], y[1], y[2] are 4, 6, and 1 units. Audit the nominal model by reconstructing the latent trace. A corrupted record could affect y[2] only; y[0] and y[1] are independently verified. Find the smallest nonnegative change to y[2] that restores physical feasibility, and determine whether a single nonzero latent time bin is then compatible with the two verified measurements.

### Q719

**A detector edge loses a fraction of the signal**

Two adjacent image zones report counts from a stationary microrobot pair. Optical calibration says 80% of the left source appears in the left zone and 20% in the right; 10% of the right source appears in the left zone, 70% in the right, and the remaining 20% is outside the frame. The dashboard reports 65 counts in the left zone and 50 in the right. Recover the two source intensities and the unobserved counts. Compare the true and dashboard left fractions to a threshold of at least 60% left-source contribution, explicitly identifying the denominator in each fraction.

### Q720

**Row timing and the order of two transitions**

A rolling-shutter camera marks each row's exposure midpoint at frame stamp + row index times 0.10 ms; rows run from 0 to 99. Two visible microrobot landmarks change state. The last unchanged and first changed observations of A are at frame stamps 0 and 10 ms on row 90. For B they are at 10 and 20 ms on row 0. Assume exact midpoint sampling, one persistent transition per landmark, and no timing error. Bound the transition time for each landmark and the possible signed delay B minus A. Decide whether order follows from their different first-changed frame stamps.

### Q721

**Two calibrations fit every available control**

An optical microrobot archive gives a lower reference of 0 units at detector input x = 0 and an upper reference of 10 units at x = 10. Two candidate calibrations pass both checks: A reports x; B reports x squared divided by 10. No intermediate calibration reading was taken. A recorded margin signal has x = 6; a decision requires calibrated signal of at least 5 units. Bound the answer over the two models. Exactly one archived intermediate standard can now be recovered at x = 2, 5, or 8. Its reading may differ from the correct model by up to 1 unit. Which choice guarantees discrimination and why?

### Q722

**Do two optical rings actually touch?**

A camera segmenting fluorescent ring tags on biohybrid microrobots exports a six-by-six binary mask. The row strings, top to bottom, are 111000, 101000, 111000, 000111, 000101, 000111. A foreground pixel has value 1; a hole is a background component cut off from the image boundary. Compare two conventions: foreground edge adjacency with background edge-or-corner adjacency, and foreground edge-or-corner adjacency with background edge adjacency. For each, calculate the foreground component count, hole count, and Euler number (components minus holes). The dashboard infers exactly two physically separate robots solely from the two holes. Assess this inference and identify one archived observation that could distinguish the alternatives.

### Q723

**A dark frame is not a flat field**

The same microrobot target moved between two pixels in an archived camera stream. At pixel P the target, dark, and uniform-reference frames read 90, 10, and 110 counts. At pixel Q they read 146, 26, and 226. The reference delivered the same known radiance to P and Q, and each pixel is affine over this range. Estimate the target's radiance change from P to Q and audit the conclusion from subtracting dark counts alone. If the uniform reference at Q actually had only 90% of the radiance at P during calibration, revise the inferred change.

### Q724

**A change that depends on unresolved signal labels**

A robot imaging archive contains 80 annotated candidate events in an early window and 80 in a late window. Early labels are 23 confirmed reporter flashes, 49 confirmed artifacts, and 8 unresolved. Late labels are 34 flashes, 33 artifacts, and 13 unresolved. The protocol qualifies an increase only when the late flash fraction exceeds the early fraction by at least 0.10 of all candidates. Find the sharp difference bounds and adjudicate. What is the minimum number of unresolved early records that must be newly verified as artifacts to guarantee qualification, even if the remaining early uncertainties are real and every unresolved late event is an artifact?

### Q725

**A correction changes the scale of the acceptance rule**

An archive qualified a microrobot reporter reader when both repeatability and bias passed: maximum within-standard range at most 4 reference units, and absolute mean bias at most 2 reference units at each standard. At reference 20, raw replicates are 24 and 28; at reference 40, they are 50 and 54. A proposed affine correction fits the two replicate means exactly. Derive the inverse calibration, evaluate both gates on the corrected readings, then independently audit a previously unseen standard at 30 with raw replicates 36 and 38. Decide whether the validation standard overturns the calibration-set decision and whether passing establishes agreement away from the three measured levels.

## Tracking and time series

### Q726

**Which clock leads?**

An archived biohybrid microrobot movie and its optical reporter log use different clocks. Two synchronization marks at camera times 4 and 44 s appear at log times 6.0 and 46.8 s. Assume an affine clock map and exact mark times. The robot crosses a map boundary at camera time 29 s. The logged reporter onset is 31.70 s with a bounded error of ±0.25 s in log time. Estimate the signed delay (reporter minus crossing), bound it, and decide whether the record establishes the order of the two events.

### Q727

**Identity after a crossing**

A one-dimensional archive shows two visually indistinguishable microrobots. At frames 0 and 1, robot A is at −2 and −1 µm, while robot B is at +2 and +1 µm. Both disappear in frame 2. These are projected positions, so the robots can share a recorded coordinate in the missing frame. At frame 3 two spots reappear at −1 and +1 µm. The maximum displacement is 1 µm per frame and either robot may reverse direction or pause. A straight-line tracker labels the right-hand spot as A. Determine the admissible frame-3 displacements of A from frame 0 and which direction-of-motion claim survives the identity ambiguity.

### Q728

**Dwell durations at the movie edge**

Six independent microrobot region visits start on camera. Recorded dwell times in seconds are 2 (right-censored), 3 (exit), 4 (exit), 4 (right-censored), 7 (exit), and 9 (right-censored). To summarize the archive, the team uses Kaplan–Meier survival, with exits processed before censoring at a tied time. A reviewer reports the median of the completed visits instead. Compute the survival probability just after 4 s, compare the two median dwell estimates, and state the assumption that limits the survival estimate if robots tend to disappear when their signal weakens.

### Q729

**Bounds on a single recorded pulse**

A fluorescence camera sampled a microrobot at 0, 40, 80, 160, 200, 200, and 260 ms. Its binary reporter labels are 0, 1, 1, 1, 0, 0, 0. The two rows at 200 ms are duplicate exports of one exposure. An analyst labels this a single sustained event lasting at least 150 ms. Assuming just one contiguous event, bound its possible duration from the observations. Then drop that assumption and assess whether the missing frame and duplicate can substantiate the analyst's continuity and duration claim.

### Q730

**A common timestamp is not a causal clock**

Four independently recorded microrobot movies contain an external scene marker and two readouts, a dimming event D and a motion-label transition M. The marker occurs at absolute seconds 10, 41, 92, and 151. Relative to each movie's marker, D occurs at 2, 4, 2, 4 s and M at 7, 5, 7, 5 s, respectively. A reviewer cites the alignment of absolute timestamps as evidence that D drives M after a fixed delay. Calculate the paired delays and examine the marker-relative pattern. What temporal and causal conclusions does the archive support?

### Q731

**Motion during camera zoom**

Two stationary reference beads in a one-dimensional microrobot video are a known 12 µm apart. At frame A their coordinates are 10 and 50 pixels and the robot center is at 34 pixels. At frame B the references are at 20 and 100 pixels and the robot is at 68 pixels. Allow an unknown affine pixel map at each frame, treat reference positions as exact, and bound each robot-center reading error by ±1 pixel. The archive certifies a displacement only if its magnitude exceeds 0.5 µm. Does the apparent pixel jump meet that criterion under any admissible localization error?

### Q732

**Localization noise mistaken for reversal**

For a long one-dimensional microrobot track sampled every 0.5 s, the estimated mean squared displacements at lags of one and two frames are 0.20 and 0.32 µm². The proposed observation model is uncorrelated diffusive steps with diffusion coefficient D plus independent position-localization error of variance s² at each frame; it predicts MSD(k) = 2DkΔt + 2s². The observed covariance of adjacent signed displacements is −0.041 µm². Estimate D and s, derive the adjacent covariance due to localization error, and assess a claim of active direction reversal.

### Q733

**An unobserved six-second interval**

An archived speed proxy for a biohybrid microrobot was exported at irregular times 0, 1, 2, 8, and 10 s, with values 0, 4, 4, 0, and 0 µm/s. The reporting threshold is a time-averaged proxy strictly above 2 µm/s over the full ten seconds. Two replay programs respectively interpolate linearly and hold the last observation constant until the next timestamp. Compute both time averages, identify the interval driving the discrepancy, and state which decision, if any, is justified without information about the reconstruction rule or the unsampled trajectory.

### Q734

**Frames and robots answer different questions**

A retrospective event classifier is evaluated on four separately tracked microrobots. Correct labels and total labeled frames for the four tracks are 90/100, 1/5, 1/5, and 4/5. The evaluation contract first picks a robot uniformly and then picks one of its labeled frames uniformly; certification requires at least 75% expected correctness under this draw. An earlier report instead pooled all 115 frames. Calculate both scores, decide whether the archive qualifies, and explain what should be resampled to reflect between-robot variability if the four robots are independent.

### Q735

**An inconsistent event-memory audit**

A binary event-memory flag in an archived robot replay toggles once per detected pulse. Its exact snapshots at four consecutive boundaries are 0, 1, 1, 0. A separate timing constraint permits from zero to two pulses in each of the three gaps. The pulse counter for the entire replay reports three, and a slide attributes the discrepancy to a missed pulse in the middle gap. List the compatible gap counts and total counts from the snapshots, reconcile or reject the counter, and specify how much can actually be localized from these records.

### Q736

**Two models of a persistent readout**

An archived reporter trace is reduced to four consecutive equal-duration windows. The observed normalized intensities are 2, 2, 5, and 5. Model L predicts a constant intensity followed by a single permanent level change after window two, with both levels fitted. Model B predicts one isolated bright window against a fitted constant background and can choose which window is bright. For each model, fit the free levels by least squares and report its minimum residual sum of squares. Which temporal description is supported over the four observed windows, and what claim about later memory retention would require more data?

### Q737

**What two-dimensional straightness can establish**

A tracked microrobot appears at projected coordinates (0,0), (3,4), and (6,0) µm in three consecutive frames. The first and last heights are both known to be zero; the intermediate height is unknown but has magnitude at most 12 µm. Define path length as the sum of the two straight three-dimensional chords between frames and efficiency as three-dimensional endpoint displacement divided by this length. A retrospective label calls paths efficient only above 0.50. Derive the full admissible interval for efficiency and decide whether the projection alone determines this label.

### Q738

**One visit, two predicted segments**

An annotated microrobot video contains three region visits in half-open intervals [2,8), [10,14), and [20,22) s. A tracker predicts [2,5), [5,9), [10,14), and [19,24). An event is correct if intersection divided by union is at least 0.50 with a distinct annotated visit, with one-to-one matching. A second metric computes intersection over union of all occupied time, ignoring visit boundaries. Score both metrics, using event F1 = 2TP/(2TP+FP+FN), and explain why a favorable duration score need not imply accurate event segmentation.

### Q739

**A wrapped clock and an unavailable frame**

A robot trajectory export uses an unsigned 8-bit camera timer in 1 ms ticks. Successive saved frames have timer values 240, 252, 8, 28, and 52. The header guarantees that every interval between saved frames is positive and less than 256 ms, even when frames are missing. A reviewer measures a delay from the second saved frame to the fourth and compares it with a limit of 40 ms. Recover the elapsed timeline relative to the first frame, decide the limit comparison, and state what extra ambiguity appears if the header guarantee is absent.

### Q740

**A greedy timestamp match loses a real event**

Three reference turning events in a robot replay occur at 10, 14, and 23 s. A detector reports events at 11, 9, and 24 s in descending confidence order. A detection may match one unused reference within 3 s inclusive. The legacy scorer greedily assigns each detection, in confidence order, to the nearest eligible unused reference. A proposed scorer first maximizes the number of matches and then minimizes total absolute timing error. Compare the assignments and event F1 scores, and identify whether the change in score reflects a change in detector output.

### Q741

**An apparent two-frame forecast**

A binary brightness marker on an annotated robot track stays zero through frame 3 and one from frame 4 onward. A replay tool assigns to frame t the mean of the five raw marker values centered on t. It calls an alert when the mean reaches 0.20, and the report credits the tool for forecasting the change. A second version averages the five values ending at t. Frames are spaced 0.25 s apart, with enough zero-valued prehistory. Find the first alert in each version and decide what evidence of predictive lead remains for a real-time observer.

### Q742

**A time warp conceals a duration error**

Two offline decoders label the same robot movie. The annotated sequence consists of quiescence for 2 s, a reporter pulse for 1 s, and recovery for 5 s. Decoder A reports the same state order with durations 2, 4, and 2 s. Decoder B reports quiescence for 3 s followed directly by recovery for 5 s. One reviewer permits arbitrary monotone time stretching within each nonempty state and compares only state order. Another scores exact agreement on the original time axis. Compare the decoders under both rules and defend a metric for an archive intended to preserve event duration.

### Q743

**Can continuous residence be inferred across a gap?**

A tracked microrobot is recorded at coordinates x=3 µm and x=4 µm at the two ends of a 2 s imaging gap. The mapped region is the closed segment [0,10] µm. Its motion is continuous and one-dimensional, and the archived maximum speed is 3 µm/s. A second analyst proposes 4 µm/s as a plausible upper bound. Use the endpoint positions and travel budget to decide, under each speed bound, whether continuous residence is guaranteed. Explain why interpolating a straight path between the endpoints does not resolve the disagreement.

### Q744

**Aligned axes without a common heading**

Four equally weighted microrobot tracks yield visible long-axis angles of 5°, 175°, 185°, and 355° in a fixed camera coordinate system. The imaging algorithm cannot label the ends of each body, so angles separated by 180° describe the same observed axis. One analyst computes the length of the mean unit heading; another computes the length of the mean unit vector after doubling each angle. Compare both statistics for the listed representatives, explain which one is invariant to relabeling a body's ends, and assess a claim of collective travel to the right.

### Q745

**An encounter created by interpolation**

At t=0 s two archived microrobot centers are at A=(−1,0) and B=(0,−1) µm. At t=2 s they are at A=(1,0) and B=(0,1). A remains on the x-axis, B remains on the y-axis, and either may pause; each speed is at most 2 µm/s. The middle frame is missing. An encounter requires center separation at most 0.5 µm at some instant. Evaluate synchronous linear interpolation, then construct a second admissible motion and determine whether the encounter label is identifiable from the saved frames.

### Q746

**A future observation changes a past label**

A microrobot reporter has two latent states, H and L. Before frame 1 each has probability 0.5. Between frames the state remains unchanged with probability 0.90, symmetrically. The observed frame-1 symbol has likelihood 0.80 under H and 0.20 under L. The observed frame-2 symbol has likelihood 0.10 under H and 0.90 under L. Emissions are conditionally independent given the states. At a 0.50 decision threshold, compare the frame-1 call using only its own observation with the retrospective frame-1 call using both frames. Which call could the original online observer have made?

### Q747

**Differential visibility in two regions**

An archived chamber movie was divided into 20 fixed one-second bins per region, independently of visibility. In region A, a microrobot reporter was readable in 12 bins and positive in 9. In region B it was readable in 18 bins and positive in 10. A hidden bin can be positive or negative, and the archive provides no relation between visibility and state. Compare positive fractions among readable bins, then derive sharp bounds for each fraction across all scheduled bins and for A minus B. Can a higher full-record fraction in A be certified?

### Q748

**Aliased oscillations in a reporter replay**

Two exact candidate models for an archived microrobot reporter are y(t)=cos(2πft), with time in seconds, unit amplitude, zero offset, and phase zero at the common origin. Their frequencies are 0.05 and 0.20 Hz. The regular replay samples only at t=0,4,8,… s. An independently time-stamped archived frame at t=2 s records −0.80 with a bounded intensity error of ±0.10. Show why the regular samples alone cannot select a frequency, evaluate the two candidate values at the extra timestamp, and decide what the extra frame establishes within this model set.

### Q749

**A persistent glow or camera carryover?**

A reporter replay stores y[k]=x[k]+0.5x[k−1], with x[k] the binary underlying event state and x[−1]=0. The camera carryover coefficient is known exactly. Frames 0 through 4 report values 0, 1, 0.5, 1, and 1.5, with no noise. A legacy annotator treated every positive y as an active state, merging detections separated by less than one full frame of darkness in y. Reconstruct x, compare the event runs under each interpretation, and state whether the record supports a single continuously active underlying event.

### Q750

**Frames are not independent replicates**

Six independently recorded robot movies each yield a paired change in mean reporter-track alignment error, defined as old decoder error minus new decoder error. Changes in micrometers are +1, +1, +1, +1, −1, and 0. Each movie contains hundreds of temporally correlated frames. A report claims a significant improvement at the one-sided 5% level after treating all positive frames as independent. Use an exact one-sided sign test over movies, dropping ties and assuming fair independent signs under the null. Compute the p-value and say what can be reported about direction and statistical support.

## Evidence and study validity

### Q751

**A ranking that depends on the image mix**

Two archives evaluate readers A and B on labeled microrobot reporter images. The only recorded stratum is image clarity. A is correct on 90 of 100 clear images and 4 of 10 dim images. B is correct on 19 of 20 clear images and 45 of 100 dim images. The intended archive contains equal numbers of clear and dim images. Calculate the pooled and target-standardized accuracies, select the reader favored for that target, and state the assumption that would justify transferring this ranking to new runs.

### Q752

**Counting original recordings behind three reports**

An audit requires at least 70% successful detection across unique positive microrobot transit recordings, counting each recording once. Report R1 detects 8 of 10 recordings. R2 reports 16 successes in 20 views. Its manifest shows two crops of each R1 recording, and both crops agree with the R1 verdict. R3 detects 2 of 5 previously unseen recordings under the same definition. A reviewer pools all three reports. Compute that estimate and the estimate supported by the manifest. Decide the audit outcome and identify what the extra crops can establish.

### Q753

**Paired significance without the pairing**

Readers A and B reviewed the same 50 one-robot clips. A localized the robot correctly in 43 clips and B in 37. The paired results were lost. For a two-sided exact sign test on disagreements, use twice the smaller binomial tail under equally likely wins, capped at one. Show two feasible sets of discordant win counts that give different decisions at 0.05. Can the archive support a claim of a significant paired improvement? Name the smallest summary from the original audit that would settle the test.

### Q754

**Selective verification of a negative readout**

A microrobot fluorescence reader flagged 50 of 200 archived clips. An independent reference review confirmed a real event in 32 of the 50 flagged clips. Among the 150 unflagged clips, 30 were chosen for review because they looked suspicious, and 3 contained real events. The other 120 are unverified. The audit requires sensitivity of at least 80%. Derive assumption-free lower and upper bounds. State precisely how many additional missed events among the 120 would be compatible with passing, and explain whether the reviewed negatives support a point estimate.

### Q755

**A reference panel that saw the predictor**

A paper reports 94% agreement between a microrobot state classifier and a final reference panel on 100 trajectories. On the 60 trajectories with an independent reference, the classifier agreed 54 times. For each of the other 40, the optical reference was inconclusive and the panel copied the classifier’s label. Treat the independent labels as correct and leave the true state of each remaining trajectory unrestricted. Bound the full-cohort accuracy, interpret the published 94%, and decide whether an 85% full-cohort accuracy claim follows from these data.

### Q756

**An unobserved optical regime**

In a labeled archive, a reporter-state reader is correct on 45 of 50 bright-background microrobot clips and 30 of 50 dark-background clips. A new collection is 25% bright, 25% dark, and 50% patterned. No labeled patterned clips exist. For this question, treat the two observed stratum accuracies as fixed and transportable and assume only that patterned accuracy lies between zero and one. Bound the new collection's accuracy. Determine the minimum patterned accuracy needed for a 75% target and evaluate the proposed use of the original pooled accuracy as a guarantee.

### Q757

**Clip IDs that restart at each site**

Two sites archive passive microrobot reporter clips. Site North recorded N01 bright and N02 dark. Site South recorded S01 dark and S02 bright. The reader predicted bright, dark, bright, dark for N01, N02, S01, S02 respectively. During export the site prefix was dropped. A faulty join copied the North reference labels onto both sites by the remaining two-digit ID. Calculate the faulty and site-aware accuracies. Decide whether the published claim of at least 75% can be retained and specify a join invariant that would catch the failure even if some copied labels happened to be correct.

### Q758

**Leakage through alternate views of one transit**

A test archive has 100 microrobot transit videos, one test video per distinct transit. A later audit finds that for 60 test transits, an alternate camera view of the same transit appeared in the training set. The classifier was correct on 58 of these 60 and on 28 of the remaining 40. The team proposes shipping a new-transit accuracy claim of 86% based on its test score. Compute separate rates, assess what the existing clean subset identifies, and specify how the unit of a replacement split and independent testing should be chosen.

### Q759

**A revised label file changes a ranking**

A repository reports 42 of 50 correct for microrobot motion reader A and 40 of 50 for B against label file L1. A blinded audit issued L2 for the same clips, revising four binary labels. On three revised clips A had matched L1 and B had disagreed. On the fourth both had disagreed with L1. No other labels or predictions changed. Reconstruct both L2 scores and the ranking, then state what evidence a release note must preserve for someone to reproduce both comparisons without mixing label versions.

### Q760

**Two co-primary endpoints for reader replacement**

A team wants to replace an archived microrobot localization reader. Its prespecified rule requires simultaneous passage of two tests. The entire paired interval for new minus old rate of correct tracks must lie above -2 percentage points, and the entire interval for new minus old mean delay must lie below +5 ms. The archive gives a track-rate change of +1 point with interval [-1.5,+3.5], and a delay change of -1 ms with interval [-8,+6]. Apply the rule, distinguish an inconclusive result from evidence of unacceptable delay, and identify what change to the interval evidence alone would resolve the open test.

### Q761

**A clock change masquerading as reporter memory**

A study infers persistent reporter activity because six microrobot tracks have a last-positive optical frame labeled time 12 s, while a stimulus-off event is logged at controller time 10 s. A file header states that the optical clock reads 3 s ahead of the controller with synchronization uncertainty of plus or minus 0.5 s. Five other tracks used a synchronized camera and have their last-positive frame at controller time 11 s. All eleven traces end at their last-positive frame. Determine which group supports post-event positivity, what persistence duration can be bounded for the synchronized group, and whether either group identifies a memory mechanism.

### Q762

**A watermark that tracks the reference label**

A reader predicts a binary marker state from archived microrobot images. Each image also has a binary acquisition watermark in the border. The reference labels were assigned independently of the watermark. Among 80 images where the watermark matches the reference, the reader gets 76 right. Among 20 where it differs, the reader gets 3 right. Calculate accuracy and agreement with the watermark. Estimate accuracy if the two strata were equally common and within-stratum accuracy transferred. Do these figures establish that the reader uses the border? Describe an offline paired check that would discriminate this explanation from a correlated image feature.

### Q763

**A firmware update with a concurrent site change**

Site E switched to a new decoder for archived microrobot images and improved from 80% to 92% correct. Site C retained the old decoder and improved from 70% to 77% over the same periods. Each rate covers 100 separately labeled clips. The team requires a decoder-attributable improvement of at least five percentage points. At E, and only at E, a new camera was introduced with the decoder. Compute the controlled before–after contrast. Can the sign-off attribute it to the decoder, and what archived comparison would separate the two changes?

### Q764

**An apparent replication after searching four endpoints**

A lab compared two state readers on archived microrobot trajectories. Four exploratory paired tests returned p-values of 0.009 for brightness-state errors, 0.018 for false transition alarms, 0.040 for localization loss, and 0.200 for dropout. The analysis plan uses Holm's step-down procedure with family error 0.05 for these four tests. After inspecting all four, the team renamed false transition alarms its primary endpoint and called that result a replication. Apply the planned procedure, judge the transition-alarm claim, and describe a valid way to test that specific endpoint independently.

### Q765

**Combining detector success and readout success**

A demonstration claims at least 45 usable results from 60 microrobot passes. A usable result requires both a localized trajectory and an interpretable reporter state on the same pass. Review sheets initially give only marginal counts, with 51 localized and 48 interpretable. First decide whether those sheets settle the claim and bound the joint successes. An independently reconciled failure log then identifies exactly four passes that failed both checks. Update the result and explain why multiplying the marginal success proportions could disagree with the reconstructed number.

### Q766

**Reconciling coordinate conventions before combining studies**

Two reports describe displacement of passive reporter microrobots relative to a stationary mark. East is positive on the shared reference axis. Report A gives a mean displacement of +4 and an interval [2,6] in reference-axis units. Report B gives -5 and [-7,-3] in image-axis units. Its archive defines the reference coordinate as 12 minus the image coordinate, with the same length unit. Both reports processed the same 18 recordings with different tracking software. Assess directional disagreement, convert B's interval, and judge a proposed claim of independent replication based on both intervals excluding zero.

### Q767

**Comparing readers at the contracted operating point**

Two optical-state readers were evaluated on the same labeled microrobot archive with 80 true event clips and 200 true quiet clips. A report advertises reader A with 72 detections and 18 false alerts versus reader B with 66 detections and 4 false alerts. The contract permits a false-alert fraction of at most 3% of quiet clips. A second documented operating point for A has 60 detections and 6 false alerts. B has no other documented point. Select among the reported points to maximize sensitivity while meeting the cap, and state what broader comparison the evidence leaves open.

### Q768

**A change in alert counts under unequal observation**

An archive compares false alerts from two silent-state microrobot readers. A produced 12 alerts over 60 fully observable robot-hours. B produced 9 over a nominal 90 robot-hours, of which 54 hours had a missing optical channel and could generate no logged alert. The prespecified estimand is alerts per observable robot-hour, with a ceiling of 0.22. Recompute the comparison, determine who meets the ceiling, and explain what additional evidence would be required for a claim about the rate of alerts the reader would have produced throughout all 90 hours.

### Q769

**High agreement on rarely positive trajectories**

On 100 archived reporter trajectories two annotators independently call a binary state. They both call positive on 2, only A calls positive on 4, only B calls positive on 4, and both call negative on 90. A release rule requires at least 90% raw agreement and positive-specific agreement of at least 60%. Define positive-specific agreement as twice the concordant positives divided by the total positive calls by both readers. Apply both criteria, calculate Cohen's kappa using marginal expected agreement, and explain whether adjudicating only the two concordant positives could demonstrate reliability of the positive labels.

### Q770

**Apparent swimming in a moving image frame**

A paper concludes that all three archived microrobot clips show movement relative to their surroundings. In the same one-second interval, signed robot displacements in image pixels are +7, +6, and +3. Nearby fixed fiducials in the same clips move +6, +6, and -1 pixels respectively because the image frame shifts. The uncertainty in each robot-minus-fiducial displacement is at most one pixel. A directional movement claim requires the entire resulting interval to be strictly positive. Evaluate the three claims and state what the surviving clip can establish about the cause of movement.

### Q771

**A balanced validation archive and rare deployment events**

A passive microrobot imaging benchmark deliberately sampled 100 true events and 100 true quiet clips. A reader detected 90 events and falsely flagged 10 quiet clips. A different archive contains 1% true events. Assume the reader's sensitivity and false-positive rate transport unchanged and use expected frequencies, ignoring sampling uncertainty. Compute the probability that a positive flag in the new archive is a true event. With sensitivity held fixed, find the largest false-positive rate that would permit a positive predictive value of at least 50% in that archive.

### Q772

**When the reference is available only for a whole field**

Four archived fields each contain three passive microrobots. An independent reference indicates whether at least one robot in a field showed a transition. The labels are positive, positive, negative, negative. A tracker flags one robot in each of the first two fields and none in the others. A reviewer calls this perfect individual-robot localization. Assuming the field references are correct, construct an individual-level assignment in which all flagged robots are correct and another in which none is correct. Give the sharp bounds on flag precision and identify a reference that would test localization.

### Q773

**An unresolved reference panel can change the winner**

Two classifiers assign binary reporter states to the same archived microrobot tracks. Among tracks with settled reference labels, A is correct and B is wrong on seven, while B is correct and A is wrong on two. All other settled tracks are ties. On six further tracks the classifiers disagree and the reference panel has not resolved the label. Find the sharp range of the difference in total correct classifications, A minus B. Does A necessarily win? Determine how many of the six must be confirmed for A to guarantee a strict overall win even if every other unresolved label favors B.

### Q774

**Can two optical readers jointly suppress false alarms?**

On 100 reference-negative microrobot clips, fluorescence reader F false-alarms on 12 and motion reader M false-alarms on 10. A combined alert requires both readers to alarm on the same clip. Their individual clip IDs have been stripped from the public table. A report multiplies the rates to claim a combined false-alert rate below 2%. Derive sharp bounds from the marginal counts, assess the independence calculation, and decide exactly what overlap would satisfy the strict 2% criterion. Specify the minimum additional archived statistic needed to settle that claim.

### Q775

**A mechanism claim based on a fading reporter**

Two analyses of the same archived microrobot imaging run agree that fluorescence outlasts the recorded input. One calls this evidence for a retained internal state. The other predicts ordinary reporter decay with no retained state. After normalization to 1.00 at input offset, the observed values at the next two intervals are 0.60 and 0.36. An independent passive reference predicts 0.60 and 0.36 from decay alone, each within 0.03. A retained-state model can also fit those measurements. Judge which claim the paired analyses support. State what pattern in an additional archived trace would reject this specific decay-only prediction and what inference would still remain open.

## Decisions and benchmarking

### Q776

**A reader for a different chamber mix**

An archive contains faint and bright reporter images from passive biohybrid microrobots. On 50 independently labeled images per chamber, readers A and B correctly classify 39 and 34 faint images, and 44 and 49 bright images, respectively. A target archive is expected to contain between 60% and 80% faint images. Assume within-chamber accuracies transfer. A team proposes picking a reader by pooled accuracy on the original archive. Evaluate that proposal, give the range of A's target advantage in percentage points, and identify one failure of the transfer assumption that would invalidate the decision.

### Q777

**The review queue changes the winning reader**

A scorer of microrobot membrane-reporter images can refer uncertain images for expert review. In the same 100 images, A makes 6 errors among 80 automatic decisions and refers 20; B makes 9 errors among 94 decisions and refers 6. Reviewers can resolve 8 referrals per 100 without error at a cost of 1 unit each. An unresolved referral costs 4; a wrong automatic decision costs 5. Correct automatic decisions cost zero. Which reader minimizes total loss? Recompute the choice if capacity rises to 20 and state why ranking by automatic accuracy alone fails.

### Q778

**Which biological event did the score count?**

In 20 archived movies of swimming microrobots, 10 movies contain one verified reporter switch each. Two switches remain visible for 40 labeled frames each and eight for 5 frames each. Decoder A detects every frame of the two long switches and none of the short ones. Decoder B detects 4 frames of each switch. Neither decoder signals outside a verified switch window. Detections within a single window are merged into one event. A switch counts as detected if at least one of its frames is detected. Select a decoder for counting switches, compare both frame recalls and event recalls, and say what cannot be concluded about onset timing.

### Q779

**A smaller tracking reader and an equivalence claim**

Two offline readers classify whether each biohybrid track retains a marker, using independent reference labels to measure accuracy. Positive differences favor the smaller reader. A paired study reports a 90% confidence interval of [−1.8, +0.6] percentage points for its difference from the reference. The preregistered accuracy margin for noninferiority is −2 points; equivalence requires the whole interval inside [−1, +1]. The smaller reader uses 40% less storage. A sensitivity analysis retaining low-contrast tracks gives [−2.3, +0.4]. Adjudicate the two accuracy claims under each analysis and explain the role of storage in that decision.

### Q780

**Estimating unseen robot tags from two optical views**

Two cameras index bright and dim tags on passive biohybrid microrobots in the same archived field. In the bright stratum, A lists 30 distinct tags, B lists 24, and 18 identities match across lists. For dim tags the counts are 10, 6, and 2. Both cameras agree on stratum for any matched tag. Within each stratum only, assume homogeneous detection probabilities and independent capture by the cameras. Using the specified estimate N = nA times nB divided by the match count, estimate the total and the number missed by both. Compare with pooling first. Decide what population bound survives if capture independence and homogeneity are both dropped.

### Q781

**Paying for a second readout**

For an archived microrobot encounter, the current evidence assigns a 0.20 probability to a true reporter event. Reporting an event when absent costs 4 units; missing a true event costs 6. A supplementary optical record can be retrieved at cost 0.3 and is positive with probability 0.8 given an event and 0.1 otherwise. Correct decisions cost zero. Decide whether to retrieve the record, giving the best action without it, the best action for each test outcome, and the highest retrieval cost at which the record remains worthwhile.

### Q782

**A one-bit record for a delayed readout**

Choose a readout for a desk review of an archived biohybrid microrobot task. A brief marker exposure, if present, ends between minutes 0 and 4. The only image available for scoring is at minute 14. Card R reports current marker presence and goes dark within two minutes after exposure ends. Card M records a one-bit exposure flag readable in the same image for at least 16 minutes after exposure. At the archived read time, M flagged 45 of 48 exposed controls and 2 of 48 unexposed controls. The task requires at least 90% sensitivity and at most 5% false positives on those controls. Select a card, check the timing and both thresholds, and identify which details of exposure history the selected interface cannot recover.

### Q783

**A relabeling audit that samples unequal fractions**

An archive has 400 short tracks and 100 long tracks of passive biohybrid markers. The original labels give 340 and 60 correct decisions for reader A. An auditor samples 20 tracks uniformly within each length group. For short tracks the review changes two apparent errors to correct calls and one apparent correct call to an error. For long tracks it changes one error to correct and five correct to errors. Estimate corrected archive accuracy using the audit as a stratified correction. Explain why applying the pooled audit correction is inappropriate and identify a source of uncertainty.

### Q784

**When zero detected failures is enough for a release gate**

A release audit checks for a track identity swap affecting the optical reporter label in a complete microrobot movie. In each of 50 independently sampled movies the audit detects no swap. The verifier detects a true movie-level failure with probability 0.80 and never flags a failure-free movie; detections are independent across movies. Each movie has 40 frames, but the target is the fraction p of movies with any failure. Use a one-sided exact 95% upper bound obtained by setting the probability of zero detected failures to 0.05. Does the record certify p below 5% by that rule? How many further independent, detection-free movies would first permit certification? Justify the unit of replication and one assumption needed to extend the audit.

### Q785

**Reviewer agreement hides an asymmetric error**

Two experts label archived frames for a brief reporter flash. Their 2×2 table has both positive 8, first-only positive 2, second-only positive 10, and both negative 80. Only the 12 disagreements receive independent adjudication: both first-only positives are confirmed and two second-only positives are confirmed. Compare raw agreement with each expert's adjudicated performance on disputed frames. A reviewer claims the first expert was 96% accurate overall. Give the tightest range consistent with the data and explain the missing information.

### Q786

**Comparing confidence without access to individual images**

On the same 100 archived reporter events, each of two classifiers produces only two probability values for the positive state. A assigns 0.2 to 50 images with 10 positives, and 0.8 to 50 with 40 positives. B assigns 0.4 to 50 with 5 positives, and 0.6 to 50 with 45 positives. Compute each classifier's Brier score (mean squared error against 0 or 1) and accuracy at a 0.5 cutoff. A sponsor equates the better cutoff accuracy with better probability estimates. Assess that claim using the observed frequencies.

### Q787

**A reader chosen under an unknown background mix**

A passive microrobot fluorescence archive has clear and turbid backgrounds. Expected loss per 100 clear or turbid clips, respectively, is A (2, 9), B (5, 5), and C (8, 3). The target share of turbid clips could be anywhere from 25% to 75%. For any share, regret is a reader's loss minus the best of the three losses at that same share. Choose the reader with the smallest worst-case regret. Show the endpoint losses and explain whether an interior share could yield a larger regret.

### Q788

**A new label policy changes the leaderboard**

A biohybrid-microrobot movie benchmark originally counted any visible flash as an event. A proposed label policy excludes 8 isolated reflections among the 40 originally positive clips; the other 60 clips remain negative. A detected 32 of the original positives, including all 8 reflections, and flagged 5 original negatives. B detected 28 positives, including 1 reflection, and flagged 3 original negatives. Rebuild both confusion tables under the new policy and rank the readers by F1 before and after. Explain whether this change demonstrates a change in either reader's behavior.

### Q789

**Does combining two readers actually help?**

In 100 binary microrobot state decisions, A and B are both correct on 70, only A on 12, only B on 8, and both wrong on 10. A vendor proposes sending disagreements to an expert, leaving agreements untouched. The expert makes a correct call on a fraction r of disagreements and costs 0.05 loss units per reviewed case. Each wrong final call costs one unit. Derive the break-even r versus always using A. If historical expert accuracy is 85% on a random sample of all cases, is that enough to adopt the policy?

### Q790

**Comparing event readers with incomplete replay windows**

A reference lists 12 reporter events in archived microrobot tracks. For A, 7 detections are confirmed within 3 frames of onset, 3 complete replay windows contain no timely detection, and 2 replays end before the deadline with no detection yet. B has 8 timely detections and 4 confirmed misses on those same events. A logging bug hid whether B succeeded on the two truncated A events. Give the sharp bounds for A's timely recall. Can either reader be declared superior on all 12, or can a paired win/loss table be reconstructed? Specify what evidence is needed for each question.

### Q791

**Attributing a failure to the right layer**

A three-stage microrobot video pipeline uses a locator, event classifier, and report formatter. A final report is correct only if all three stages succeed. On 120 archived events there are 18 locator failures. Among locator successes the classifier fails on 12. Among the remaining cases the formatter fails on 6. Engineers say removing all 18 locator failures must add 18 correct final reports. Calculate current success and the sharp bounds after an ideal locator replacement, assuming previously localized cases are unchanged and that nothing is known about downstream outcomes on the 18 recovered cases. What offline evidence would narrow the range?

### Q792

**Zone-specific reporting after unequal robot recovery**

In an archived enclosed imaging chamber, ten reporter microrobots were assigned to each of zones X and Y and remained in their assigned zone. A desk review must identify any zone where more than half of its original ten robots recorded a marker. Interface P pools all recovered flags and loses zone identity. Interface Z retains each recovered robot's original zone and its binary marker flag. Under Z, four robots were recovered from X, three flagged, and nine from Y, three flagged. Flags on recovered robots are exact. Recovery may depend on marker state. Choose an interface, bound each zone's flagged fraction among its original ten, and state which majority decisions can be defended from this archive.

### Q793

**A preregistered paired test on discordant clips**

Two readers classify reporter flashes in the same 60 microrobot clips. Both are correct on 39, both wrong on 9, only A correct on 10, and only B correct on 2. The registered comparison uses a two-sided exact sign test on discordant clips at 0.05, doubling the smaller binomial tail under equal chances. Determine the outcome treating clips as independent. Then learn that the 12 discordant clips are excerpts from only two source movies. Which numerical findings survive, and what additional information is needed for a valid movie-level comparison?

### Q794

**What external navigation and live optical reporting each establish**

A desktop replay must document at least two marker-positive frames while a biohybrid microrobot occupies a mapped zone. An external navigation log independently places it inside from 1.5 through 3.5 seconds on the position clock. A validated live optical reporter is positive at camera times 2.4, 3.2, and 4.2 seconds. Camera time minus position time is 1.0 second with a bounded error of 0.2 seconds. Count a frame only if its entire possible time interval is inside the zone. An optional endpoint memory card stores whether the marker was ever seen, without time or position. Choose the records needed, decide whether the replay passes, and assess a claim that the biological reporter guided the robot toward the marker.

### Q795

**Ablations with an interaction**

A fixed replay of 100 biohybrid tracks compares two optional processing steps: drift correction and a background mask. The outcome is the number of tracks with a verified trajectory and marker state. With neither step, 54 pass. With drift correction alone, 66 pass. With masking alone, 70 pass. With both, 72 pass. Quantify the interaction on the count-difference scale. A report assigns the entire improvement over baseline to masking. Give a symmetric attribution by averaging each step's increment across the two possible orders, and state what the replay cannot establish about individual tracks.

### Q796

**When a partial-credit winner depends on an essential finding**

Two systems interpret ten independent archived microrobot readout cases. Each case has four binary scoring criteria: correct decision, support from the observed data, identification of an ambiguity, and a valid limit on the claim. System A earns 34 of 40 points and gives the correct decision on 6 cases. B earns 31 points and gives the correct decision on 9. A proposed additional metric gives a case zero credit if the decision is wrong and otherwise keeps its earned points. Derive sharp bounds for each system's gated total and decide whether the two published aggregates suffice to rank them under this metric. What additional aggregate would recover each exact gated total?

### Q797

**Can a stored-state decoder be tested with this reference?**

A microrobot imaging archive contains 50 clips with a verified earlier reporter event and 50 without. At the end of each clip a camera independently measures whether a visible marker remains. The archive includes only two combinations: all 50 event-positive clips have a visible marker, and all 50 event-negative clips lack it. A decoder matches the earlier event label on 97 clips. Assess the claim that it retrieves event history even if the marker is gone. Construct a competing explanation consistent with the 97 scores, specify the missing comparison, and bound accuracy on event-positive clips without a visible marker.

### Q798

**Invariance and responsiveness on matched replays**

For each of 40 microrobot movies, benchmark curators create two offline variants. One changes only the display palette; the other reverses a labeled directional cue and therefore flips the required binary answer. The criterion for a robust movie is that the original answer is correct, the palette answer stays the same, and the cue-reversal answer flips. There are 32 correct original answers. Within those 32, 28 are palette-stable and 23 flip appropriately. The overlap was not saved. Bound the robust count and decide whether a requirement of at least 22 robust movies is established. What cross-count resolves it?

### Q799

**Benchmarking an explicit unknown state**

An image benchmark labels each biohybrid reporter record positive, negative, or genuinely indeterminate. The three groups contain 30, 50, and 20 records. On positives a system predicts positive/negative/unknown = 24/2/4. On negatives it predicts 5/40/5; on indeterminate records it predicts 3/3/14. A report calls every unknown prediction a failure. Compare three metrics: exact agreement across all three labels, accuracy of definite answers on determinate records, and the rate of unsupported definite answers on indeterminate records. Explain which denominators would matter to a reader using this system to review ambiguous records.

### Q800

**A release decision with two different acceptance gates**

A frozen review board evaluates two decoders on the same 80 ordinary and 20 optically ambiguous microrobot clips. On ordinary clips every call is definitive; A makes 5 errors, B makes 2. On ambiguous clips A makes 8 definitive calls with 2 errors and defers the rest; B makes 16 with 5 errors and defers the rest. The board requires at most 30% errors among definitive ambiguous calls. Among passing decoders it minimizes loss at a target mix of 60% ordinary and 40% ambiguous, with a wrong call costing 3, deferral costing 1 and a correct call zero. Compute both gate values and target losses, choose under the rule, and explain how the decision changes if the gate becomes 32%.
