# Compute Infrastructure We Use

## Overview

Overall [Infrastructure Chart](https://docs.google.com/spreadsheets/d/1JSOi5pp2Y8Utj_npzKcYmvAxGncgmvP2gait5H0oYKk/edit?usp=sharing) with system specifications and notes.

- [The Ohio Supercomputing Center (OSC)](https://www.osc.edu/): Large compute resource accessible through `ssh` or OnDemand (web) platform.
    - [Globus Endpoint](https://www.globus.org/) — this is the preferred transfer method for collaborations, especially for large data.
    - OnDemand page: [info](https://www.osc.edu/resources/online_portals/ondemand), [login]( https://ondemand.osc.edu)
    - myOSC client portal: [info](https://www.osc.edu/supercomputing/portals/client_portal), [login](https://my.osc.edu/acprod/odb_osc/r/osc/portal/login_desktop?clear=101)
- Imageomics dedicated GPU server: _Internal_ server, hosts our CVAT instance.
    - [Usage and access guide (_internal_)](https://github.com/Imageomics/internal-guidelines/wiki/Imageomics-GPU-Server)
    - [CVAT user guide](https://github.com/Imageomics/kabr-tools/wiki/CVAT-User-Guide)
- NSF ACCESS Accelerate Allocation: NCSA Delta GPU credits
- [Amazon Web Services (AWS)](https://aws.amazon.com/?nc2=h_lg): Basic to extremely powerful, abundant (though finite) resources, high cost.
    - Used sparingly for urgent deadlines when other compute is not available (generally hasn't been available at those times either, though) or to host projects that cannot be hosted effectively through a Hugging Face Space.
    - [AWS usage guidelines (_internal_)](https://github.com/Imageomics/internal-guidelines/wiki/AWS-@-Imagomics)

## Other Compute Resources We've Used or Considered

- OpenAI Researcher Access Program ([_internal_ info](https://github.com/Imageomics/internal-guidelines/wiki/OpenAI-Researcher-Access-Program))
- NAIRR Pilot Program
