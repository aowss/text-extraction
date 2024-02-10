Feature: Extracting text

  Scenario Outline: extracting data from a proof of sustainability
    Given this proof of sustainability: <file_name>
    When the extraction is run
    Then the following data is extracted
      | grade   | trade number |
      | <grade> | <trade_id>   |

    Examples:
      | file_name          | framework | grade | trade_id |
      | PoS_EU_Vers1.1.pdf | textract  | G1    | U12345   |