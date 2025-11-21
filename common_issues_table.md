# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                   Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :---------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   | [TSV_ADDITIONAL_COLUMNS_UNDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L30) |          10030           |              31759              |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L17)      |           1789           |              5286               |
|   ERROR    |       [REQUIRED_COORDSYSTEM](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L99)       |           721            |              2370               |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)        |           1710           |              1260               |
|   ERROR    |        [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///000070/blob/draft/derivatives/validations/bids_validation.txt#L42)        |           834            |               903               |
|  WARNING   |          [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           621            |               620               |
|  WARNING   |        [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///000070/blob/draft/derivatives/validations/bids_validation.txt#L17)         |           414            |               542               |
|   ERROR    |          [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///000070/blob/draft/derivatives/validations/bids_validation.txt#L37)          |           414            |               477               |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L17)  |            39            |               352               |
|  WARNING   |            [NO_AUTHORS](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/bids_validation.txt#L31)            |           267            |               267               |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/bids_validation.txt#L41)         |           259            |               259               |
|   ERROR    |   [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000018/blob/draft/derivatives/validations/bids_validation.txt#L23)   |           251            |               249               |
|   ERROR    |     [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L78)     |           1026           |               212               |
|   ERROR    |    [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L73)    |            49            |               49                |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L66)      |            25            |               21                |
|   ERROR    |     [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L37)     |           163            |                1                |
|  WARNING   |        [EMPTY_DATASET_NAME](https://github.com/bids-dandisets///000724/blob/draft/derivatives/validations/bids_validation.txt#L7)         |            1             |                1                |
|   ERROR    |       [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L91)       |          12413           |                0                |
|   ERROR    |           [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L35)           |          21976           |                0                |
|   ERROR    |    [MISSING_DATASET_DESCRIPTION](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L1)    |            9             |                0                |


## `nwb2bids` Notifications

|            Severity            |                                                                                Title                                                                                 |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|    STYLE_SUGGESTION (ERROR)    |                [Invalid session ID](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1431)                 |          34696           |              43236              |
|    STYLE_SUGGESTION (ERROR)    |               [Invalid participant ID](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L43)                |          26386           |              34927              |
|  SCHEMA_INVALIDATION (ERROR)   |                  [Invalid species](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1417)                  |           2831           |              2831               |
| SCHEMA_INVALIDATION (CRITICAL) |               [Missing participant sex](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)                |           1170           |              1170               |
|    STYLE_SUGGESTION (ERROR)    |          [Invalid participant sex (BIDS)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L4470)           |           496            |               407               |
|    STYLE_SUGGESTION (ERROR)    |        [Invalid participant sex (archives)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L7035)         |           346            |               345               |
|     INTERNAL_ERROR (ERROR)     |  [Failed to initialize converter on remote Dandiset](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)   |           255            |               254               |
|     INTERNAL_ERROR (INFO)      |           [INFO: invalid Dandiset metadata](https://github.com/bids-dandisets///000005/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)            |           142            |               137               |
|     INTERNAL_ERROR (ERROR)     |          [Failed to convert to BIDS dataset](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)           |           104            |               94                |
|     INTERNAL_ERROR (ERROR)     | [Failed to extract metadata for one or more sessions](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15) |            99            |               94                |
|     INTERNAL_ERROR (ERROR)     |               [Dandiset is already BIDS](https://github.com/bids-dandisets///000026/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)               |            24            |               22                |
| SCHEMA_INVALIDATION (WARNING)  |      [WARNING: multiple licenses not supported](https://github.com/bids-dandisets///000156/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)       |            4             |                4                |
| SCHEMA_INVALIDATION (CRITICAL) |             [Missing participant species](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)             |            4             |                4                |