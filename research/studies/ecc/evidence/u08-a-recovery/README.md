# U08-A interrupted-publication recovery

Status: RECOVERY IN PROGRESS, not completed U08-A research. Date: 2026-09-18.

The previous turn created two Git blob objects but did not link them into a published research tree. This recovery commit preserves those exact object identities without rewriting their bytes. The original local E06 files are not present in this turn's active /mnt/data; this is an availability observation, not proof of permanent loss.

Objects:
- 9c36feb87bdedbbbd51a2a7126f81b51ce6b3e8c
- 4b6af43bcce99fceb6be677f4239c14cb6d7b660

Both text-oriented blob reads failed with a UTF-8 decode error at byte 0x8b. Contents, decompression integrity and correspondence to the historical experiment are NOT YET VERIFIED. They are quarantined evidence objects, not authoritative findings or executable inputs. Nothing from these objects is to be executed during recovery.

Next recovery step: fetch the attached paths with encoding=base64; decode locally; verify Git object identities; inspect compressed contents and any internal manifest; then publish a readable recovery result and coherent STATE. Do not rerun the experiment or start a new research unit to replace missing publication evidence. Existing U07-A and historical E05 records remain unchanged.
