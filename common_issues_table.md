# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |              Title              |                                             Count<br>(Unsanitized)                                             |                                                Count<br>(Basic sanitization)                                                 |
| :--------: | :-----------------------------: | :------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: |
|  WARNING   |     SIDECAR_KEY_RECOMMENDED     | [82110](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L46)  | [334879](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L13)  |
|   ERROR    |      SIDECAR_KEY_REQUIRED       | [14187](https://github.com/bids-dandisets//000039/blob/draft/derivatives/validations/bids_validation.txt#L96)  | [109917](https://github.com/bids-dandisets//000016/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L105) |
|  WARNING   |    TSV_COLUMN_TYPE_REDEFINED    | [39839](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L13)  |  [66366](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L70)  |
|   ERROR    |   TSV_INDEX_VALUE_NOT_UNIQUE    | [3584](https://github.com/bids-dandisets//000638/blob/draft/derivatives/validations/bids_validation.txt#L124)  | [13334](https://github.com/bids-dandisets//000638/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L116)  |
|   ERROR    |       TSV_COLUMN_MISSING        |  [632](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L150)  |  [814](https://github.com/bids-dandisets//000473/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L114)   |
|  WARNING   |      JSON_KEY_RECOMMENDED       |   [728](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L1)   |   [725](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L1)    |
|   ERROR    |    TSV_VALUE_INCORRECT_TYPE     | [1225](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L103)  |  [642](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L103)   |
|  WARNING   |        EVENT_ONSET_ORDER        |  [316](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L35)   |   [436](https://github.com/bids-dandisets//000016/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L96)   |
|   ERROR    |         TSV_EQUAL_ROWS          |  [316](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L134)  |  [407](https://github.com/bids-dandisets//000473/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L106)   |
|   ERROR    |  JSON_SCHEMA_VALIDATION_ERROR   |  [384](https://github.com/bids-dandisets//000025/blob/draft/derivatives/validations/bids_validation.txt#L13)   |   [384](https://github.com/bids-dandisets//000025/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L53)   |
|  WARNING   |         SUBJECT_FOLDERS         |   [371](https://github.com/bids-dandisets//000004/blob/draft/derivatives/validations/bids_validation.txt#L1)   |   [369](https://github.com/bids-dandisets//000004/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L1)    |
|  WARNING   |           NO_AUTHORS            |  [118](https://github.com/bids-dandisets//000019/blob/draft/derivatives/validations/bids_validation.txt#L25)   |   [117](https://github.com/bids-dandisets//000019/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L25)   |
|   ERROR    |        JSON_KEY_REQUIRED        |  [118](https://github.com/bids-dandisets//000019/blob/draft/derivatives/validations/bids_validation.txt#L35)   |  [117](https://github.com/bids-dandisets//000019/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L101)   |
|  WARNING   | SUSPICIOUS_POSITIVE_EVENT_ONSET |   [39](https://github.com/bids-dandisets//000061/blob/draft/derivatives/validations/bids_validation.txt#L13)   |   [39](https://github.com/bids-dandisets//000061/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L13)    |
|   ERROR    |     PARTICIPANT_ID_MISMATCH     |   [1](https://github.com/bids-dandisets//000020/blob/draft/derivatives/validations/bids_validation.txt#L93)    |    [1](https://github.com/bids-dandisets//000020/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L93)    |
|   ERROR    |      INVALID_ENTITY_LABEL       | [20657](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L116) |                                                              0                                                               |
|   ERROR    |          NOT_INCLUDED           | [35921](https://github.com/bids-dandisets//000008/blob/draft/derivatives/validations/bids_validation.txt#L19)  |                                                              0                                                               |
|   ERROR    |    SIDECAR_WITHOUT_DATAFILE     |  [346](https://github.com/bids-dandisets//000043/blob/draft/derivatives/validations/bids_validation.txt#L33)   |                                                              0                                                               |


## `nwb2bids` Notifications

