# Specification for the Development of an MMORPG Fan Server Website

## 1. General Provisions
   - Project Name: <b>mmocom</b>
   - Project Objective: To create a web resource functioning as a bulletin board for an MMORPG fan server.

## 2. Functional Requirements
   1. **User Registration and Authentication**
      - Ability to register via e-mail.
      - Sending an e-mail with a confirmation code for registration.
      - Account protection with a password.

   2. **Creation and Editing of Advertisements**
      - Capability to create ads with a title and text.
      - Inserting images, embedded videos, and other multimedia content into the text.
      - Editing and deleting one's own advertisements.

   3. **Advertisement Categorization**
      - Mandatory categorization of an advertisement into one of the provided categories (Tanks, Healers, DPS, Traders, etc.).

   4. **Interaction with Advertisements**
      - Ability to respond to other users' ads.
      - Receiving e-mail notifications for new responses.
      - Private page for viewing responses to one's ads.
      - Functionality for filtering, deleting, and accepting responses.

   5. **Notifications and Responses to Replies**
      - Email notification to the user when their response to an ad is accepted.

   6. **Newsletters**
      - Option to subscribe to newsletters.
      - Regular news updates via e-mail to subscribed users.

## 3. Technical Requirements
   - Suggested Technology Stack: [HTTP5, CSS, Django, PostgreSQL].
   - Compatibility with major browsers.
   - Mobile device support.

## 4. Acceptance Criteria
   - List of criteria and tests to evaluate the project's readiness.
   - **Model Design Accuracy**: Correctly designed models, no errors in relationships, no redundant models or fields — 3 points.
   - **View Implementation**: Views written in accordance with the logic of the specification, models used effectively — 5 points.
   - **Authorization and Registration Functionality**: Registration and authorization working correctly, confirmation code sent to e-mail — 3 points.
   - **Email Notification Logic**: Emails sent for the correct events — 5 points.