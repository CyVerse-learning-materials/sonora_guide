.. include:: cyverse_rst_defined_substitutions.txt
.. include:: custom_urls.txt

|CyVerse_logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_



Manage Data in the Discovery Environment
----------------------------------------

To manage data in the Discovery Environment, begin by clicking on the Data icon
|Data Icon| in the sidebar. You may be prompted to log in. Once logged in, you
should be shown your own home directory, in order with folders first, then
alphabetically.

|Data Window|

Browsing Data in the Discovery Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. To see more information, press the :guilabel:`&Customize Columns` button to
show more columns in the display, such as size or modification date.

2. If the folder you're viewing has many items in it, the bottom of the screen
provides a way to change between pages and set the number of items displayed per page.

3. Click on the name of a subfolder to open that folder. Near the top of the
screen, you should see breadcrumbs that indicate the folder you're viewing and its parent folders.

4. From the top left, at the start of the breadcrumbs, you may select another
root folder to view from among your home folder, "Shared With Me", "Community Data", and Trash.

Discovery Environment File and Folder Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. Click the checkbox next to a file or folder to select it.

2. With an item selected, there will be a button near the top right labeled :guilabel:`&Details`. Alternatively, click the three-dots menu to the right edge in a file or folder's row, and click the :guilabel:`&Details` button there to see specific information about the selected item, to copy the path to the item, to add tags to the item, or to set a file's info type.

3. Click "Permissions" to see your own permissions on the item, and those of
other users.


The Discovery Environment allows you to access, view, and manage your files in the CyVerse Data Store. You can upload smaller files, but for large files or large number of files, we recommend faster methods such as Cyberduck or iCommands. See documentation for those tools in our |Data Store Guide|.


*Upload / import small files in the Sonora Discovery Environment*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In the navigation menu, click the **Data** button |Data Icon| to access the data window in the Discovery Environment.

2. In the data window you will see a directory of files and folders in your Data Store. You may select a folder to be the destination for your uploaded file(s). You may also click the **Folder** button to create a new folder. If you do not select a destination, files will be uploaded to your home Data Store folder (i.e. iplant/home/CYVERSE_USERNAME)

3. Click the **Upload** button |upload button| to choose your options for importing files into the Discovery Environment:

    - To upload files from your local computer choose **Browse Local**;
      a file browser will open and you may select up to XXX files to upload
      (XXX MB Max)

    - To upload files available at a URL choose **Import by URL**;
      You may paste in a valid HTTP or FTP url. Then press **Import**. You may paste additional URLs or close this window by clicking **Done**.

  .. tip::

    When your data store file browser is open, you can also upload files from your computer by dragging them onto your browser window.

    |upload drag|


4. Once you have begun the upload, you will get a notification that files have been queued for upload. You may also view the status of an upload or import
by going back to the **Upload** button and choosing **View Upload Queue**.

   |upload queue|

   .. note::

     The queue will only display the status of uploads from local files. Files imported by URL will generate a message in your notifications (bell icon, upper-left) when they have completed or if they fail.

----

*Share data with another CyVerse user*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. If necessary, log in to the |discovery environment|.

2. Open the **Data** view by clicking on |Data_icon|

3. Select the data resources you wish to share with another user; then click the Share button.

4. In the Sharing dialog that opens, ensure that the resources you wish to share are shown.

   |Data_sharing|

5. In the search field, search for the CyVerse user you wish to share with by searching for their CyVerse username or email address.

6. Next, under "Permission", choose which permission you want to grant the person you are sharing these resources with.

7. Once you are finished, click Done to begin sharing. The user(s) will be notified that resources have been shared with them.

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
<<<<<<< HEAD
- Send feedback: `learning@CyVerse.org <learning@CyVerse.org>`_
=======
- Send feedback: `learning@CyVerse.org <learning@CyVerse.org>`_
