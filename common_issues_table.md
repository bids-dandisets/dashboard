# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L26)     |           1068           |                0                |
|   ERROR    |            [HED_ERROR](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L39)            |            28            |                0                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L45)       |          15142           |                0                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)           |          31829           |                0                |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000018/blob/draft/derivatives/validations/bids_validation.txt#L19)   |           236            |                0                |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L13)     |            1             |                0                |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)        |           382            |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           162            |                0                |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)       |           1517           |                0                |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           2152           |                0                |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           627            |                0                |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)            |           382            |                0                |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13) |            68            |                0                |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000488/blob/draft/derivatives/validations/bids_validation.txt#L26)    |           308            |                0                |


## `nwb2bids` Notifications

|            Severity            |                                                                                Title                                                                                 |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|    STYLE_SUGGESTION (ERROR)    |                [Invalid session ID](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1431)                 |          38663           |              43754              |
|    STYLE_SUGGESTION (ERROR)    |               [Invalid participant ID](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L43)                |          29926           |              35017              |
|  SCHEMA_INVALIDATION (ERROR)   |                  [Invalid species](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1417)                  |           2831           |              2831               |
| SCHEMA_INVALIDATION (CRITICAL) |               [Missing participant sex](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)                |           1170           |              1170               |
|    STYLE_SUGGESTION (INFO)     |                [Missing description](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3384)                |           754            |               754               |
|    STYLE_SUGGESTION (ERROR)    |          [Invalid participant sex (BIDS)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L4470)           |           496            |               496               |
|    STYLE_SUGGESTION (ERROR)    |        [Invalid participant sex (archives)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L7035)         |           346            |               346               |
|     INTERNAL_ERROR (ERROR)     |  [Failed to initialize converter on remote Dandiset](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)   |           262            |               262               |
|     INTERNAL_ERROR (INFO)      |           [INFO: invalid Dandiset metadata](https://github.com/bids-dandisets///000005/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)            |           140            |               140               |
|     INTERNAL_ERROR (ERROR)     |          [Failed to convert to BIDS dataset](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)           |            99            |               98                |
|     INTERNAL_ERROR (ERROR)     | [Failed to extract metadata for one or more sessions](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15) |            99            |               98                |
|     INTERNAL_ERROR (ERROR)     |               [Dandiset is already BIDS](https://github.com/bids-dandisets///000026/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)               |            24            |               24                |
| SCHEMA_INVALIDATION (CRITICAL) |             [Missing participant species](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)             |            4             |                4                |
| SCHEMA_INVALIDATION (WARNING)  |      [WARNING: multiple licenses not supported](https://github.com/bids-dandisets///000156/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)       |            4             |                4                |