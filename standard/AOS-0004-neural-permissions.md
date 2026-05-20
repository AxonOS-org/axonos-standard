# AOS-0004 — Neural Permissions

Status: Draft 0.1.1 — pre-normative.  
Audience: SDK authors, kernel authors, application developers, safety assessors, and privacy reviewers.  
Normative force: draft language only until AxonOS Standard v1.0.

## 1. Purpose

AOS-0004 defines the AxonOS neural-permission model.

The central rule is: neural data is not application data.

A BCI application must not receive arbitrary neural signal data merely because it
is installed, authenticated, paired with a device, or running inside a trusted UI.

## 2. Threat model

Applications may be honest but over-broad, buggy, compromised, economically
incentivized to over-collect, or capable of correlating neural-derived events
with external identifiers.

## 3. Permission object

A neural permission is typed authority to receive a class of neural-derived
event. It should include permission id, event type, scope, max rate, payload
class, consent dependency, revocation behavior, and evidence level.

## 4. Default denial

Raw neural data is denied by default. Unknown event classes are denied. Expired
permissions are denied. Permissions outside scope are denied. Withdrawn consent
disables dependent permissions.

## 5. Capability gate

The gate checks permission, scope, active session, consent state, safety state,
event rate, event class, and version compatibility. If any check fails, delivery
is denied.

## 6. Requirements

Draft alignment requires raw data denial by default, explicit permissions,
documented event classes, consent dependency, fail-closed unknown events, and
auditable delivery decisions.

## 7. Summary

Neural permissions are the structural privacy boundary of AxonOS.
