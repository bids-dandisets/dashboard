# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                   Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :---------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|   ERROR    | [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L35) |            0             |               172               |
|  WARNING   | [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L22)  |            0             |               135               |
|  WARNING   |    [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L13)     |            0             |               85                |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L7)        |           2193           |                8                |
|  WARNING   |            [NO_AUTHORS](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L31)            |           731            |                1                |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L41)         |           731            |                1                |
|   ERROR    |        [HED_ERROR](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L50)         |            0             |                1                |
|   ERROR    | [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/basic_sanitization/derivatives/validations/bids_validation.txt#L13)  |            0             |                1                |
|  WARNING   |          [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           731            |                0                |


## `nwb2bids` Notifications

|            Severity            |                                                                                Title                                                                                |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|    STYLE_SUGGESTION (ERROR)    |                [Invalid session ID](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1431)                |          43256           |              43256              |
|    STYLE_SUGGESTION (ERROR)    |               [Invalid participant ID](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L43)               |          34524           |              34524              |
|  SCHEMA_INVALIDATION (ERROR)   |                 [Invalid species](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1417)                  |           2831           |              2831               |
| SCHEMA_INVALIDATION (CRITICAL) |               [Missing participant sex](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)               |           1170           |              1170               |
|    STYLE_SUGGESTION (INFO)     |               [Missing description](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3384)                |           754            |               754               |
|    STYLE_SUGGESTION (ERROR)    |          [Invalid participant sex (BIDS)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L4470)          |           496            |               496               |
|    STYLE_SUGGESTION (ERROR)    |        [Invalid participant sex (archives)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L7035)        |           346            |               346               |
|     INTERNAL_ERROR (ERROR)     |  [Failed to initialize converter on remote Dandiset](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)  |           264            |               264               |
|     INTERNAL_ERROR (INFO)      |           [INFO: invalid Dandiset metadata](https://github.com/bids-dandisets///000005/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)           |           140            |               140               |
|     INTERNAL_ERROR (ERROR)     | [Failed to extract metadata for one or more sessions](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3) |           101            |               101               |
|     INTERNAL_ERROR (ERROR)     |              [Dandiset is already BIDS](https://github.com/bids-dandisets///000026/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)               |            24            |               24                |
| SCHEMA_INVALIDATION (CRITICAL) |            [Missing participant species](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)             |            5             |                5                |
| SCHEMA_INVALIDATION (WARNING)  |      [WARNING: multiple licenses not supported](https://github.com/bids-dandisets///000156/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)      |            4             |                4                |
|     INTERNAL_ERROR (ERROR)     |      [Failed to convert to BIDS dataset](https://github.com/bids-dandisets///000341/basic_sanitization/derivatives/validations/nwb2bids_notifications.json#L3)      |            0             |                1                |