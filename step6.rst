.. include:: cyverse_rst_defined_substitutions.txt
.. include:: custom_urls.txt

|CyVerse_logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_



Manage Analysis Status and History in Sonora Discovery Environment
--------------------------------------------------------------------

The Discovery Environment maintains a detailed history of jobs you have previously
launched. Using the Analyses view you can see the status of jobs in progress,
cancel analyses, relaunch analyses, and view and save the parameters of previously launched
analyses.

----

*Browse Analyses in the Discovery Environment*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the **Analyses** view by clicking on |analyses icon| on the left side of the Discovery Environment workspace to monitor the status of your submitted analysis.

   .. tip:: By default analyses are sorted by start date and time. The analysis started most recently will appear at the top of the list.

2. To sort your analyses hover over the name of the column you wish to sort by and click on the arrow that appears beside the column name. Analyses can be sorted by name, start date, end date or status.

3. To filter your analyses by user click on the "View" dropdown menu and select either 'only my analyses' or 'analyses shared with me'. The default view is 'all' analyses.

4. To filter your analyses by app type click on the "App Type" dropdown menu and select the type of analyses you would like to see (Agave, DE, interactive or OSG).

5. To open the output folder of a particular analysis click on the output folder icon |output folder icon| at the right side of that analysis.


*Share analyses with another CyVerse user*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. If necessary, log in to the |discovery environment|.

2. Open the **Analyses** view by clicking on |Analyses_icon|

3. Select the analyses you wish to share with another user; then click the Share button.

4. In the Sharing dialog that opens, ensure that the analyses you wish to share are shown.

    |Analyses_sharing|

5. In the search field, search for the CyVerse user you wish to share with by searching for their CyVerse username or email address.

6. Next, under "Permission", choose which permission you want to grant the person you are sharing these analyses with.

7. Once you are finished, click Done to begin sharing. The user(s) will be notified that analyses have been shared with them.

   .. hint::
      Permissions (based on UNIX permissions) are described in this chart:

      .. list-table::
          :header-rows: 1

          * - Permission level
            - Read
            - Download/Save
            - Metadata
            - Rename
            - Move
            - Delete
          * - Read
            - **X**
            - **X**
            - **View**
            -
            -
            -
          * - Write
            - **X**
            - **X**
            - **Add/Edit**
            -
            -
            -
          * - Own
            - **X**
            - **X**
            - **Add/Edit**
            - **X**
            - **X**
            - **X**



----

**Fix or improve this documentation**

- Search for an answer:
  |CyVerse Learning Center|
- Ask us for help:
  click |Intercom| on the lower right-hand side of the page
- Report an issue or submit a change:
  |Github Repo Link|
- Send feedback: `learning@CyVerse.org <learning@CyVerse.org>`_
