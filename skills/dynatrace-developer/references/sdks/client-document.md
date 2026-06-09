# @dynatrace-sdk/client-document

Source: <https://developer.dynatrace.com/develop/sdks/client-document/v1/> (latest: `client-document/v1`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## client-document/v1

`/develop/sdks/client-document/v1/`

- SDK for TypeScript
- Document
- V1

## Document
This API allows you to create and manage documents, as well as manage access to them.

Have a look at the service documentation to familiarize yourself with its key concepts.

Note, that the document's content isn't inspected by the document-store, therefore it can be entirely schemaless. If your content adheres to a schema, it's your responsibility to enforce that.

Information about authorization can be found here.

### Access Management

There are 2 different permission mechanisms. Most operations involve both mechanisms.

### Endpoint Permissions

IAM permissions (e.g. `document:documents:read`) guard endpoints. If the user doesn't have the permission required by an endpoint, the request gets rejected.

These permissions can not be modified via the doc-store API.

### Document Permissions

These permissions guard individual documents. They are modelled in the service itself, independent of IAM permissions.

They can be modified via the API, e.g. by using the sharing endpoints.

Therefore, a user needs to have access both in the DT IAM layer (by having specific IAM permissions) as well as access to the specific documents (e.g. by being document owner).

### Sharing

By default, documents are only accessible to their owner. There are 3 ways of sharing documents.

Documents can be made public (via the updateDocument operation) by the owner. This immediately grants read access to all users in the environment.

Environment-Shares grant read or read-write access to users of the same environment, but users need to actively claim the share.
The owner effectively loses control over who exactly gains access, as any user can claim the share and therefore receive access.

Direct-Shares immediately grant read or read-write access to specific users and groups. The owner is in total control of who exactly receives access, and can also revoke access retrospectively.

By default, every user with write-access to a document is allowed to re-share it via direct-shares and environment-shares. The owner can disable this by setting the `isReshareable` property to `false` (via the updateDocument operation).

The sharing mechanisms are not mutually exclusive - a document can be shared via multiple sharing mechanisms at the same time.

### Owner Transfer

Document ownership can be changed via the transferDocumentOwner operation.

### Document Locking

### Optimistic Locking

Operations which modify a document generally use mandatory optimistic locking.

When such operations are executed, the user must provide the version upon which they operate.

If the document version in the service doesn't match, because the document has been modified in the meantime, then the operation gets rejected.

### Active Locking

In addition to the mandatory Optimistic Locking, there is optional Active Locking.

Active locking can be optionally utilized to prevent conflicts caused by multiple users concurrently updating the same document.

A user can lock a document to prevent other users from updating the document for some time.

Once the user is done updating the document, they can release the lock and therefore enable updates by other users.

### Deletion and Restoration

Deleted documents are moved to the trash and permanently deleted after 30 days.

The Trash API can be used to manage deleted documents.

Restoring a deleted document makes the document accessible again for the owner as well as all users who had previously received access via shares.

### Snapshots

Document snapshots allow to reset a document's content back to an earlier state.

Snapshots must be explicitly created when updating the document. Multiple snapshots can be created per document.

Restoring a snapshot means that the document's content gets changed to the state it had when the snapshot was originally created. It doesn't change access-related data like the document's shares or ownership.

Snapshot creation is rate-limited to 5 snapshots per 60 seconds per document.

The maximum amount of snapshots per document is 50. Additional snapshots result in the deletion of the oldest existing snapshot.

All snapshots get automatically deleted after 30 days.

### Snapshot Permissions

All users with read access to a document may read its snapshots.

All users with write access to a document may create snapshots of it.

Only the owner may restore or delete a snapshot.

### Labels

Labels allow the user to organize and search their documents.

Labels are optional, a document may have zero or more. The maximum number of labels per document is 25 and the maximum length of each label is 80 characters.

### Document Identity

Each document is assigned a unique and immutable identifier (id) at the time of creation.

This identifier may be supplied by the user. If the user doesn't provide one, the system will generate it automatically.

Regardless of its origin, the identifier is guaranteed to be unique across all documents and is immutable.

### Admin Access

Regular users can only access documents owned by them or shared with them.

Users with the permission `document:documents:admin` can act with elevated permission - they can access all users' documents of the current environment, regardless of ownership.

The admin-access can be enabled on a per-request basis, by setting the optional request parameter `admin-access` to `true.`

### User Data

No user data like names or email addresses are stored. Instead, SSO ids are persisted.

Every user's last access to every document gets stored to allow ordering of results so that least recently accessed documents appear first.

### System-owned Documents

Some documents are created and maintained by the system itself, instead of being user-owned.

### Ready-made Documents

Apps can contain documents which automatically become available to all users of the environment when the app gets installed or updated.
The property `originAppId` indicates app ownership.

### Extension-shipped Documents

Extensions can contain documents which automatically become available to all users of the environment when the extension gets installed or updated.
The property `originExtensionId` indicates extension ownership.

 @dynatrace-sdk/client-document v1.31.0 

`tsx
npm install @dynatrace-sdk/client-document
`

### directSharesClient

`tsx
import { directSharesClient } from '@dynatrace-sdk/client-document';
`

#### addDirectShareRecipients

directSharesClient.addDirectShareRecipients(config): PromiseAdd recipients to a direct-share.Required scope: document:direct-shares:writeAdd one or multiple SSO-users and/or SSO-groups to this share. The affected users immediately gain access to the document.You can only add recipients to shares which are accessible to you. Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access.
The maximum number of recipients is 1000.The validity of the SSO-users and SSO-groups isn't verified. It's technically possible, albeit pointless, to add non-existing users and groups.Already added users or groups are ignored.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.body*required | AddDirectShareRecipients |
 | config.id*required | string | System-generated id of a share.
 | config.sendNotification | boolean | Indicates whether a notification shall be sent to share recipients or new document owners.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | The recipients have been added.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | ShareNotFound | Share not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.addDirectShareRecipients({ id: "...", body: { recipients: [ { id: "441664f0-23c9-40ef-b344-18c02c23d789", type: "group", }, ], }, });
`

#### createDirectShare

directSharesClient.createDirectShare(config): PromiseDirectShare>Create a direct-share.Required scope: document:direct-shares:writeCreate a direct-share for a document. This is only possible for documents you own, as well as for reshareable documents owned by other users to which you have write access. The share can be used to grant access to a specific set of users and/or groups, via addRecipients.You can optionally add users and/or groups which will directly be registered as recipients of the share. The users and groups are specified via their sso-ids. The maximum number of recipients is 1000.The validity of the SSO-users and SSO-groups isn't verified. It's technically possible, albeit pointless, to add non-existing users and groups.The share can be created with either `read` or `read-write` access.A document can have maximally one direct-share per access type, therefore it's impossible to create multiple `read`-shares or multiple `read-write`-shares for a single document.This means, that you can create one `read`-share for a document, and this single `read`-share can be used to give read-access to an arbitrary number of users (and/or groups). The same applies to a `read-write`-share.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.body*required | CreateDirectShare |
 | config.sendNotification | boolean | Indicates whether a notification shall be sent to share recipients or new document owners.

##### Returns
 |
 | Return type | Status code | Description
 | DirectShare | 201 | A new share for the specified document has been created.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | DocumentNotFound | Document not found.
 | ShareAlreadyExists | Share creation failed - a share with the specified permission already exists for the document.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.createDirectShare({ body: { documentId: "...", access: "...", recipients: [ { id: "441664f0-23c9-40ef-b344-18c02c23d789", type: "group", }, ], },});
`

#### deleteDirectShare

directSharesClient.deleteDirectShare(config): PromiseDelete a direct-share.Required scope: document:direct-shares:deleteDelete the share. This will not delete the share's document.You can only delete shares which are accessible to you. Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access.This operation effectively revokes the access of all the share's recipients.Be aware that deleting a share doesn't necessarily prevent a user from accessing a document, as the user might still have access via another share (of the same document). E.g., if a user has 'read' and 'read-write' access (via one 'read' and another 'read-write' share), and the 'read' share gets deleted, access is still granted to the user via the other 'read-write' share.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.id*required | string | System-generated id of a share.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | The share has been deleted.

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | ShareNotFound | Share not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.deleteDirectShare({ id: "...",});
`

#### getDirectShare

directSharesClient.getDirectShare(config): PromiseDirectShare>Retrieve a direct-share.Required scope: document:direct-shares:readRetrieve a direct-share via its id.
The share must be accessible to you. Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.id*required | string | System-generated id of a share.

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | ShareNotFound | Share not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.getDirectShare({ id: "...",});
`

#### getDirectShareRecipients

directSharesClient.getDirectShareRecipients(config): PromiseDirectShareRecipientList>List the recipients of a direct-share.Required scope: document:direct-shares:readRetrieve a share's recipients. If there are groups among the recipients, the groups always appear before the users.You can only retrieve the recipients for shares which are accessible to you. Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.id*required | string | System-generated id of a share.
 | config.page | number | The page parameter is used to directly access a specific page. The value of the page parameter, if specified, has to be a value greater than zero. If the value of the page parameter exceeds the highest available page on the backend, an empty page is returned.
 | config.pageKey | string | The page key is used to query results from the next page. You get a `nextPageKey` parameter in the return value of this method to use here. If this parameter is omitted, the first page will be returned.
 | config.pageSize | number | The page size which defines the requested number of result entries. You can request a maximum of 1000 result entries. If this parameter is omitted, the default value of 20 will be used.

##### Throws
 |
 | Error Type | Error Message
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | ShareNotFound | Share not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.getDirectShareRecipients({ id: "...", });
`

#### listDirectShares

directSharesClient.listDirectShares(config): PromiseDirectShareList>List all direct-shares accessible to you.Required scope: document:direct-shares:readList all direct-shares accessible to you.
Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access. If you are only concerned with a specific document's shares, or a specific share, you can use the `filter` parameter to narrow down the result set. If you attempt to retrieve shares which are not accessible to you the result set will be empty.Note, that at the moment we offer a naive pagination, and therefore interim mutations can lead to result inconsistencies (such as duplicates, missing entries).

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.filter | string | The filter query, as explained here. Filtering is only possible on the `documentId` property, and only with the equals operator. Via this you can effectively retrieve the direct-shares of a specific document. If this parameter is omitted, all direct-shares accessible to you will be returned.
 | config.page | number | The page parameter is used to directly access a specific page. The value of the page parameter, if specified, has to be a value greater than zero. If the value of the page parameter exceeds the highest available page on the backend, an empty page is returned.
 | config.pageKey | string | The page key is used to query results from the next page. You get a `nextPageKey` parameter in the return value of this method to use here. If this parameter is omitted, the first page will be returned.
 | config.pageSize | number | The page size which defines the requested number of result entries. You can request a maximum of 1000 result entries. If this parameter is omitted, the default value of 20 will be used.

##### Returns
 |
 | Return type | Status code | Description
 | DirectShareList | 200 | A list of direct-shares accessible to you.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.listDirectShares();
`

#### removeDirectShareRecipients

directSharesClient.removeDirectShareRecipients(config): PromiseRemove recipients from a share.Required scope: document:direct-shares:writeRemove one or multiple recipients from the share. The affected users immediately lose access to the document.You can only remove recipients from shares which are accessible to you. Shares accessible to you include those of your own documents, as well as those of reshareable documents owned by other users to which you have write access.
The maximum number of recipients is 1000.Non-existing users or groups are ignored.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.body*required | RemoveDirectShareRecipients |
 | config.id*required | string | System-generated id of a share.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | The recipients have been removed.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | ShareNotFound | Share not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { directSharesClient } from "@dynatrace-sdk/client-document";const data = await directSharesClient.removeDirectShareRecipients({ id: "...", body: { ids: ["..."] }, });
`

### documentLockingClient

`tsx
import { documentLockingClient } from '@dynatrace-sdk/client-document';
`

#### acquireLock

documentLockingClient.acquireLock(config): PromiseAcquireLockResult>Acquire the lock on the document.Required scope: document:documents:writeAcquire the lock on the document. A user can lock a maximum of five documents at any given time. Once the lock is acquired by the user, other users cannot make any updates to the document.The user acquiring the lock can optionally specify the duration for which the lock can be attained. However, the specified duration must not exceed the maximum allowed duration of 15 minutes. If not specified, the lock is acquired for 10 minutes.If the user who has currently locked the document attempts to acquire the lock for the same document again, the duration of the lock gets extended by the specified duration or by a default duration of 10 minutes, if not specified.The other users would not be allowed to acquire the lock on an already locked document.

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | AcquireLock |
 | config.id*required | string | System-generated or user-given id of a document.

##### Returns
 |
 | Return type | Status code | Description
 | AcquireLockResult | 200 | The lock has been acquired by the user.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | DocumentNotFound | Document not found.
 | DocumentAlreadyLocked | Lock acquisition failed as the document is already locked.
 | LockedDocumentsLimitReached | Lock acquisition failed as number of locked documents reached or exceeded the allowed limit.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { documentLockingClient } from "@dynatrace-sdk/client-document";const data = await documentLockingClient.acquireLock({ id: "...", body: { documentVersion: 10 },});
`

#### inspectLock

documentLockingClient.inspectLock(config): PromiseDocumentLockDetails>Inspect whether the document is locked.Required scope: document:documents:readInspect whether the document is locked.This provides the information about whether the document is locked and the user that currently owns the lock.

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | System-generated or user-given id of a document.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | DocumentNotFound | Document not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { documentLockingClient } from "@dynatrace-sdk/client-document";const data = await documentLockingClient.inspectLock({ id: "...",});
`

#### releaseLock

documentLockingClient.releaseLock(config): PromiseRelease the lock on the document.Required scope: document:documents:writeRelease the lock on the document.
The lock on the document can be released only by the user who owns it.

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | System-generated or user-given id of a document.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | The lock on the document has been released.

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
 | DocumentNotFound | Document not found.
 | InternalServerError | There is a problem in the backend.
 | ServiceUnavailable | There is a temporary problem in the backend.
 | GeneralError | Unexpected error.Code example
`tsx
import { documentLockingClient } from "@dynatrace-sdk/client-document";const data = await documentLockingClient.releaseLock({ id: "...",});
`

### documentsClient

`tsx
import { documentsClient } from '@dynatrace-sdk/client-document';
`

#### bulkDeleteDocument

documentsClient.bulkDeleteDocument(config): PromiseBulkDeleteResponse>Bulk-delete multiple documentsRequired scope: document:documents:deleteMove the documents with the given ids into the trash. They are no longer accessible until they're restored from the trash. The number of provided document ids is limited to 100.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Indicates whether the operation should be performed with elevated permissions - additionally requires document:documents:admin.

 If provided, the user effectively operates as owner of all documents. This isn't supported for ready-made documents.
 | config.body*required | BulkDeleteRequest |

##### Throws
 |
 | Error Type | Error Message
 | BadRequest | Malformed request or invalid parameters.
 | Unauthorized | API token or tenant missing or corrupt.
 | Forbidden | Access forbidden. This usually happens because the user lacks the permission to access the specific endpoint, or because the target entity isn't accessible to the user.
