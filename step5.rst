.. include:: cyverse_rst_defined_substitutions.txt
.. include:: custom_urls.txt

|CyVerse_logo|_

|Home_Icon|_
`Learning Center Home <http://learning.cyverse.org/>`_



Using Applications in the Discovery Environment (DE)
----------------------------------------------------

*Applications*, also known as *apps*, are pieces of software that have been configured to run within the Discovery
Environment (DE). When you're ready to analyze your data, you may choose from several hundred pre-defined apps to do
so.

----

Browsing Apps in the Discovery Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can see a listing of existing applications by visiting the |DE Apps View|,
which can be accessed by clicking |DE Apps Navigation Icon| in the navigation
bar on the left-hand side of the DE.

When you first access the Apps view, you may be prompted to log in. After
logging in, you'll be presented with a screen that looks something like this:

|DE App Listing|

*Sorting and Filtering Applications*

You can click on the column headings to sort the app listing in ascending or
descending order by app name, the name of the person who integrated the app, or
average rating. You can also use the controls at the bottom of the Apps view to
choose how many apps to list on a single page and navigate between pages.

Because the DE contains a large number of apps, it can be helpful to reduce the
number of apps that are displayed. The bar just above the app listing provides
two ways to do that. First, the upper left corner of the Apps view contains the
currently active subset of apps to be included in the listing. By default, the
Apps view displays all apps that are available to you. Clicking the arrow next
to the currently active subset allows you to select a different subset of apps
to display:

|DE App Subsets|

The currently selected app subset is highlighted in gray. The app subsets that are available are:


.. list-table::
    :header-rows: 1

    * - Application type
      - Description
    * - Apps under development
      - Apps that you have added to the DE that have not been made public.
    * - Favorite Apps
      - Apps that you have marked as favorite apps in the DE.
    * - My public apps
      - Apps that you have added to the DE that have been made publicly
        available.
    * - Shared with me
      - Apps that other users have shared with you.
    * - High-Performance Computing
      - Apps that run at the Texas Advanced Computing Center using the |TAPIS
        API|.
    * - Browse All Apps
      - All apps available to you within the DE.

The second way to reduce the scope of the app listing is to select a filter in
the upper right corner of the Apps view. Clicking anywhere on the Filter
control allows you to select which type of apps you'd like to see in the
listing:

|DE App Filter|

The currently selected filter is displayed in the Filter control itself. If no filter is selected, the control will be
empty. The currently available app filters are:


.. list-table::
    :header-rows: 1

    * - Application filter
      - Description
    * - Agave
      - Apps that run at the Texas Advanced Computing Center using the |TAPIS
        API| (formerly known as Agave). Choosing this filter is essentially equivalent to selecting the High-Performance Computing app subset.
    * - DE
      - Executable (non-interactive apps) that run on CyVerse computing
        resources.
    * - Interactive
      - Interactive apps (e.g. Jupyter, RStudio, R Shiny) and other apps with
        their own interactive interfaces.
    * - OSG
      - Executable (non-interactive apps) that run on Open Science Grid (OSG)
        resources.


Once you've selected an app filter, it will be displayed in the Filter control:

|DE Selected App Filter|

The selected filter will stay in place until you select a new filter or dismiss
the current filter by clicking the `X` just to the right of the filter name.
Note that the `X` is only present when the mouse cursor is hovering over the
Filter control.

Viewing App Details in the Discovery Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you've found an app of interest, you can select it by clicking the check
box in the row containing the app name. If exactly one app is selected, a
*Details* button will appear in the upper right corner of the apps view, just
to the right of the Filter control.

|DE App Details Button|

Clicking the Details button produces a slide-out panel containing additional
information about the app (e.g. description, number of times run, etc.).

|DE App Details|

This screen has several controls available. The Heart icon just to the right of
the app name allows you to add the app to or remove it from your list of
favorite apps. The heart will be filled in if the app is currently in your list
of favorites. The Link icon will display a link to the app that you can copy
and share with other DE users. The stars icons labeled, :guilabel:`Your
rating`, allow you to give the app a rating. The :guilabel:`Tools used by this
App` tab contains information about the steps that the app takes to perform an
analysis. You can dismiss the app details panel by clicking anywhere outside
the panel.

 ..  tip::

     Favorite your frequently used applications to make it easier to find them.

----

**Fix or improve this documentation**

- Search for an answer:
  |CyVerse Learning Center|
- Ask us for help:
  click |Intercom| on the lower right-hand side of the page
- Report an issue or submit a change:
  |Github Repo Link|
- Send feedback: `learning@CyVerse.org <learning@CyVerse.org>`_
