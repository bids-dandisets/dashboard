# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)     |          40974           |             160126              |
|   ERROR    |      [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000039/blob/draft/derivatives/validations/bids_validation.txt#L96)       |           3039           |              48357              |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L70)    |          23379           |              34782              |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L124)  |           6724           |              9185               |
|   ERROR    |       [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L141)       |           3929           |              4476               |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)       |           234            |               232               |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L103)    |           207            |               179               |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L46) |            39            |               118               |
|  WARNING   |    [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L96)    |            0             |               110               |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           100            |               100               |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L25)            |            42            |               41                |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L35)        |            42            |               41                |
|   ERROR    |     [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///000473/basic_sanitization/derivatives/validations/bids_validation.txt#L100)     |            0             |               25                |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L93)     |            1             |                1                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L116)      |           3612           |                0                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)           |          12047           |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           244            |                0                |


## `nwb2bids` Notifications

