Great. I’ll restructure the full UFC and UFGS Specification Standards into a clear, markdown-formatted version with:

* A concise executive summary
* Numbered and nested bullet points for each topic
* A table of contents
* Explicit markdown links where references apply

I’ll let you know as soon as the document is ready for your review.


# UFC and UFGS Specification Writing Standards

## Executive Summary

* **Use Official Templates and Formats:** Always use the approved UFC or UFGS template (SpecsIntact for UFGS) to ensure correct formatting, numbering, and styles. Adhere to the CSI MasterFormat® and SectionFormat™ guidelines for organizing content, and follow the unified numbering schemes for sections and paragraphs. This guarantees consistency across all documents.

* **Clarity, Consistency, and Active Voice:** Write in a clear, concise, and direct manner. Use active voice and imperative mood to address the contractor or reader directly (e.g. *"Install the equipment..."*). Avoid ambiguous terms (e.g. “relatively simple,” “as necessary”) and vague references (“etc.”, “and/or”). Define requirements explicitly rather than using phrases like “as shown on the drawings” or “as per manufacturer’s recommendations.” Consistently spell out or abbreviate terms and units per standard practice (spell out acronyms on first use, use numerals for measurements, etc.).

* **Avoid Prohibited Language and Content:** Do **not** include certain content without approval:

  * **No “Contractor shall…”** – UFCs/UFGSs are prescriptive documents; simply state requirements or instructions rather than using “shall” for the Contractor. Use “must” only if necessary for clarity, and avoid “should” (which implies optional). Use “will” for actions by the Government, and “may” only for truly optional steps or Government choices.
  * **No Proprietary or Brand-Specific Items** – Do not use brand names in specifications unless absolutely no substitute exists and **Level One Contracting Officer** approval is obtained. If a **brand-name** is authorized, include the phrase *“notwithstanding any other provision of the Contract, no other product will be acceptable”* after the named item to legally preclude alternatives, and add a bold notice at the top of the section stating it contains brand name products. Prefer generic descriptions and performance criteria for products. Use **“brand name or equal”** specifications only if approved, and always list the salient characteristics that an “equal” product must meet (per FAR Clause [52.211-6](https://www.acquisition.gov/far/52.211-6)). Avoid proprietary language that could limit competition.
  * **No Rewriting of Contract Clauses** – Do not duplicate or paraphrase standard contract clauses or regulatory requirements in the technical sections. UFGS and UFC documents should complement the contract, not restate it. Including contract terms (e.g. bonding, payment, legal rights) in specs can cause conflicts or confusion; leave those to the contract itself.
  * **No Subjective or Indefinite Phrases** – Avoid non-quantifiable descriptors like “first-class workmanship,” “properly,” “thoroughly,” or “securely.” Also avoid colloquialisms or jargon (“bulkhead” for wall, “deck” for floor, etc.). These terms are unenforceable or unclear. Specify requirements in measurable terms instead.
  * **No Gendered Pronouns** – Steer clear of pronouns like “he,” “she,” “his,” “their,” etc., when referring to entities in specifications. It’s usually clearer to repeat the noun (e.g. “the Contractor,” “the Engineer”). If pronouns are needed, use gender-neutral language (e.g. “they/their”) to avoid bias.
  * **Limited Use of Symbols and Parentheses** – Do not use symbols such as `’` `"` `#` `%` `°` `+` `±` `/` `@` in the text. Write out the words “foot,” “inch,” “number,” “percent,” “degree,” “plus,” “minus,” “plus or minus,” “by,” or “per.” *(Exception: foot and inch marks are acceptable in dimensional indications like 8'-6", and tables may use symbols where appropriate.)* Also minimize use of parentheses and quotation marks in specification text; incorporate information into the narrative or use lists/notes for clarity instead.

* **Ensure Technical Accuracy and Completeness:** Provide all information necessary for the user:

  * Clearly state performance requirements, materials, standards to comply with, and execution methods. The specification should supplement the drawings with non-graphic requirements (materials, installation procedures, quality criteria, etc.).
  * Avoid referencing another document without context – if you refer to another spec section or standard, ensure it’s listed in the references and use the correct citation format (section number and title, or standard number and title/year). When cross-referencing within the same document, refer by paragraph **title** rather than number (since numbers can change if sections are edited).
  * Include a **REFERENCES** section listing all referenced standards (ASTM, ANSI, UFC, etc.) used in the text. Use the official designation and title of each reference (including publication year or version) as given in the Unified Master Reference List (UMRL). For example, list standards as *“ASTM E119-2020, Standard Test Methods for Fire Tests of Building Construction”* and ensure that in the text you cite it simply as “ASTM E119”. Each reference in text should have a corresponding entry in the reference list, and vice versa. Use the reference tagging features of editing software (e.g. SpecsIntact) so that references are consistent and update automatically.
  * Provide **Notes to the Designer** (in UFGS) or explanatory notes (in UFC, if needed) to guide spec editors on how to choose options or edit the section for project-specific needs. These notes should appear in the document (usually highlighted or in brackets) but will be removed in the final project specification. They are for internal guidance only.
  * Clearly distinguish **mandatory requirements** from advisory statements. Do not use the term “should” in the technical requirements (as it sounds optional); reserve it for non-mandatory guidance in notes. Use **“must”** or just imperative statements for requirements that must be followed.
  * **New or Uncommon Materials:** If specifying a material or technology that is new or not widely proven, include criteria to ensure its suitability. Require that its performance be validated by testing or documented experience. For example, state that any new product must have successful laboratory and field tests (with conditions of actual use) by reputable independent labs. The specification writer should gather available data from manufacturers and industry organizations, possibly including a generic specification template from the manufacturer that can be adapted. Always ensure such content is made generic (no proprietary bias) and meets the same standard of quality as other specs. The goal is to encourage innovation while managing risk appropriately – do not specify a brand-new product without evidence and without allowing for an equal alternative if possible.

* **Quality Control and Changes:** Keep track of document revisions and maintain consistency:

  * Follow the official process for changes and revisions. Minor **administrative edits** (typos, format fixes, correcting reference citations, etc.) are considered *“clerical repairs”* and do not need formal change documentation in the header or change log.
  * **Changes** (technical modifications to a published spec) should be logged. Indicate the change number and date in the section header/banner and section date tag (without altering the original publication date of the section). Provide a brief summary of the change for record. For example, a section banner might show “Change 2 – 08/16” with the preparing activity and superseded information. Use the format and procedures outlined for your agency to record changes (e.g. a Change Notice or Change List entry).
  * **Revisions** (comprehensive updates or reissue of a spec) require a new publication date. If more than about 25% of the content is being changed, or more than 5 separate Changes have been issued, a full Revision is typically warranted. Update the section’s date in the header to the new release date and list the previous edition as “Superseded” with its date. Also update the **“Superseding/Superseded”** information in the header to show the link between the new revision and the old version (including if the section number changed).
  * When marking changes in the text of draft documents, use the proper notation: for UFGS, enclose new or changed text with `\#\ ... /#/` markers (where `#` is the change number) to flag additions/edits. Omit these markers in the final published version; they are just for review drafts. Similarly, remove prior change markings when issuing a new revision.
  * **Approval Workflow:** Coordinate drafts through the appropriate Tri-Service channels. UFCs and UFGS are **joint publications** – Army, Navy, and Air Force representatives (Discipline Working Group members and Engineering Senior Executive Panel for criteria) must review and approve them. As a preparing activity, incorporate feedback from other agencies. Finalize new or revised documents by submitting them to the designated approval authority (the Technical Proponent or Coordinating Panel/ESEP as required) for signature. Do not publish changes affecting technical content without consensus from the other services.

By following these standards, UFC (Unified Facilities Criteria) documents and UFGS (Unified Facilities Guide Specifications) will be consistent, technically sound, and usable across all DoD agencies. Below is a detailed breakdown of the guidelines from the UFC 1-300-01 **Criteria Format Standard** (for criteria documents) and UFC 1-300-02 **UFGS Format Standard** (for guide specifications).

## Table of Contents

1. **UFC 1-300-01 Criteria Format Standard (Guidance for UFC Documents)**
   1.1 Purpose and Scope
   1.2 Applicability
   1.3 References and Authority
   1.4 Format and Organization
     1.4.1 Variations in Format
     1.4.2 Content Structure and Numbering
   1.5 Publication and Maintenance
     1.5.1 Assigning Publication Numbers
     1.5.2 Document Size and Volumes
     1.5.3 Publication Date
   1.6 Document Updates
     1.6.1 Changes (Minor Updates)
     1.6.2 Identifying Changes in Text
     1.6.3 Revisions (Major Updates)
   1.7 Electronic Format Requirements
     1.7.1 UFC Template and Style
     1.7.2 Digital Format (PDF)
   1.8 Copyright Releases
   1.9 Registered Trademarks
   1.10 Glossary and Acronyms
   1.11 References

2. **UFC 1-300-02 UFGS Format Standard (Guidance for UFGS Sections)**
   2.1 Purpose and Scope
   2.2 Applicability
   2.3 References and Fundamental Resources
   2.4 Content and Format Guidelines
     2.4.1 General Content Guidance for UFGS
     2.4.2 Editing UFGS for Project Use
   2.5 UFGS Section Organization
     2.5.1 CSI 3-Part Section Structure
     2.5.2 Table of Contents and Section TOC
     2.5.3 Attachments and Appendices
   2.6 Formatting Rules
     2.6.1 Electronic File Format (SpecsIntact)
     2.6.2 Section and Paragraph Numbering
     2.6.3 Subpart Titles
     2.6.4 “Notes to the Designer” Usage
     2.6.5 Units of Measure (English/Metric)
   2.7 Referenced Standards and Cross-References
     2.7.1 Listing Reference Publications (REFERENCES section)
     2.7.2 Citing Standards Organizations (UMRL Acronyms)
     2.7.3 Federal Acquisition Regulation (FAR) Clauses in Specs
     2.7.4 Reference Dates and Revisions
     2.7.5 Quoting vs. Referencing Standards
     2.7.6 Cross-References to Other Sections
   2.8 Tailoring Options in UFGS
     2.8.1 Service-Specific Tailoring
     2.8.2 Design-Build vs. Design-Bid-Build Tailoring
   2.9 Language and Style Conventions
     2.9.1 Bracketed Options
     2.9.2 “Submittals” Article and Submittal Items
     2.9.3 Submittal Descriptions (SD numbers)
     2.9.4 Submittal Naming and Tagging in Text
     2.9.5 Submittal Classifications (G, S, etc.)
     2.9.6 Submittal Reviewers (Army/Navy procedures)
     2.9.7 Design-Build Submittals After Award (D, C, R, A codes)
     2.9.8 O\&M Data and Manuals
   2.10 Writing Style Guidelines (UFGS)
     2.10.1 Voice, Mood, and Tense
     2.10.2 Abbreviations and Acronyms
     2.10.3 Numbers and Units
     2.10.4 Terminology (Jargon and Redundancies)
     2.10.5 Avoidance of Symbols and Pronouns
     2.10.6 Capitalization of Defined Terms
     2.10.7 Handling of Brand Names and “Or Equal”
     2.10.8 Warranty Statements
     2.10.9 Excluding Contract Boilerplate
     2.10.10 Introducing New or Innovative Items
   2.11 Tables, Forms, and Figures
     2.11.1 Formatted Tables in Specs
     2.11.2 External Forms, Graphics, and URLs
   2.12 Modification Records and Approval
     2.12.1 Clerical Changes (Repairs)
     2.12.2 Technical Changes (Change Notices)
     2.12.3 Revisions (Full Updates)
     2.12.4 Superseding Dates and Section History
     2.12.5 Tri-Service Approval Process

---

## 1. UFC 1-300-01 Criteria Format Standard (Guidance for UFC Documents)

**1.1 Purpose and Scope:** This Unified Facilities Criteria (UFC) document (UFC 1-300-01, *Criteria Format Standard*) provides a unified approach to the appearance, formatting, and content of all UFC and FC (Facility Criteria) documents. Its goal is to ensure that all DoD criteria documents are presented in a consistent manner so they can be easily used and understood by all Military Departments. UFCs are used to convey planning, design, construction, and operations/maintenance criteria, and FCs are similar criteria documents used by a single service (not unified across all services). In accordance with the authority in [MIL-STD-3007](https://www.wbdg.org/ffc/dod/federal-military-specifications-standards/mil-std-3007) (the Standard Practice for UFC and UFGS), UFCs are prepared by DoD committees called Discipline Working Groups (DWGs) for each technical discipline, and are ultimately issued under the authority of the Engineering Senior Executive Panel (ESEP) which oversees the tri-service criteria program.

**1.2 Applicability:** The UFC format standard applies to **all** UFC and FC documents developed by or for the Army, Navy, Air Force, Marine Corps, and other DoD agencies, as prescribed by MIL-STD-3007. All new or revised UFCs must conform to these format guidelines. Requirements that are specific to one service (Army, Navy, or Air Force only) are to be identified as such and used only when that service is the **design and construction agent** for a project. (In other words, the document should primarily contain unified guidance, and only include service-specific instructions in clearly marked ways when absolutely necessary.)

**1.3 References and Authority:** UFC documents derive their authority from DoD policy and must comply with higher-level standards:

* They are part of the **Tri-Service Unified Facilities Criteria system** mandated by Congress and DoD (per DoD Directive 4270.5 and related policy). The UFC system is formalized by MIL-STD-3007, which outlines how UFCs and UFGS are developed and maintained. Each UFC should include a reference to MIL-STD-3007 in its front matter to affirm this authority.
* Preparation of UFCs should also follow relevant DoD guidance on issuances. For example, the format and writing style principles in [MIL-STD-962](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36082) (“Defense Standards Format and Content”) may be used as a reference for general style, since UFCs share some characteristics with technical standards. Additionally, UFC writers are encouraged to follow plain language principles per the DoD Issuance Style Guide (clear language, avoid redundancy, etc.).
* Every UFC will contain its own **References section** (usually at the end or an appendix) listing all documents cited. When writing a UFC, ensure all references are current and relevant. Use official titles and, where applicable, include version or date. For instance, if referencing the International Building Code, list it as “IBC – International Building Code (2018)” in the References. Include key industry standards, other UFCs, UFGS, DoD directives, and so on that were cited in the text. (The UFC template provides a format for the References section.)

**1.4 Format and Organization:** UFCs have a standardized structure and appearance to promote uniformity.

* UFCs are organized into **chapters and paragraphs** with a **decimal numbering system** (similar to an outline). Major headings (chapters) are numbered 1, 2, 3, etc., and sub-levels are numbered as 1-1, 1-2, 2-1, 2-2.1, etc. (up to at least three levels, more if necessary). The UFC template will have styles pre-defined for heading levels. All UFCs should include an **Introduction chapter (Chapter 1)** with general information (purpose, scope, applicability, etc. as sub-sections), followed by chapters covering technical criteria content, and ending with any appendices (such as glossary or reference list).
* **Variations in Format:** The format prescribed by this standard is intended to be followed uniformly. If a deviation from the standard format is needed, it **must** be approved in advance by the Coordinating Panel (CP) that oversees UFC development. The DWG responsible for the UFC should submit a request explaining the needed variance to the CP early in the development process, and proceed only if approved. (In practice, this means you should not introduce novel section numbering schemes or document layouts on your own – stick to the template and standard unless an exemption is granted.)
* **Content Structure:** The UFC content itself should be arranged logically according to subject matter. UFC 1-300-01 includes an Appendix (Appendix A) that provides guidance on organizing UFC content by subject series. For example, *Series 1-200* UFCs cover general building requirements (like the DoD Building Code UFC), *Series 3-XXX* cover discipline-specific design criteria (300-series for structural, 500-series for electrical, etc.), and *Series 4-XXX* cover facility-specific criteria (400-series for various facility types). When assigning a publication number to a new UFC, choose the series that best fits the subject (the DWG will recommend an appropriate series based on these categories). For instance, a new UFC on airfield pavement evaluation might be numbered in the 3-260 series (Civil Engineering – Pavements).
* **Chapter and Paragraph Titles:** Use clear, descriptive titles for chapters, sections, and paragraphs. Chapter titles are all caps (e.g. **CHAPTER 2 DESIGN CRITERIA**), while lower-level headings use Title Case. Every major paragraph at least down to the third level should have a title, not just a number, to serve as an informative heading. If a heading has no content (because certain recommended paragraphs don’t apply), you should typically delete that heading rather than leave it empty. Only include headings/paragraphs that are applicable to the subject at hand. *(Appendix A of the UFC format standard provides a recommended list of paragraph titles and sequence based on CSI’s SectionFormat™ outline for specifications, but in UFCs (which are not contract specs) the author has more flexibility to determine logical sections. Use the suggested outline as applicable, but you are not required to include every possible heading.)*
* **Front Matter:** UFCs include standardized front matter pages:

  * **Cover/Title Page:** Lists the UFC document number, title, date, and “Approved for Public Release” statement. DoD component seals or logos may appear as appropriate. *(Use the UFC template cover page style.)*
  * **Change Record Page:** Following the title page, include a *Record of Changes* table if the UFC has been updated. This table lists change number, date, and a brief description of each change. For a brand new UFC, this table may be blank or omitted.
  * **Foreword:** UFCs typically contain a Foreword that explains the UFC program and gives context. The Foreword notes that the UFC system is prescribed by MIL-STD-3007, that UFCs are living documents subject to periodic review and update, and that they are effective upon issuance and distributed through the Whole Building Design Guide (WBDG) website. It may also direct users to submit criteria change requests (CCR) via the WBDG system for improvements. The Foreword page also includes signature blocks of the officials (from Army, NAVFAC, Air Force, and OSD) who have authorized the document.
  * **Authorities and Responsibilities:** Often included in the foreword or introduction, this clarifies the roles (e.g., DWGs prepare, Engineering Senior Executive Panel approves) and directs that recommended changes be submitted via the CCR process on the WBDG site.
  * **Table of Contents:** List all chapters, paragraph titles (usually down to the second or third level), appendices, figures, and tables with page numbers. Use the auto-generated TOC from the template, ensuring it’s up to date.
* **Back Matter:** Following the main chapters, UFCs may have appendices for supplemental information:

  * **Appendix (if needed):** Could include supporting data, example calculations, detailed tables, or in the case of UFC 1-300-01, guidance on numbering (as Appendix A). Appendices should be labeled A, B, C, etc., and referenced in the text if applicable.
  * **Glossary (if applicable):** If the UFC uses many acronyms or unique terms, include a Glossary appendix listing acronyms and definitions of terms (UFC 1-300-01 suggests including a glossary if needed). Ensure every acronym is spelled out at first use in the text, even if a glossary is provided.
  * **References:** The final appendix or section of the UFC is typically the References list (Appendix C in UFC 1-300-01). All documents cited in the UFC (military standards, other UFCs, codes, etc.) should be listed here. Use the format specified by the UFC template (which often mirrors APA or similar citation style, but usually just the document designation, title, and issuing organization). Hyperlink web addresses where appropriate (e.g., reference entries may include URLs to the source).

**1.5 Publication and Maintenance:**

* **Distribution:** All UFCs are published in **electronic media only** – there are no printed distribution by DoD. The official source is the **Whole Building Design Guide (WBDG)** website, which serves as the sole distribution method for UFCs and UFGS. Users can view or download UFC documents from the WBDG (FFC DoD Criteria library). The Memorandum of Agreement among the services establishes WBDG (managed by NIBS) as the authorized platform for publication.
* **Controlled Unclassified Information (CUI):** If a UFC contains sensitive but unclassified information (CUI), it will **not** be posted freely on WBDG. Instead, a front-matter notice and instructions for obtaining the full document are posted. The actual CUI content might be distributed through controlled channels (e.g., by request via USACE or another authority). In general, however, most UFCs are unclassified and public.
* **Assigning Publication Numbers (1.5.1):** When creating a new UFC, the DWG should recommend an appropriate document number in accordance with the established numbering system (outlined in Appendix A). UFC numbers are in the format *UFC X-XXX-XX*, where:

  * The first digit(s) represent the series (e.g., 1- for general criteria, 2- for multi-discipline or planning, 3- for discipline-specific technical criteria, 4- for facility-type criteria, 5- for mission-specific or facility systems, etc.).
  * The next set of numbers indicates the specific subject group and sequence. For example, UFC **3-530-01** is an Electrical series UFC (3-500 series) on *Interior and Exterior Lighting Systems*.
  * “FC” (Facility Criteria) documents use a similar numbering but often have an “FC” prefix and a service suffix (e.g., FC 2-100-01 (Army) might denote an Army-only document).
  * The numbering scheme is hierarchical and outlined in the UFC format standard appendix. Using the correct series helps users find related criteria. **Do not** duplicate or conflict with existing publication numbers. If in doubt, coordinate with the tri-service **Database Managers** or CP to get an approved number.
* **Document Size and Volumes (1.5.2):** Criteria documents are distributed as PDFs. If a UFC is very large (exceeding \~20 MB or extremely lengthy), it may be practical to split it into **volumes** for manageability. If split into volumes, each volume should be labeled clearly (e.g., Volume 1: Chapters 1-9; Volume 2: Appendices) and the title page should indicate the volume title. Each volume will have its own table of contents, etc., but all volumes together constitute the UFC. Generally, avoid excessive file sizes by using reasonable image compression and only split when necessary.
* **Publication Date (1.5.3):** The UFC’s official publication date (and any change dates) appear on the cover and each page header. The **initial publication date** remains associated with the UFC until it is formally revised. Interim changes (Change 1, Change 2, etc.) will have their dates noted in the Record of Changes and section headers, but the main date on the cover often remains the original publication date (with a note like “Change X, \[date]”). After a major Revision, a new publication date is assigned and the document supersedes the previous edition. Coordinate publication timing with the **National Institute of Building Sciences (NIBS)** which manages WBDG, to ensure the document is posted promptly once approved (the UFC program office typically handles this coordination).

**1.6 Document Updates:** UFCs are living documents that undergo updates for accuracy, new technology, and criteria changes. Updates can be issued as **Changes** or complete **Revisions**.

* **Changes (1.6.1):** A “Change” is a limited update that amends no more than about 25% of the UFC content. Changes are numbered sequentially (Change 1, Change 2, etc.) and are used to address specific criteria change requests or corrections without reissuing the entire document. Per policy, a given UFC should not accumulate more than **five Changes**; after five changes, a full Revision is required. *(Exception: certain continually updated UFCs like the DoD Pricing Guide may exceed five changes before revision, but that is an approved special case.)* Changes must be approved by the responsible DWG and the Coordinating Panel. Once approved, publish changes by updating the UFC file on WBDG with the change number and date. Each Change will be noted in the change record table. For example, **UFC 1-300-01 Change 1** might update a few paragraphs; the next page header might show “Change 1, Jan 2024” and the Record of Changes will list what was changed.

  * **Identifying Changes in the Text (1.6.2):** When preparing a draft that includes changes, clearly mark the new or modified text so that reviewers can see what has been altered. The standard method is to insert the change number in backslash and forward-slash markers around the changed text. For example: `\1\This sentence is added in Change 1./1/`. At the beginning of changed paragraphs, you might also see the change number in brackets. In the final published UFC (PDF), these markers may either be removed or retained visibly (practices vary, but often published UFCs show change markings to help users identify new content). A legend is usually provided explaining that *\1.../1/* indicates Change 1. Do **not** mark trivial editorial fixes. Do mark substantive additions, modifications, or deletions (though deletions might be indicated with a note or by strikeout in draft form).
* **Revisions (1.6.3):** A “Revision” is a reissue of the UFC that incorporates many changes or a broad update to content. Typically, if the criteria have changed so much that incorporating them piecemeal is impractical, or if the UFC has had multiple changes and needs reorganization, the document is **revised** and given a new date (and sometimes a new UFC number if it’s a consolidation). Triggers for a revision include: more than 25% of the text requiring changes, exceeding the limit of 5 changes, or significant shifts in policy/technology that affect the whole document. Revisions undergo full coordination (DWG -> CP -> ESEP approval) like a new UFC.

  * **Formatting a Revision (1.6.3.1):** When preparing a Revision, start with the latest UFC template to ensure format compliance. Remove all previous change markings and notations, so that the revised document reads cleanly. The Record of Changes on page ii should be reset or include an entry that the document was revised on X date (superseding the previous edition). Update the publication date on the cover and in headers/footers. If the UFC number has changed or if it now supersedes multiple old documents, make sure to indicate that in the superseding statement on the cover or foreword (e.g., *“This UFC supersedes UFC X-XXX-XX, dated 1 June 2010.”*).
  * Revisions are considered **final** publications requiring senior approval (ESEP for UFCs). Once the revision is signed off, it is published as a new edition of the UFC (with no change number, since it’s an all-new baseline). For example, UFC 3-XX-YYY might be revised January 2025; the new PDF would be UFC 3-XX-YYY (January 2025) with no change marks, and any future small updates start over at Change 1 from that baseline.

*(In summary, limit incremental changes and bundle major updates into formal revisions. Always document changes clearly, and don’t let the document become too patchy with many amendments.)*

**1.7 Electronic Format Requirements:** UFC documents must be prepared and delivered in specified electronic formats.

* **UFC Template (1.7.1):** DoD provides a UFC MS Word template or similar format to authors. **Always use the current UFC template** when writing or editing a UFC. The template contains predefined paragraph styles, heading numbering, cover page layout, and other formatting macros to ensure consistency. It also includes boilerplate text (such as the foreword and signature page format, record of changes table, etc.). Using the template not only saves time but also ensures that your document will automatically meet most format rules (margin sizes, fonts, headers/footers, etc.). The template and other tools can typically be found on the WBDG UFC website or through the criteria management offices.
* **PDF (1.7.2):** The final published format of all UFCs is Adobe PDF. Ensure that the Word (or source file) is correctly converted to PDF with bookmarks for major headings (the template styles should convert to PDF bookmarks). The PDF should be set up for **bookmarks and hyperlinks** – i.e., the table of contents entries, references, and any internal cross-references should be clickable in the PDF. Check that the PDF is clear and that any figures or tables are legible. If a UFC has embedded drawings or complex graphics, optimize the PDF so that file size remains reasonable without losing clarity. All UFC PDFs are posted on **WBDG** with their UFC number and date.

  * Note: Some UFCs may also be provided in **HTML** or other accessible formats on WBDG, but the PDF is the official version.
  * If the UFC includes attachments like spreadsheets or models (rare for UFCs; more common for UFGS, which might have forms), coordinate with NIBS/WBDG on how those are made available (perhaps as separate downloadable files linked in the UFC).
* **Software Compatibility:** The template may require certain Word versions or plug-ins. Follow instructions provided with it. Do not introduce formatting that isn’t in the template (like text boxes, non-standard fonts, etc.).
* The UFC should also be compatible with requirements for 508 accessibility (if it’s an official DoD publication for public release, ensure that the PDF text is searchable and images have alt-text as needed).

**1.8 Copyright Releases:** If any part of the UFC incorporates copyrighted material (e.g., figures, tables, or substantial text excerpts from a privately published source), you **must identify it and obtain permission** from the copyright holder for use in the UFC. The UFC format requires that any copyrighted content is acknowledged at the point of use (usually via a footnote or parenthetical credit in the text or figure caption). Additionally, a statement in the front matter may note that “Any copyrighted material included in this UFC has been approved for use by the copyright owner”.

* In practice, try to avoid using proprietary content. Often you can reference a standard or manual rather than copy it. But if, for example, a UFC on seismic design wants to include a graph from an ASCE publication, you would seek written permission from ASCE and then note in the figure caption something like: “*Reprinted with permission from ASCE…*”. Keep documentation of that permission on file.
* All text in UFCs should ideally be DoD-authored or public domain. If you need to quote a section of a code or standard, verify if that standard is copyrighted. Many industry standards are copyrighted, so instead of quoting large passages, it’s better to summarize or simply refer to them.
* Include any required copyright statements or credits in an appendix or footnote as required by the permission grant. Failure to do so could infringe on intellectual property rights.

**1.9 Registered Trademarks:** Use of trademarked names should be avoided in UFCs. Where possible, use generic descriptions instead of brand names (as noted earlier in “Proprietary content”). If referring to a specific product or system is necessary (for clarity or as an example), include the trademark (™ or ®) symbol on first use and a footnote indicating that it is a trademark of whatever company. But generally:

* Do not endorse or appear to endorse any specific brand.
* If a trademarked term has become generic vocabulary and no other term exists, you may use it sparingly (for example, “Kevlar®” if describing a material—then perhaps note “(a proprietary aramid fiber)”). Provide a generic equivalent description if possible.
* Many times, simply capitalizing a common name is enough if it’s defined. For instance, say “high-strength bolts shall conform to ASTM specs” rather than naming a brand of bolt.
* The UFC template might have guidance on listing trademarks in the Glossary if used. Be consistent and fair in any references to trademarked items.

**1.10 Glossary and Acronyms:** If the UFC contains many acronyms, abbreviations, or unique terms, include a Glossary section (often Appendix B). The Glossary should list acronyms alphabetically with their meanings (e.g., *“DWG – Discipline Working Group”*, *“RFP – Request for Proposal”*) and any specialized definitions of terms used in the UFC. This helps ensure all readers (including those from different services or backgrounds) can understand the terminology. Some tips:

* Even if you have a glossary, still spell out acronyms the first time they appear in the text, followed by the acronym in parentheses. E.g., “Unified Master Reference List (UMRL)”.
* The Glossary can also define terms that have specific meaning in the context of DoD criteria (for example, definitions of “Shall, Must, Should, Will” if not already standardized).
* If MIL-STD-3007 or other policy contains an official Glossary, you can align with those definitions.
* A small UFC may not need a glossary at all; in that case, ensure clarity in text. Only include this section if it adds value.

**1.11 References:** Every UFC ends with a list of **References** (typically labeled “REFERENCES” or as Appendix C). Ensure this list includes all documents cited in the UFC and no others (it’s not meant to be a bibliography of everything you read, just what the text explicitly references). The references might include:

* **Military Criteria:** Other UFCs or FCs. List them by number and title (and date if relevant). Example: *“UFC 1-200-01, DoD Building Code (General Building Requirements)”*. You can optionally include the latest change or revision date if needed for clarity.
* **DoD Issuances:** DoD Directives, Instructions, and other standards (like DoDD 4270.5, or MIL-STD-3007). Give their full title and date. Example: *“DoD Directive 4270.5, Military Construction, dated 2/12/2005.”*
* **Industry Standards:** ASTM, ANSI, ASHRAE, ISO, etc. Give the designation and title, and possibly year. (Following a format consistent with the UMRL is ideal; e.g., *“ASTM E119-2020, Standard Test Methods for Fire Tests of Building Construction and Materials”*).
* **Codes and Regulations:** If the UFC references international or model codes (IBC, NEC, etc.), list them. Also FAR clauses if you referenced any (though usually in UFCs you do not directly reference FAR; that’s more for UFGS).
* **Other References:** Textbooks, handbooks, or other sources if directly cited. This is uncommon in UFCs, but if, for example, you quoted the USACE Soil Design Manual, list it.
* The references should be ordered in a logical manner (often grouped by category: Government/Military references first, then industry, then non-government). UFC 1-300-01’s reference list itself cites things like MasterFormat, CSI guides, etc., which indicates they list all external resources they mention.
* Each reference entry might include an identifier in the text. Sometimes superscript numbers or bracketed numbers are used for citations in UFC text, corresponding to the numbered list in References. Follow the approach given by the UFC template (some use numeric referencing, others just rely on listing by order of appearance). For UFC 1-300-01, the references in the text were indicated by footnote-like numbering `\1\ ... /1/` which correspond to the list entries. Ensure these markers or callouts match the final list.

*(By following the above guidelines in Section 1, you ensure that any UFC document you produce is formatted correctly, contains all required front/back matter, and avoids common content mistakes. Now, the next section will address the UFGS format standard, which has more detailed instructions for preparing guide specifications.)*

---

## 2. UFC 1-300-02 UFGS Format Standard (Guidance for UFGS Sections)

**2.1 Purpose and Scope:** UFC 1-300-02, *Unified Facilities Guide Specifications (UFGS) Format Standard*, provides guidance for the development and preparation of UFGS sections. UFGS are a library of master guide specification sections used in construction contract documents for military facilities. This UFC aims to unify the requirements for how these spec sections are written and formatted so that all UFGS, regardless of preparing agency, have a common structure and style. UFGS sections are published under the auspices of the Tri-Service Engineering Senior Executive Panel (ESEP) – the same body that oversees UFCs – and are prepared by Discipline Working Groups (DWGs) consisting of subject-matter experts from Army, NAVFAC (Navy), and AFCEC (Air Force). UFGS are made available to users (government and contractors) electronically at no cost, via distribution sources identified in the UFC foreword (primarily the WBDG website). The guide specifications are **not proprietary** – they are deliberately generic and performance-based, allowing competition among products.

**2.2 Applicability:** This standard applies to all agencies (Army, Navy, Air Force, etc.) and their contractors who prepare or update UFGS sections. In practice, whenever you write a new UFGS section or edit an existing one, you must follow UFC 1-300-02. Some UFGS requirements or options are service-specific; those are to be used only when that particular service is the contracting agent for the project. For example, if a UFGS has an option that only applies to Navy projects, that option should be included only in specs for Navy jobs. The UFC makes it clear that any requirements labeled for a specific service (Army, Navy, or Air Force) are only applicable when that service is the design/construction agent. Generally, UFGS are intended to be unified as much as possible, so service-specific variations are minimized and isolated. All preparers must also comply with overarching policy in MIL-STD-3007 (which governs both UFC and UFGS development) – so the coordination and approval processes described later are mandatory for everyone.

**2.3 References and Fundamental Resources:** Preparing UFGS sections requires familiarity with several key references and tools:

* **Construction Specifications Institute (CSI) Formats:** UFGS formatting is based on CSI’s MasterFormat®, SectionFormat™, and PageFormat™ standards for specifications. MasterFormat is the indexing system that assigns each spec section a number and title (e.g., “03 30 00 – Cast-in-Place Concrete”). SectionFormat provides a standard three-part outline (Part 1 “GENERAL”, Part 2 “PRODUCTS”, Part 3 “EXECUTION”) and standard article titles within each part. PageFormat covers the standard layout on the page (margins, paragraph numbering scheme, etc.). The UFGS use the latest MasterFormat numbering (currently the 6-digit with optional two-digit extension format) and generally adhere to SectionFormat. For instance, every UFGS section should be organized into the three parts and use the recommended article sequence (e.g., Part 1 includes references, submittals, quality control, etc., Part 2 lists materials, Part 3 lists installation/test requirements).

  * **MasterFormat Compliance:** Each UFGS is identified by a MasterFormat section number and title. Use the exact MasterFormat title if the number is a standard one. If a UFGS covers a topic not precisely in MasterFormat, a custom section number ending in a **.10, .20, .30,** etc. might be used to indicate a specialization (the *fifth-level* two-digit code used by UFGS to differentiate service-specific or specialized sections). For example, *“01 45 00.00 10 Quality Control”* might be an Army-specific version of a quality control section, indicated by the “10” suffix for Army. The codes are: **10 = Army**, **20 = Navy**, **30 = Air Force**, **40 = NASA**. A UFGS with no suffix (just six digits) is a fully unified section used by all. Always ensure the section number you assign does not conflict with another UFGS or MasterFormat listing. (The DWG and SpecsIntact database managers will help coordinate section numbers.)
* **SpecsIntact Software:** UFGS sections must be written using SpecsIntact, a specification editing software developed by NASA and adopted by the Tri-Services. SpecsIntact enforces many formatting rules automatically and uses **XML-based .SEC files** for specs. It also handles tagging of paragraphs, references, submittals, options, etc., and can produce merged project manuals. Use of SpecsIntact is **mandatory** for UFGS prep. Download SpecsIntact from the official site (e.g., the Kennedy Space Center website or via the WBDG link) and familiarize yourself with its functions. There are two key guides:

  * *SpecsIntact QuickStart Guide (Numeric)* – covers how to tag and number paragraphs using the numeric system.
  * *SpecsIntact Process & Print/Publish Guide* – covers how to compile sections, generate tables of contents, and publish specs.
    Use these guides (available as PDFs from NASA) for reference on the mechanics of editing.
* **Tri-Service Standard References:** UFGS often refer to common references such as [UFGS 01 33 00 “Submittal Procedures”](https://www.wbdg.org/ffc/dod/ufgs/ufgs-01-33-00) for general submittal requirements, or [UFGS 01 78 23 “Operation and Maintenance Data”](https://www.wbdg.org/ffc/dod/ufgs/ufgs-01-78-23) for O\&M manuals, etc. Become familiar with Division 01 UFGS sections (general requirements) because individual technical sections should not duplicate information found in Division 01. The UFC 1-300-02 reference list includes many of these key UFGS sections (for sustainability reporting, O\&M requirements, etc.) as resources.
* **FAR and DFARS Clauses:** While the actual contract clauses are not included in UFGS text, the format standard references FAR clause [52.211-6 “Brand Name or Equal”](https://www.acquisition.gov/far/52.211-6) as a basis for how to handle proprietary items. Additionally, UFGS writers should be generally aware of procurement regulations that affect specs (e.g., restrictions on using brand names, requirements for including certain clauses if certain materials are used, etc.). Coordination with contracting officers may be necessary if a spec section treads into territory governed by FAR (for example, warranties or options).
* **UMRL (Unified Master Reference List):** This is a tri-service maintained list of approved reference standards (military and civilian) along with their acronyms. The UMRL is integrated into SpecsIntact – when you cite a standard, you use the UMRL acronym (like ASTM, NAVFAC, UFC, etc.) so that SpecsIntact can generate the References list automatically with the full titles. Always use the official acronyms and titles as per UMRL for consistency.

Before writing or editing a UFGS, gather all these resources. Open the latest similar UFGS sections for reference on style. Use SpecsIntact from the start rather than writing in Word and converting (to avoid format cleanup later).

**2.4 Content and Format Guidelines:**

**2.4.1 General Content Guidance for UFGS:** UFGS sections translate design requirements (criteria) into construction specification requirements. They are intended for use in contract documents, so they must be written clearly for contractors/bidders, but they originate from design criteria that have been coordinated with industry. Each technical Discipline Working Group (DWG) is responsible for the technical accuracy, format, and overall quality of their assigned UFGS sections. The UFC 1-300-02 standard sets the general required content and appearance for all UFGS:

* UFGS sections follow the CSI SectionFormat™ three-part structure (General, Products, Execution) and standard article sequence. This structure is embedded in the SpecsIntact UFGS templates, so following the template naturally aligns with CSI format.
* UFGS are designed to be edited as needed for a project, but the master text provides the baseline. They should be broad enough to cover various scenarios (different climates, materials, methods) via options (brackets or tailoring) but **not** so broad that they become unclear. The guide spec’s job is to provide all typical requirements that have been agreed upon by the Tri-Services and to highlight where choices or additions may be needed for a project.
* **Avoid Duplication of Criteria:** Do not repeat extensive design criteria or explanations in the specification text that are already covered in design criteria documents (UFCs) or that could become quickly outdated. Instead, reference the relevant UFC or standard. For instance, rather than copying a table of wind loads criteria into a roofing spec, the UFGS might say *“Design roof system to meet wind uplift pressures as required by UFC 1-200-01 (DoD Building Code) and ASCE 7.”* The spec thus references the criteria rather than duplicating it. This ensures the spec stays aligned with criteria updates.
* **No Project-Specific Info in Masters:** Master UFGS are **generic** – they should not include project-specific or location-specific requirements (except as options). For example, a master spec should never hard-code something like “for Fort Bliss only, do X.” Instead, it might offer an option or note like *“\[For hot-dry climates, XYZ additive may be used].”* Generally, leave site-specific adaptations to the project editors. As the UFC says, do not include restrictions for particular localities in the master; if needed, provide optional provisions that a designer can include based on climate or other conditions.
* **Clarity to Avoid Misinterpretation:** Write the UFGS in a way that a construction contractor and contract admin personnel will interpret it correctly and consistently. Ambiguities can lead to legal disputes or change orders. For example, avoid open-ended phrases like “work shall be of high quality” – instead specify measurable criteria (e.g. required standards or outcomes). Another example: instead of “Install equipment as per manufacturer’s recommendations,” (which is vague and potentially unenforceable), incorporate the critical requirements from those recommendations or state “Install equipment in accordance with **\[specific standard or section]** and the manufacturer’s instructions.” The spec should make it clear what the contractor is responsible for.
* **Leverage Industry Standards:** Wherever possible, reference well-established non-government standards (ASTM, IEEE, etc.) rather than writing proprietary criteria. The UFGS should not restate the content of those standards (to avoid inconsistencies). Merely require compliance. For example, say “Concrete shall meet ASTM C94 requirements for Ready-Mix Concrete.” This reduces the need for spec text and automatically keeps the project aligned with industry practice. Only elaborate where the standard gives options or where DoD needs to exceed the standard.
* **Keep Requirements Non-Geographic:** UFGS are intended to be applicable to projects worldwide (unless the section itself is region-specific, which is rare). So do not bake in assumptions that only apply to certain regions (snow load requirements, seismic zones, etc.). Instead, refer to the project’s design criteria which will vary by location. Or provide optional text that can be included or excluded. For example, do not include “Contractor shall design for frost depth of 48 inches” in a master spec; that is location-specific (Alaska vs. Florida). Instead, if addressing frost, perhaps note, “If project site is in a frost-susceptible region, include requirements for frost protection in foundations as specified in UFC 3-\*\*\*.” *(In practice, climate-specific requirements are determined by the design documents and should be reflected on drawings or in design UFCs, not in the generic spec – except via options.)*

**2.4.2 Editing UFGS for Project Use:** A fundamental principle spelled out in UFC 1-300-02 is that **UFGS masters provide the minimum baseline requirements**, and it is expected that project spec writers (designers) will edit them to suit the project’s needs. Some key points:

* A UFGS master often contains **bracketed text, choices, and notes** to the spec writer. The project editor must make decisions on those: select the appropriate options, fill in project-specific values, and remove portions that don’t apply. **Do not include** in the final project spec any options that are not chosen or any notes/instructions meant for the editor.
* **Do not reduce quality below the master’s baseline.** The UFC explicitly states: *“Do not specify lesser quality requirements than are provided in the UFGS.”*. The master is written to ensure a minimum acceptable quality and performance. If anything, project edits might add more stringent requirements (for a special project need) or include additional provisions, but one should never delete a requirement just to cut cost below what Tri-Service consensus has set, unless there is a very good justification and it does not compromise the intent.
* The UFGS includes a lot of guidance via **Notes to the Designer** (which are embedded in the master text in SpecsIntact, usually in blue or within braces). These notes help the project spec writer understand when to use certain options or how to tailor the section. For example, a note might say, *“Note: For Navy projects, include the following paragraph; for Army and Air Force, delete it.”* Follow these instructions when editing for a project.
* The masters are arranged to cover a wide range of scenarios, so a particular project likely doesn’t need every paragraph. **It is normal to delete inapplicable paragraphs** when editing a project spec. The UFC suggests using the arrangement and sequence given, but eliminating those paragraphs that do not apply and adding any project-specific ones needed【66†L1337-L1345 (Table A-1)】. For instance, if a section has an option for “Above-ground tanks” vs “Underground tanks” and your project has only above-ground, you would remove the underground-related requirements entirely.
* If the project scope demands additional requirements not in the master (perhaps a unique material or test), the spec writer can add to the section, but should try to maintain the style and format. If you find yourself frequently adding something that might be generally useful, consider submitting a Criteria Change Request (CCR) so that the UFGS master can be updated for future projects.
* **Tailoring and Bracketing (see Section 2.8 below)** are the primary mechanisms masters use to handle different needs. Project editors will apply or not apply those tailoring options as appropriate. The outcome should be a smooth, coherent spec section that reads as if it was originally written just for that project (no extraneous options or instructions left visible).

In summary, the master UFGS is a tool – it must be intelligently edited by the designer for each project. The UFC format standard makes sure the master is set up to be easily edited and that it contains markers for all variable items. It’s the responsibility of the project spec writer to use those correctly and not to deviate from the intent of the master (except to add project-specific info or higher standards).

**2.5 UFGS Section Organization:**

Each UFGS section must follow a standard organizational structure, primarily defined by CSI’s SectionFormat and tailored to DoD needs:

* **Three-Part Format:** Every UFGS section is divided into **PART 1 – GENERAL, PART 2 – PRODUCTS, PART 3 – EXECUTION**. CSI recommends this format and it is mandatory in UFGS. Within each part, subjects are arranged in a consistent sequence.

  * Part 1 (GENERAL) covers the scope, references, submittals, quality assurance, delivery/storage, sequencing, warranties, etc. – basically all administrative and procedural requirements.
  * Part 2 (PRODUCTS) lists the materials, products, systems, or assemblies required, including descriptions, properties, standards they must meet, fabrication (if pre-fab), etc.
  * Part 3 (EXECUTION) describes how products are to be installed, applied, tested, or operated in the field – including preparation, workmanship, erection, installation, tolerances, field quality control (tests/inspections), and post-installation actions (cleanup, training, etc.).
* **Required and Optional Articles:** CSI SectionFormat provides a list of standard article titles in each Part. The UFGS format guidance (Appendix A of the UFC) includes these recommended paragraph titles and their order【66†L1337-L1345 (Table A-1)】. For example, Part 1 typically includes **References, Submittals, Quality Assurance, Delivery/Storage, Site Conditions**, etc. Part 2 might be organized by system component or material type, and Part 3 usually includes **Preparation, Installation/Application, Field Quality Control, and Demonstration/Training** if applicable. Use these conventional headings where appropriate so that users can easily navigate the spec.

  * Not all sections will use all possible headings; include only those relevant. For instance, if no special Quality Assurance provisions are needed beyond standard submittals and industry standards, you might not include a separate “Quality Assurance” article. Conversely, if a spec requires a **Preconstruction Conference** or a mockup, those would appear under Part 1, typically in a **Quality Assurance** or **General** paragraph.
  * If a Part of the section has **no content**, do not delete the Part – instead insert the phrase “**NOT USED**.” For example, if Part 2 has no materials (perhaps the section is purely procedural, though that’s rare), you would still include the Part 2 heading and write “Not Used.” in that part. This indicates to the reader that the part was intentionally left blank. Within parts, however, do not leave numbered paragraphs blank – remove them if not used. Only whole Parts get the "Not Used" treatment. *(This seldom occurs; most sections will use all three parts. An example might be a section that only specifies performance testing (Part 3) but actually even that would require equipment (Part 2) and references (Part 1), so again, it's rare.)*
* **Section Table of Contents (TOC):** SpecsIntact can generate a mini-TOC at the start of each section listing its articles and paragraphs. The UFC says the section TOC is optional: SpecsIntact has two modes – printing a master or project-level TOC for all sections, and printing a TOC at the beginning of each section if desired. The UFGS standard approach is usually **not** to include a TOC within each spec section in the project manual, because the project manual itself has an overall contents and sections are short enough to scan. However, during editing or review, the section TOC can be useful.

  * *Recommendation:* Do not include a section TOC in the final issued spec unless agency practice calls for it. If you do include attachments (appendices) within a section, SpecsIntact will list them in a mini-TOC automatically.
  * **Attachments List:** If the section has attachments like appendices or figures at the end, you can list them in the section’s table of contents by using the `<ATT>` tag around the attachment title. This signals SpecsIntact to include that title in the TOC output for the section.
* **Attachments and Appendices (2-1.3):** UFGS sections **rarely include appendices or lengthy attachments** within the section file. The preference is to keep each spec section focused on textual requirements and handle bulky data (forms, charts, lengthy test reports, etc.) outside the spec (see Section 2.11 on Tables and Forms). If you absolutely need to attach something to a spec:

  * Consider if it can be a separate contract document or included in the project’s attachments rather than the spec text. For example, large tables of data might be better as a separate file provided to bidders.
  * If an appendix is needed in a UFGS section (for example, a detailed calculation method or a reference form), SpecsIntact allows creating an Appendix at the end of the section. Use the appropriate tags (`<APPENDIX>` in SpecsIntact) and give it a title. Keep appendices simple (text or tables). Complex appendices that include figures, etc., might be better handled as separate PDF attachments to the contract rather than part of the spec text.
  * The UFC specifically notes: *“Attaching appendices to a UFGS section is rarely necessary. Create a simple appendix at the end of a section in SpecsIntact when necessary for project specifications.”* And if there is a **complex appendix** (like something that cannot be nicely rendered in the spec format), it may be handled by manually inserting a PDF into the final project manual. For instance, perhaps a geological report excerpt might be included as an attachment PDF. In such cases, one would note in the spec “See Appendix X (bound separately)” and ensure it’s delivered with the docs.
  * **Figures:** The UFGS standard is **do not include figures within the text of a specification section**. If drawings or sketches are needed, they should typically be part of the drawings set, not embedded in specs. If a figure (illustration) is absolutely needed in the spec (e.g., a wiring schematic for a special system that is not in the drawing set), the approach is to attach it as a separate PDF page at the end of the spec or in the project manual, rather than trying to include it inline. Essentially, treat it like an appendix or separate file.
  * In summary: keep UFGS sections as text-focused as possible. Use references to external documents or drawings for visuals. Only include attachments when no other option, and then list them clearly and integrate via tags so they appear in contents.

Following these organization rules ensures that all UFGS sections have a familiar layout. A contractor or engineer who opens any UFGS will immediately know where to look for certain information (because Part 1 always has submittals, Part 3 has execution requirements, etc.). Consistency here is key to usability.

**2.6 Formatting Rules:**

*(This section consolidates various format-related instructions from the UFC into one place.)*

**2.6.1 Electronic File Format (SpecsIntact Usage):**

* **SpecsIntact Mandatory:** UFGS sections **must** be prepared in SpecsIntact format. The SpecsIntact software uses an **Extensible Markup Language (XML)** based format with the file extension “.SEC” for specification sections. Each .SEC file represents one spec section. The SpecsIntact template for UFGS already contains all the necessary XML tags for parts, paragraphs, lists, etc. By using it, the output (whether PDF or Word or HTML) will automatically meet UFGS format criteria: correct fonts, indentations, numbering, headers/footers, etc.

  * **Page Layout:** The standard page layout is portrait orientation, 1-inch margins, a header with the section number, UFC publication info, and date, and a footer with page number. Body text is typically Times New Roman 12 pt (or equivalent). SpecsIntact ensures things like paragraph tags (`<PAR>`, `<SUBPAR>`, `<LST>` for lists, etc.) are properly applied. Do not override these.
  * **Output Formats:** SpecsIntact can output to PDF and Word (DOC) formats for review or publishing. The final contract specs are often compiled in PDF format. The **entire UFGS Master library** is available in SpecsIntact format (often a ZIP file download) – ensure you have the latest version of any section before editing.
* **Paragraph Numbering and Tags:** SpecsIntact uses special tags to label each paragraph level, which then generate the numbering. For example, a first-level paragraph in Part 1 might be tagged `<PAR>` and come out as 1.1, a second-level `<SUBPAR>` becomes 1.1.1, etc., down to itemized lists `<LST>` giving letters or numbers. Appendix A of UFC 1-300-02 provides a table (Table A-1) showing examples of the numeric format with and without tags for each level. UFGS typically number paragraphs to four levels deep (1.1.1.1), and beyond that use bulleted or lettered lists (a., (1), (a), 1.) as needed, which SpecsIntact handles with `<LST>` and `<ITM>` tags.

  * **Consistency:** Do not manually type paragraph numbers – always use the tags so that if something is added or deleted, SpecsIntact will renumber automatically. Also, do not use Word’s auto-numbering outside of SpecsIntact; those won’t translate to the .SEC file.
  * The numbering format should remain **fully numeric down to the third level** (as recommended) with titles, and fourth level could either continue numeric or switch to letters depending on the context (per CSI format). The example in Table A-1 shows numbering to 1.1.1.1 (fourth level) with a title, then examples of a., (1), (a), 1. etc., for list subdivisions. In practice:

    * Use actual paragraph numbers for any substantive paragraphs.
    * Use **lists** for minor enumerations within a paragraph (so if you need to list a series of requirements or options, use SpecsIntact list tags which will give you a., b., c. or 1), 2), 3) as appropriate).
    * Avoid going past the sixth sublevel – SpecsIntact supports up to six levels of paragraph numbering, which should be plenty. If you find a need beyond that, restructure.
* **Headers/Footers and Section Banner:** Each UFGS section will have a “section header” (also called a **banner**) at the top of the first page that includes identification info: which agencies approved it, the section number and title, the date (and change number if any), and the preparing activity. SpecsIntact helps populate this when you fill in the project database. The UFC’s modifications section (2-5) details how changes and revisions are to be indicated in that banner. Key points:

  * The banner lists the agencies (USACE, NAVFAC, AFCEC, NASA) involved, the UFGS number and title with the original approval date, and below that a line for Change or Revision information.
  * If a Change has been issued, it might say “Change 2 – 08/16” (meaning Change 2, August 2016) on the banner.
  * If the section supersedes an older section number, that is indicated as well (Superseding XYZ...).
  * In the footer of each subsequent page, typically the section number and page number appear (e.g., “01 33 00 - 5” for page 5 of section 01 33 00).
  * As a spec writer, you normally won’t edit the banner except to update the date or change as directed by the UFGS program (the **Database Managers** for UFGS handle official changes in the master library).
* **Footer Notes for Classified sections:** (Though not common, if a section were classified or CUI, special markings would be needed, but usually such content isn’t in UFGS. If it were, follow DoD marking guidance per DODI 5200.48 for CUI or classification on each page. The UFC mentions CUI handling under publication.)

**2.6.2 Section and Paragraph Numbering:**

* As discussed, UFGS sections use MasterFormat numbers (6 digits plus optional extension). Ensure the **section number and title** in the header are correct and match the content. If a master spec is repurposed or split, the numbers must be adjusted accordingly. Do not arbitrarily change section numbers; they are assigned and listed in the index of UFGS on WBDG.
* Within the section, the **paragraph numbering hierarchy** should strictly follow the prescribed format:

  * Part numbers are roman-numeral or just named (Part 1, Part 2, Part 3).
  * First-level paragraphs within Parts are numbered `1.1, 1.2, 1.3, ...` (the first digit matches the part number; e.g., 1.X are in Part 1).
  * Second-level are `1.1.1, 1.1.2, ...`, third-level `1.1.1.1, ...`. Typically, three levels of numbering with titles are sufficient for most content.
  * If further breakdown is needed under a third-level, usually bullet or lettered lists are used rather than a `1.1.1.1.1`. However, some specs do go to four levels of numbers for clarity, which is acceptable, but anything deeper turns into outlines of a), (1), etc. as noted.
* **Paragraph Titles:** Every numbered paragraph should have a descriptive title (except maybe low-level list items). For example, “3.2.1 **Surface Preparation**” or “2.1 **Materials**”. According to UFC:

  * The **first-level subparts (Articles)** in each part should be titled in **ALL CAPS** (or Title Case but bold) as per SectionFormat – however, the UFC text suggests uppercase for the first level and title case for lower levels. In practice, current UFGS use Title Case for all paragraph titles, not full caps (the PART headings are caps, but article titles are often Title Case). The key is consistency within a section.
  * Example given: *“2-2.4 Subpart Titles. Each numbered subpart must have a title; uppercase for the first level (ARTICLE) and title case for lower level subparts as shown above.”*. This indicates: Part headings like “PART 1 GENERAL” are caps; an Article like “1.1 ARTICLE” might be caps, then “1.1.1 Paragraph” in Title Case. However, current practice has evolved and one should follow the prevailing style in recent UFGS (which generally use Title Case for article titles).
  * **Untitled Paragraphs:** The guidance says use no more than two untitled paragraphs in a row. This typically applies to short paragraphs that continue directly under a heading. It’s best to avoid having multiple paragraphs under one heading without sub-headings; if you have more than one, consider whether they need their own title or could be combined. Usually, an untitled paragraph is just the text immediately following a heading – if more follow, either number them or make them a list.
* **Lists and indentations:** Use lists (with bullets or letters) for enumerations instead of burying them in a sentence. SpecsIntact `<LST>` tags will handle the indentation and lettering (e.g., a., b., c. or 1., 2., 3.). There are different list styles; follow CSI:

  * Main body numbered paragraphs use Arabic numerals.
  * First indent list uses lowercase letters (a., b., c.),
  * Next indent uses numbers (1), 2), 3)),
  * Next uses lowercase roman ((a), (b)), etc.,
  * This resets as you exit levels. The example in Appendix A-1 shows this progression.
  * Provide a hanging indent such that multi-line text under a list item aligns after the bullet/number (SpecsIntact does this automatically with `<LST INDENT=-0.33>` for example).
* **“Not Used” text:** As mentioned, if an entire Part or a major article is not applicable, mark it “Not Used.” E.g., if Part 4 or Part 5 existed but are not used, state “PART 4 NOT USED” or similar at that location. But normally, UFGS sections do not have Part 4 or 5; they stop at 3.
* **Spacing and Pagination:** Start each Part on a new page if possible (SpecsIntact can insert page breaks before “PART 2” and “PART 3”). This isn’t strictly required but is neat. Ensure there’s a blank line before and after major headings in the source to improve readability.
* **Example numbering** (from Table A-1 in Appendix A) for clarity:

  * PART 1 GENERAL
    1.1 **SUMMARY** (this could be an article title in caps or title case)
    1.1.1 **Related Requirements** (first subparagraph)
    1.1.2 **References**
    1.1.3 **Submittals**
    1.2 **QUALITY ASSURANCE**
    1.2.1 **Installer Qualifications**
    1.2.2 **Field Samples**
    a. Example (list item under 1.2.2)
    b. Example
    (1) Example (sub-list under list item b)
    (2) Example
    1.3 **DELIVERY, STORAGE, AND HANDLING**
    *(...and so on...)*
    The above shows hierarchical numbering. Use the template to avoid manual errors here.

**2.6.3 Subpart Titles:** *(Note: “Subpart” here refers to any subsection or paragraph heading in the spec.)* As already noted, every numbered paragraph level in UFGS should have a title that describes its content. This improves navigation and reduces ambiguity.

* **First-level headings** (the articles directly under Parts) should be short nouns or noun phrases (often the CSI standard titles). Examples: **REFERENCES**, **SUBMITTALS**, **QUALITY ASSURANCE**, **MATERIALS**, **INSTALLATION**, **FIELD QUALITY CONTROL**. These are often in Title Case or ALL CAPS depending on style (the UFC suggests uppercase for first level).
* **Second and third-level headings** should further narrow the topic. For instance, under **Quality Assurance** you might have “Qualifications” or “Mockups” or “Pre-Installation Meeting.” Under **Materials** you might have headings for each type of material (e.g., **Cement**, **Aggregates**, **Admixtures** in a concrete spec).
* **Case Convention:** The UFC text example implies: ARTICLE titles (first-level under part) uppercase; lower-level titles in Title Case (first letter of each major word capitalized). In actual UFGS documents, you’ll see Title Case used at all levels with bold text. Follow the current convention found in the UFGS masters. The main point is to use consistent capitalization for similar levels.
* Do not leave a heading number with no title. It is never “1.2.3 – \[blank]”. If something doesn’t warrant a title, it likely should be part of the parent paragraph’s text or a list, not a separate numbered item.
* The only place without titles might be unnumbered list items or very short subparagraphs that continue directly from a lead-in sentence. But even then, better practice is to incorporate any requirement into a structured list or paragraph with a clear lead-in.

**2.6.4 “Notes to the Designer” Usage:** In UFGS masters, **Notes to the Designer** (sometimes called “Editor’s notes” or just “Notes”) are crucial for guiding how to tailor the spec for a project.

* These notes are **not meant to be in the final contract spec**; they are there to assist the person editing the master spec. They often explain choices to be made or criteria for including/excluding something.
* Format: In SpecsIntact, such notes are typically enclosed in special tags (like `<NOTE>` or as hidden text). When printed in draft form, they might appear in italics or a different color, and often enclosed in brackets or starting with “NOTE:”. Example from the UFC: *“Notes provide directions and criteria for the designer to choose options and alternatives... Provide notes between the subpart title and text paragraph to indicate when to use the paragraph, how to choose bracketed items, and what tailoring tags are in the text.”*. This exactly describes how to position notes: a note can go immediately under a heading, before the actual spec text, so the project editor knows how to deal with that section.
* **What to include in Notes:** Guidance on:

  * When to include or exclude a paragraph (e.g., *“(Note: Include the following paragraph only for Air Force projects.)”*).
  * How to select bracketed options (e.g., *“(Note: Choose coating type A for mild environments and type B for coastal environments.)”*).
  * Where to find additional info (e.g., *“(Note: Designer to obtain wind load data from project drawings to insert below.)”*).
  * Do not put essential technical requirements in notes; notes are removed for final issue, so anything mandatory must be in the main text or an option that will be turned on.
* **Tailoring Notes:** If a note itself should only be shown under certain tailoring (like service-specific), it can be placed within a tailoring tag so that it only appears when that option is active. The UFC mention: *“Provide the note itself within tailoring tags if the note only applies if the tailoring option is selected; thus, the note will be deleted if the tailoring option is not selected.”*. For example, if a spec has tailoring for Army vs Navy differences, you might put a note for Army editors and wrap it in the Army tailoring tags so that if someone prints the Navy version, that note isn’t shown.
* **Removal:** When preparing the final spec for a project, SpecsIntact has a function to strip out all these notes (or you manually mark them to not print). The end result is that contractors never see them. As a UFGS writer, double-check that nothing critical is left only in a note.
* **Keep Notes Updated:** If criteria change or options change, update the notes accordingly. Sometimes notes lag behind spec changes, causing confusion. For instance, if a new material option is added to the text but the Note still says “choose between two options” (when now there are three), that needs fixing.
* Do not overuse notes. If something can be made obvious through the text itself (like bracketed choices which are self-explanatory), a note may be unnecessary. But err on the side of clarity for the editor.

**2.6.5 Units of Measure (English/Metric):** DoD uses dual units in its guide specifications to accommodate both metric (SI) and US customary units.

* **Dual-unit Presentation:** For UFGS masters, provide measurements in both **Metric (SI)** and **English (Imperial)** units, with **Metric units listed first** followed by the English in parentheses or in separate tags. The UFC gives a specific format: *“...text<MET> 50 mm</MET><ENG> 2 inches</ENG> text;”*. In practice, SpecsIntact handles this with `<MET>` and `<ENG>` tags around the respective values. When printed, it can show either both or only one set depending on project settings.

  * For example, a requirement might read: *“Provide conduit of diameter not less than <MET>25 mm</MET><ENG>1 inch</ENG>.”* In the master file, both are present with tags. A project spec can be set to metric or English output; SpecsIntact can print both (which might show as “25 mm (1 inch)”) or only one system if desired.
* **Spacing and Format:** Note the formatting: no space before the first unit within the tags, a space before the unit abbreviation if needed, and no duplicate punctuation. The UFC example shows no extra spaces around the tags except a space separating the value and unit. Follow the example precisely so that when rendered it looks correct. E.g., in `<MET>50 mm</MET><ENG>2 inches</ENG>`, SpecsIntact might output "50 mm (2 inches)" automatically.
* **Conversion standards:** Convert units in accordance with [IEEE/ASTM SI 10](https://www.nist.gov/pml/us-japan-technical-exchange-program/si10-american-national-standard-metric-practice) (the standard for metric practice) or other relevant guidance. Use sensible rounding so that the converted values are practically equivalent. Avoid showing an excessive number of significant figures – round to an appropriate precision. For example, if the metric design is 10 mm, the inch equivalent should be 3/8 inch (approx 9.5 mm) if that’s a standard value, rather than 0.39 inch.
* **No Parentheses for Dual Units:** The UFC specifically says not to use parentheses to show dual units in the master text. Instead, use the <MET> and <ENG> tags. The output might include parentheses depending on the SpecsIntact style, but you as a writer just input via tags. If writing outside SpecsIntact (like an illustrative document), you might use parentheses for clarity, but in the actual spec file, rely on tags.
* **Project Unit Selection:** For actual project specs, the designer will decide whether the job will use metric or US units (or both). The UFC note: *“For projects, select either English or Metric units when setting up the Job.”*. In the SpecsIntact project settings, one can choose the output units. If metric project, it will either show metric with English in parentheses or metric only. If English project, it can show English with metric in parentheses or English only. The master provides both, so it’s adaptable.
* **Do Not Mix Unit Systems in Requirements:** Each requirement should be clear in one unit or both consistently. Don’t have some values only in mm and others only in inches in the same spec unless it's done systematically (like maybe metric for some products and inch for trade sizes – but even then, normally both given). Consistency avoids errors.
* **Example Implementation:** If a spec says *“Maintain a temperature of 21 °C (<MET>21 °C</MET><ENG>70 °F</ENG>) in the room.”* That ensures both 21 degrees Celsius and 70 degrees Fahrenheit are conveyed. The project can then output whichever needed. If one output, no parenthetical is needed; if both, one may be in parentheses as formatted by the software.

Following the above ensures compliance with DoD metric policy (which is essentially to design in SI but accommodate US customary usage).

**2.7 Referenced Standards and Cross-References:**

**2.7.1 Listing Reference Publications (REFERENCES section):** Each UFGS section typically begins Part 1 with an article titled **REFERENCES** (usually paragraph 1.x). This article lists all the external documents (industry standards, codes, etc.) that are cited in the text of that spec section. Key guidelines:

* **Completeness:** Ensure every standard, code, UFC, UFGS, manual, or regulation that you refer to in the spec text is listed under REFERENCES. Conversely, do not list documents that are not actually cited. This helps the contractor know what resources are relevant and prevents confusion.
* **Format:** In the References article, list documents by identifier (like ASTM, ANSI, etc.) typically in alphanumeric order by their designation. The UFC example shows the references in a bulleted list format in the text, but in final formatting it may appear as an indented list or paragraph style. E.g.:

  * ASTM SI 10, *American National Standard for Metric Practice*
  * ISO 9223, *Corrosivity of Atmospheres – Classification, Determination, and Estimation*
  * DoD Directive 4270.5, *Military Construction, 5 February 2005*
  * MIL-STD-3007, *Department of Defense Standard Practice: Unified Facilities Criteria and Unified Facilities Guide Specifications*
  * MasterFormat® (Latest Edition), *Master List of Numbers & Titles for the Construction Industry*
  * SectionFormat™/PageFormat™, *CSI’s Recommended Format for Construction Specifications Sections*
    *(These are examples extracted from the UFC snippet【28†L321-L329}.)*
* **Reference Identifier (RID):** In SpecsIntact, each reference is assigned an identifier (often the acronym of the organization or a shorthand) that is used in the spec text. For instance, if you have ASTM C150 referenced, “ASTM C150” in the text is tagged to link to the full citation in the References list. This identifier is often just the standard designation itself. The UFC states: *“In the UFGS, the reference identifier (RID) for the reference must appear and be tagged in the reference paragraph and at all occurrences in the text using the SpecsIntact software.”*. That means:

  * When you list a reference in the References article, you wrap it in <REF> tags with an identifier.
  * When you mention it in the text (e.g., “Comply with **ASTM C150** for cement”), you also tag that as a reference to connect to the list. SpecsIntact will handle updating the reference list or flagging if a reference is listed but not used or vice versa.
* **UMRL Compliance:** Use the official acronyms/names as in the UMRL. For instance, use “ANSI/AWC NDS” or “ACI 318” exactly as standardized. If a standard is from an organization not in the UMRL, coordinate to add it or at least be consistent with similar UFGS usage.
* **Edition/Date of Standards:** The UFGS policy generally is to not include specific years for standards in the spec text itself (to allow using the latest), but the References list may include the version if needed. Actually, the UFC suggests listing with latest version implied, but also provides guidance in 2-7.4 (Reference Dates and Titles) on how to handle revision years. Many UFGS simply list standards without date, assuming the latest edition at contract award applies. Others list a specific year to lock it in. Follow agency policy – often, the UMRL is configured such that references are listed without year unless otherwise noted.
* **Whole Section vs. Partial Reference:** Always reference the entire standard by its designation/title, not a subsection of it. In the text, you might cite a section (e.g., “Test per ASTM E119, Section 11”), but still the References entry is just ASTM E119 (whole standard).
* **No project-specific references in master:** Master UFGS should stick to commonly applicable references. Don’t include references that would only apply to a specific location or project (those should be added by the project editor if needed). Masters focus on industry standards and DoD criteria that broadly apply.

**2.7.2 Citing Standards Organizations (Standards Orgs Acronyms):** When referencing standards in the text, identify the issuing organization by its accepted acronym per the UMRL:

* Use acronyms like **ASTM**, **ISO**, **ACI**, **IEEE** etc., instead of writing out the full name each time (after the first explanation if needed). The References list or glossary can clarify acronyms if needed.
* The UFC warns about **conflicting acronyms**: If two organizations have similar acronyms or if a single standard is co-issued by two bodies (like ANSI/IEEE), how to handle it? The guidance: *“Where dual acronyms may be used to identify the standards-producing organization and an underwriting organization... use the issuing organization only.”*. For example, a standard might be ANSI/IEEE 123. If IEEE is the actual maintainer, just call it IEEE 123 and list IEEE in references. The reference ID should be the primary one (IEEE in this case). The idea is not to confuse by listing both “ANSI” and “IEEE” for the same standard in the spec text.
* If a standard doesn’t have a readily known acronym, you may create a short one in the reference list and use it consistently (the SpecsIntact UMRL usually assigns something).
* If an acronym isn’t in UMRL and you introduce it, inform the Database Manager so it can be added to avoid future duplication under different acronyms.
* **Acronym Case:** Use the exact case as per standard naming (most are uppercase). For example, use “NAVFAC” not “NavFac”, “AFI” for Air Force Instruction, etc.

**2.7.3 Federal Acquisition Regulation (FAR) Clauses in Specs:**

* The general rule: **avoid referencing FAR clauses in UFGS** unless absolutely necessary. FAR and DFARS clauses belong in the contract’s Section 00700 General Provisions or Section 00800 Special Provisions, not usually in technical specs (Divisions 01-48). UFGS are Division 01-48 technical specs.
* If there is a procurement requirement that must be in the spec and it overlaps with a FAR clause, often the FAR clause will take precedence contractually, and duplicating it in the spec could cause conflicts. So UFGS authors should steer clear of including things like “The contractor is entitled to XYZ as per FAR 52.xxxx” in the spec.
* However, sometimes to enforce a certain practice, referencing a clause is needed (especially for "Brand Name or Equal"):

  * The UFC specifically addresses **“Brand Name or Equal”** usage: If you ever specify a brand name followed by “or equal,” by regulation you must include FAR 52.211-6 in the solicitation. Rather than the spec writer including the clause text, the spec just should note the requirement that if brand name or equal is used, the clause is invoked. But typically, contracting will handle that. So the UFC says: use the phrase "brand name or equal" only if approved, and do **not** include the FAR clause text in the spec; just use the phrase, and contract specialists will know to include FAR 52.211-6 in the contract.
* If a FAR clause **must** be referenced:

  * Mention it by number and title in the text (in Title Case). E.g., “According to FAR clause 52.236-5 **Material and Workmanship**,...”. Do not quote the clause content; just reference it.
  * Do not include the date of the FAR clause in the reference (FAR clauses change over time but the contract will attach the correct version date).
  * Do not list FAR clauses in the REFERENCES paragraph of a UFGS. Those clauses are part of the contract’s legal texts, not technical reference standards. The UFC explicitly says not to include FAR clauses in the References list.
  * Double-check with contracting: often if a technical spec is trying to enforce something that’s actually a contractual issue, it’s better handled by a contract clause or Section 00800 special provision. For example, warranty terms or govt-furnished property should be in the contract conditions, not in UFGS (except to specify technical aspects).
* The UFC provides **Examples** of how to name FAR clauses if needed:

  * FAR 52.243-4 **Changes**
  * FAR 52.236-2 **Differing Site Conditions**
    That shows the format: Clause number and short title in Title Case.
* **Verify Titles:** If you do mention a clause, ensure the title is exactly as in FAR and current. Acquisition.gov is the resource to verify FAR clause titles and text. The UFC reminds to verify FAR titles at acquisition.gov.
* Ideally, avoid it altogether. If the spec needs a certain contractual enforcement, maybe instead instruct the project team to include a proper section in Division 01 or rely on FAR. Keep technical specs focused on materials and workmanship, not contract terms.

**2.7.4 Reference Dates and Titles:**

* The UFC advises using the **most current version of referenced standards** in UFGS, unless there is a specific reason to use an older version. So, masters should be periodically updated to reflect new editions of standards (the tri-service committees do this through CCRs).
* In the References section listing, the format often is *Standard Number – Title – (sometimes date or edition)*. The UFC suggests including the year of publication in parentheses after the title, which can help identify edition. However, some agencies prefer no year to always mean “latest.” This is a policy choice. The UFC instructs on how to handle when multiple revisions exist:

  * If you need to refer to a specific edition, include the year and any change/revision info. For example: *“UFGS 08 34 73 (November 2009)”* which might be shown in a revision history. For industry standards: *“ACI 318-14”* could be referenced as such if needed. Otherwise, saying “ACI 318” implies latest.
  * They give a method to show revisions: e.g., *“2009; R 2010; C 2011; errata 2012”* to indicate original 2009, revision in 2010, change in 2011, errata in 2012. This level of detail likely is too much for a spec references list; it sounds more like an internal tracking. Possibly this was guidance for how to notate if you explicitly mention a specific revision in the text (but typically, one wouldn’t).
* **In-Text Reference to Versions:** Generally, you would not mention version years in the spec text, just the standard ID. If there’s a critical need (like requiring a particular edition because a newer one is not acceptable yet), clarify in the text or a note. But masters usually follow latest.
* **Use of UMRL Tools:** The **Unified Master Reference List (UMRL)** and SpecsIntact can automatically update references if a newer version is available (if the UMRL is updated). As a spec writer, ensure the references in your section are up to date in the UMRL. For example, if ASTM renumbered or changed a title, update it. The UFC encourages using the UMRL and SpecsIntact’s automated features to manage updates to standards.
* **Minimize text from standards:** Rather than incorporating large excerpts from standards (which then might need updating if the standard changes), rely on the standards themselves as much as possible. The UFC notes to use industry reference standards to the maximum extent to reduce lengthy spec text. E.g., don’t rewrite the entire ASTM test procedure in your spec – just say “Test in accordance with ASTM X”.
* If a standard is obsolete or replaced, update the reference. If a standard is superseded by another (e.g., a federal spec replaced by ASTM), change the text accordingly.

**2.7.5 Quoting vs. Referencing Standards:**

* **Don’t quote large portions** of reference standards in the UFGS text unless absolutely necessary. If you quote or paraphrase too much, you run the risk of creating discrepancies or having outdated info when the standard updates. It can also violate copyright if done excessively. Instead, incorporate by reference. Only reiterate key points if needed for clarity.
* The UFC says: *“Do not quote or repeat portions of the referenced standard in the text of the guide specifications unless it is necessary to improve clarity and readability.”*. That’s straightforward: rely on the standard, except maybe to summarize a requirement or highlight something crucial the contractor must do, especially if the standard’s requirement might be overlooked or if you need to emphasize it.
* If you find yourself needing to include significant text from a standard:

  * Check if the standard is freely accessible (many are not). If not, better to keep it minimal to avoid copyright issues.
  * Consider if that standard is actually appropriate or if you should just specify the requirement directly in your own words (thus making it a project requirement not just a referenced one).
  * Possibly add a note in the spec referencing that section of the standard rather than copying it.
* **Example:** Instead of quoting OSHA regulations on scaffolding in a spec, just say “Comply with OSHA requirements for scaffolding (29 CFR...).” One might only detail additional requirements not in OSHA or emphasize something like “Scaffolds shall be capable of supporting at least 4 times the max intended load (per OSHA).”
* Another case: If the project needed a specific part of a standard, e.g., a particular table or figure, it might be tempting to include it. It’s usually better to reference the standard and have the contractor obtain it. Or provide the values from the table in your own table citing the source, if it’s really necessary to include (ensuring credit).

**2.7.6 Cross-References to Other Sections:**

* Avoid arbitrary cross-references between spec sections, as renumbering or spec shuffling can cause errors. The UFC specifically advises against referencing other sections or paragraphs unless necessary.
* If you must refer to another specification section within a UFGS:

  * Refer by **section number and title**, not just section number. For example: *“Section 09 90 00 **Paints and Coatings**”* instead of just “Section 09900”. This is because some projects might renumber or because clarity is improved with title (and it avoids confusion if section numbers change in future MasterFormat updates). SpecsIntact has tags `<SRF>` for cross-section references where you can input the section number and title so it prints nicely.
  * Do not refer to specific paragraph numbers of another section, because if that other section is edited, the paragraph numbers might change. Instead, refer generally by subject. For example: *“Concrete work is specified in Section 03 30 00 **Cast-in-Place Concrete**.”* If you need something specific, refer by article name: *“…as described under **Finishing** in Section 03 30 00.”* Paragraph titles are less likely to change than numbers.
* The format recommended: *“Section <SRF>01 33 00</SRF> **SUBMITTAL PROCEDURES**”* etc., with the title in caps. The UFC snippet shows format like `<SRF>01 23 40</SRF> MISCELLANEOUS (where MISCELLANEOUS is the full section title)`.
* When referencing a paragraph within the **same** section (like “as specified in paragraph 3.2 of this section”), don’t use the number. The UFC suggests referencing by paragraph title instead. E.g., say *“...as specified under **EQUIPMENT** in Part 3 of this section.”* or *“See requirements in article **Field Quality Control** below.”* This is because if you insert a new paragraph 3.1 later, the numbering shifts. Paragraph titles remain the same, so saying “Equipment” will still point to that content.
* **Automatic Renumbering:** If cross-references are tagged properly in SpecsIntact, they can update if section numbers change. But SpecsIntact can’t update a paragraph number reference inside text easily. Better to avoid mentioning specific numbers as text.
* **Minimize cross-section dependencies:** The goal is that each spec section stands alone as much as possible, except for broad references. If the sections have interrelated requirements, often that’s handled in Division 01 (e.g., Section 01 14 00 Work Restrictions might outline who does what if two trades overlap).
* If cross-reference is used, double-check in final project manual that the referenced section exists and titles match. Broken references cause confusion for contractors.

**2.8 Tailoring Options in UFGS:**

“Tailoring” in UFGS refers to built-in choices that can be toggled on or off to suit specific agency requirements or project conditions. This is implemented via SpecsIntact’s tailoring tags `<TAI>` (Tailoring options).

* **Tailoring vs. Bracketing:** Tailoring is used for larger blocks of text that apply only to certain scenarios (often service-specific or contract-type specific requirements), whereas brackets \[ ] are used for smaller optional words/phrases choices. Tailoring is like an on/off switch for chunks of content.
* The UFC describes tailoring as **pre-editing of information** such as materials, methods, or regional requirements, by turning options on or off before producing the project spec. This reduces editing time because irrelevant content can be globally excluded.

**2.8.1 Service-Specific Tailoring:**

* Many UFGS sections include paragraphs that are only needed by one service. For example, the Army might have an additional testing requirement or the Navy might have a different submittal process. Instead of maintaining separate UFGS, the differences are integrated and marked.
* In the SpecsIntact master, these are marked with a code like `TAI OPT=ARMY` or `OPT=NAVY` etc., around the text that is only for that service. When generating a project specification, the spec editor will set which service’s options to include. The UFC guidance:

  * *“Master UFGS writers must reconcile agency differences to the greatest extent possible to avoid needing service-specific paragraphs.”*. That means unify requirements if you can. But if something truly differs (like Army has one approach, Navy another), use tailoring.
  * If more than one service-specific variation is required in a spec, prefer to use the tailoring mechanism rather than creating separate paragraphs for each service in the same doc (which could confuse a project editor). Tailoring cleanly separates them.
  * For example, you might have: `<TAI OPT=ARMY>Paragraph text that only Army needs.</TAI>` and `<TAI OPT=NAVY>Paragraph text that only Navy needs.</TAI>`. When preparing an Army project spec, you select "ARMY" and the Navy text will be left out, and vice versa.
* **No Double Method:** The UFC specifically cautions: *“Do not use both tailoring and bracketed paragraphs for a particular DoD Service’s requirements within one specification.”*. That means if you have something that is only for Army, don’t both bracket it and tailor it. Use one method. Typically, you’d just tailor it for Army so it doesn’t appear at all in Navy/Air Force specs. Brackets are more for technical options (like \[steel] or \[aluminum]), not for service distinctions.
* **Notes to Designer with Tailoring:** As noted, if tailoring is used, include a note that explains what the tailoring does (like “(Army only)” or “(Navy only)”) and ensure the note itself is tailored to show up only for the relevant service so other service editors aren’t distracted by irrelevant notes.
* **Example of Service Tailoring Implementation:** Suppose a concrete spec has an additional submittal required by the Air Force but not by Army or Navy. The master might have:

  * *Submittals:* under that list, an entry `<TAI OPT=AF>G. Air Force Only special submittal of XYZ</TAI>` with a note for the editor. When an Army or Navy spec is printed, that submittal line is omitted entirely.
* The result is a single UFGS that can produce three slightly different specs depending on service, without cluttering each other’s version.
* The UFC note says *“In most cases when more than one Service-specific paragraph is required, incorporate Service-specific tailoring. In most cases:”* then provides guidelines (which we cover below as bullets that were in text):

  * **Guideline 1:** *“Do not use both tailoring and bracketed paragraphs for a particular DoD Service’s requirements within one specification.”* (We already explained this.)
  * **Guideline 2:** *“Along with tailoring, provide a Note to the Designer to indicate what tailoring is in the text and the criteria for choosing the tailored option.”* – So yes, label the sections internally so the editor isn’t guessing.
  * **Guideline 3:** *“For clarity in viewing a UFGS in a format other than SpecsIntact, provide tailored items as part of a complete sentence, rather than items within a sentence.”*. This is important: it’s basically saying when writing optional text, write it as whole sentences or paragraphs that can be turned on/off, rather than peppering optional words mid-sentence. Because if someone looks at the spec outside of SpecsIntact (like a plain PDF of the whole master with all options shown), it gets confusing. They even give an example:

    * Good: *“<TAI OPT>Use galvanized steel.</TAI> <TAI OPT>Use stainless steel.</TAI>”* – here two complete sentences are optional; one might be included or the other.
    * Bad: *“Use <TAI OPT>galvanized </TAI><TAI>stainless </TAI>steel.”* – this tries to toggle words within one sentence which is much harder to read and manage.
  * So, the master spec should be written so that if an option is off, the sentence still reads correctly. If including both in one sentence, ensure one is entirely inside a tailoring block and the other outside, so one path yields a full coherent sentence. Usually, it’s clearer to separate into two sentences or two bullets with tailoring.
* **Summary:** Use tailoring to manage service differences, keep them separate and well-documented, and avoid mixing them with other optional mechanisms for the same content.

**2.8.2 Design-Build vs. Design-Bid-Build Tailoring:**

* Some UFGS are used in both **Design-Bid-Build (DBB)** and **Design-Build (DB)** projects, but the requirements might differ slightly. For instance, in a design-build scenario, the spec might require the contractor (who is also the designer) to submit design calculations or engage a registered design professional for certain aspects, which wouldn’t apply in a design-bid-build scenario where the design is already complete.
* The UFC indicates that masters may include tailoring options for DB vs. DBB, in addition to service-specific ones. It says: *“Ensure that design-only requirements for design-build projects are captured in tailoring tags. Use these tailoring options to distinguish between Design-Build versus Design-Bid-Build requirements that are service-specific.”*.
* So, typically there might be options like `<TAI OPT=DB>` and `<TAI OPT=DBB>` or similar. Alternatively, they might use one set of tags indicating design-build only content.
* The UFC provides a list of example tailoring labels for DB or DBB by service:

  * Air Force Design-Build
  * Air Force Design-Bid-Build
  * Army Design-Build
  * Army Design-Bid-Build
  * Navy Design-Build
  * Navy Design-Bid-Build
    These appear as bullet points in the UFC text, suggesting that in the SpecsIntact tailoring setup, there are distinct combinations (like an option that’s active if both “Air Force” and “Design-Build” are selected). Possibly the master has combined tailoring flags, e.g., `OPT=AF-DB` or nested tailoring `<TAI OPT=AF><TAI OPT=DB> ... </TAI></TAI>`.
* The intent is that an editor setting up a project in SpecsIntact can choose both their service and the project delivery method, and the spec will include the correct pieces. For example, if it’s an Army Design-Build project, certain paragraphs (like those instructing the contractor to submit design documents or to follow certain UFC design criteria) will appear, whereas in an Army Design-Bid-Build project those paragraphs wouldn’t be needed.
* The UFC snippet suggests using “generic” DB/DBB options for things that apply to all services\*\* if\*\* design-build or design-bid-build:

  * *“Use the following where requirements apply to all Services: – Design-Build – Design-Bid-Build”*. This implies that some tailoring can be broad (not service-specific) if something is needed in all design-build projects regardless of service.
  * Perhaps an example: a note “(This section is intended for Design-Bid-Build projects. For Design-Build, see UFGS X or adjust accordingly)” and the tailoring might exclude the entire section for design-build.
* This is a complex area; not all UFGS masters incorporate DB vs DBB tailoring – some agencies instead publish separate guide specs or have notes telling the spec editor how to modify for DB. But UFC 1-300-02 encourages the use of tailoring to handle it within one master when feasible.
* **Design-Build Submittals:** The next item (2.8.3 below) actually continues the topic, focusing on submittal codes (D, C, R, A) which specifically relate to design-build scenarios. We’ll cover that under submittals in 2.9.7.

The bottom line: if the spec needs to have alternative text depending on whether the contractor is also the designer, implement that with tailoring options (and clearly label them). For instance, a part of the spec might say:

* `<TAI OPT=DB>Design Analysis: The Contractor (Designer) shall submit a design analysis in accordance with ...</TAI>` – which would only show up for DB projects.

* `<TAI OPT=DBB> (empty) </TAI>` – nothing needed in DBB because the government provided design.

**2.9 Language and Style Conventions:**

*(This section consolidates the “Writing Style” guidance from UFC 1-300-02, much of which we touched in the Executive Summary, but we’ll enumerate as per the TOC items 2.9.1 through 2.9.10 for completeness.)*

**2.9.1 Voice, Mood, and Tense:**

* **Imperative Voice:** UFGS are written as instructions to the contractor, so use the imperative mood for action statements whenever possible (e.g., “Provide X,” “Install Y,” “Test Z”). Do **not** write “The Contractor shall...” – just say what must be done. For example, instead of “The Contractor shall paint all metal surfaces,” write **“Paint all metal surfaces.”** This is understood to be directed to the contractor. UFC 1-300-02 explicitly states not to use “the Contractor shall” in specs.
* **“Shall” vs “Must” vs “Will”:** The document advises to avoid “shall” where possible:

  * Use **“must”** if a mandatory requirement needs emphasis and rewriting in imperative isn’t suitable (UFGS masters rarely use “must,” they typically stick to imperative or “shall” in passive contexts). But the UFC says if use of "shall" cannot be avoided, use "must" instead. This is possibly to align with plain language preferences (some agencies consider “shall” ambiguous).
  * Use **“will”** for actions performed by the Government or a third party (e.g., *“The Government **will** perform quality assurance testing.”* or *“Concrete mix **will** be provided by \[Government]\[Contractor] as indicated”* – but careful, if by contractor, use imperative or “shall” structure).
  * **“May”** is used only for permissive or optional actions **by the Government** (or to indicate options given to the contractor at their discretion, though usually better to specify choices rather than leave “may”). “May” in specs is generally avoided except in context “Contracting Officer may direct X”.
  * **“Should”** is generally not used in specifications because it implies a recommendation, not a requirement. If something is desirable but not mandatory, either make it mandatory or omit it (or put it in a note or guidance document).
* **Present Tense Descriptions:** Often specs describe attributes in present tense, e.g., “Pump is UL-listed” rather than “shall be UL-listed.” This is acceptable as long as clarity is maintained.
* **Consistency:** Don’t mix “shall” and imperative for the same subject. UFGS largely stick to imperative. Some older specs or specific sections might use “shall” for passive requirements (like “Concrete **shall be** proportioned...” where the actor isn’t stated). If writing new content, prefer active voice or restructure to avoid unnecessary “shall be” statements.
* **Examples (from UFC text):**

  * Incorrect: “the Contractor shall submit shop drawings.” Correct: **“Submit shop drawings.”**
  * Avoid “Provide X in accordance with Y” – better: **“Provide X per \[standard name].”** (Imperative and concise.)
  * *“Specify execution of alternatives with guidance.”* – Possibly meaning, if giving options, present them clearly with guidelines.
* **Speak only to Contractor:** Do not address subcontractors, manufacturers, or others directly. The contract is with the Contractor, so everything flows through them. E.g., do not say “Manufacturer shall provide warranty...” say **“Provide manufacturer’s warranty...”** which implies Contractor ensures that happens.
* **No instructions to Govt:** Don’t write things instructing the Contracting Officer or Government project manager in the spec. For example, don’t include “The Contracting Officer will approve the color before application” in the technical spec – if a submittal is required, just list the submittal and indicate if it’s for approval (that implicitly involves the Contracting Officer’s action). If needed, use passive voice: “Color shall be approved by the Contracting Officer.” But typically this is handled by submittal procedures generically.
* The UFC note: *“Do not use the specification to instruct the Contracting Officer.”*. Keep roles clear: specs instruct the contractor on what to do; contract clauses and Division 01 sections instruct how Government will administer.
* **Furnish/Install:** The term **“provide”** is preferred to cover “furnish and install”. The UFC explicitly says: do not use “furnish” if it’s meant to include installation. Use “provide” to mean supply and put in place. Only use “furnish” if you mean supply only (not installed). So:

  * “Furnish” = supply to site (someone else might install),
  * “Install” = put in place (someone else might supply),
  * **“Provide”** = furnish and install (the whole thing, which is usually what we want).
* **Per vs. In accordance with:** Don’t use “per” to mean “according to.” Write out **“in accordance with”** for clarity. E.g., “in accordance with \[standard]” not “per \[standard]”.
* **Example from UFC text about “shall” usage:** *“Avoid use of 'shall' and 'must'; if use cannot be avoided, use 'must' instead of 'shall' unless it changes the meaning of the sentence.”*. So they strongly dislike “shall.” Many UFGS still contain “shall” (especially older ones), but new guidance is to minimize it. In any case, do not overuse these modal verbs.

**2.9.2 Abbreviations and Acronyms:**

* **Introduce Once:** Spell out each abbreviation or acronym the **first time** it appears in the section, followed by the abbreviation in parentheses. After that, use the acronym. For example: “High-Efficiency Particulate Air (HEPA) filter” on first use, then just “HEPA filter.”
* **Follow Discipline Practice:** Certain disciplines have common abbreviations that everyone in that field knows (like HVAC, LED, psi). Use them but still introduce them once for completeness. The UFC text says follow the practices in the discipline and follow the same abbreviation consistently (that appears to reference MIL-STD-38784A – which is actually about technical manual style – but the general point stands).
* **No Plurals with Acronyms:** Don’t add “s” to make acronyms plural. Instead, if needed, write out the plural or use context (e.g., “two HVAC units” is fine, not “two HVACs”).
* **Unit Symbols:** Use standard symbols for units (ft, in., psi, kW, etc.) and be consistent. They should match the UMRL or common standards. (Also recall dual units formatting from earlier.)
* **Abbreviations in SpecsIntact:** Typically, the UFGS will have a section (often an Appendix B Glossary) for acronyms, or sometimes acronyms are listed in the References if they are references. It’s not mandatory to have an acronyms list if only a few are used and they’re spelled out on first use. But do ensure that across the spec, you don’t have the same thing spelled out in one place and abbreviated in another without introduction.
* Avoid overly local or project-specific abbreviations that might confuse. Stick to widely recognized terms.
* If an acronym could be confused (like CO could mean Commanding Officer or Contracting Officer or Carbon Monoxide), clarify it by context or don’t use it. In a spec, CO usually not used because it’s ambiguous.
* Example: Use **“NTP”** only after saying “Notice to Proceed (NTP)” once. Use “NASA” only after “National Aeronautics and Space Administration (NASA)” if it appears (though NASA is so well known it might not need it in some contexts).

**2.9.3 Numbers and Units:**

* **Numerals vs. Words:** Spell out numbers under 10 (one through nine) and use numerals for 10 and above, as a general rule【59†L1100-L1108 (part, though not explicit)】. Additionally:

  * Always use numerals when a number is accompanied by a unit of measure, regardless of size (e.g., 5 mm, 3 days, 2 inches, 1 percent).
  * Spell out a number at the beginning of a sentence (e.g., “Twenty samples shall be taken…” or better yet rephrase to avoid starting with number: “Take twenty samples…”).
* **Time and Measurement:** For units like time, measurements, degrees, always use numerals plus unit abbreviation (except one and zero, see below). e.g., 4 hours, 2 weeks, 3 °C.
* **Use of “one” and “zero”:** The UFC suggests always spelling out “one” and “zero” when used alone to avoid confusion with O or I【59†L1100-L1108 (footnote likely)】. E.g., say “one coat of paint” not “1 coat” if just a single instance (though some specs might still use 1, but spelling out prevents someone reading it as “l coat”).
* **Avoid redundancy:** Don’t write both numeral and word (no “ten (10) widgets” in UFGS). That style is sometimes seen in contracts or legal docs, but for technical specs it’s unnecessary and adds clutter. The UFC explicitly says do not repeat a spelled-out number with a numeral in parentheses.
* **Consistent Unit usage:** Always present dimensions as numerals with units. E.g., 4 ft, 6 in., not “four feet six inches” (except in descriptive text if needed).
* **Formatting Units:** Put a space between numeral and unit (50 mm, not 50mm). Use the correct symbols (mm, not MM).
* **Fractions vs Decimals:** Use common fractions for inch measurements (e.g., 1/2 inch) unless a decimal is standard (0.5"). Typically in UFGS, inch fractions are given as common fractions (with a space: 1 1/2 inches) because that’s common in construction. But sometimes decimals are used for inches too. Whichever, be consistent and ensure it’s clear.
* When dual units are shown, one might be fraction and the other metric. E.g., *“<MET>6 mm</MET><ENG>1/4 inch</ENG>”*.
* **Large numbers:** Use commas for thousands (1,000; 20,000) in text or digits grouping as appropriate.
* **Percent:** Use the % sign with a numeral (e.g., 5%), but in a sentence, if starting a line or no number given, write “percent” (e.g., “Zero percent” spelled out, but seldom needed).
* **Temperature:** Use °C or °F with numeric (with a space: 21 °C).
* Ensure the context makes clear what the number refers to. If you say "provide six", six what? Always pair with a noun or unit.

**2.9.4 Terminology (Jargon and Redundancies):**

* Avoid colloquial construction jargon in formal specs. Words like *“bulkhead” (when meaning wall), “deck” (floor), “pit” (excavation)* should be replaced with the proper technical term. Use *“wall,” “floor,” “excavation,”* etc.
* Avoid archaic or formal legalese like *“hereinbefore,” “hereinafter,” “thereof,”* etc.. Modern specifications use plain language. So, instead of “the parties hereto,” just say “the Contractor and the Government”.
* Eliminate superfluous words: *“the Contractor shall completely and thoroughly clean...”* can just be **“clean...”** (with an expectation of completeness by definition). Words like *“securely,” “properly,” “in a workmanlike manner”* are subjective. If something must be secure or proper, specify measurable criteria or leave it implied by referencing a standard or general requirement.
* *“First-class workmanship”* – don’t use. Quality is ensured by meeting all specified requirements and industry standards; such phrases are unenforceable.
* Avoid double phrases like *“each and every,” “any and all”* – just say “all” or “each” as needed.
* Avoid **redundant wording**: e.g., “completely remove” (remove implies completely), “true and correct” (pick one), “type of” (often unnecessary as in "type of material"). The UFC suggests avoiding “conforming to,” “all,” and “type” as filler words. For instance, instead of “Materials shall conform to all requirements of ASTM C150,” just say **“Materials shall conform to ASTM C150.”**
* **Indefinite words:** *“etc.”, “and/or”, “any” (when used vaguely)* should be avoided.

  * Use **“for example”** or **“e.g.”** instead of “etc.” if you intend to list examples.
  * Do not use **“and/or”**; rewrite the sentence to be clear (often “or” suffices because in specs usually “or” is interpreted inclusively unless stated exclusively). If truly both could apply, say “X or Y or both.”
  * Avoid using **“any”** when it could be misinterpreted. “any damage shall be repaired” could be okay, but “connect to any existing outlets” is too vague; specify which ones or how many.
* **Vague catch-all phrases:** *“as required,” “as necessary,” “to the satisfaction of...”* are generally not acceptable. If something is required, specify by whom or by what criteria. *“Install conduit as required.”* (Required by whom? Instead, “Install conduit as shown on the drawings.”) *“Clean surfaces as necessary before painting.”* (When is it necessary? Better: “Clean surfaces free of dust and grease before painting.”) *“to the satisfaction of the Contracting Officer”* – avoid, since it’s subjective; if there’s a standard or measurement for acceptance, state it.
* **Escape Clauses:** Similarly, phrases like *“in accordance with manufacturer’s recommendations”* are tricky if used alone—ensure they supplement but don’t override specified requirements. It’s fine to say "Install per manufacturer’s instructions" for something where we cannot detail everything, but ensure that doesn’t conflict with safety or code requirements.
* **Contracting Officer vs. others:** Use the term “Contracting Officer” for the person who will accept or approve, not “Engineer” or “Architect” in UFGS (since it's a government contract context). Actually, in UFGS, they often phrase things impersonally: e.g., “Submit XYZ for approval.” It’s understood the Government (Contracting Officer’s technical representative) approves it.
* If needing to reference Government action, "the Contracting Officer will ..." is used. But as said, avoid instructing the CO; just indicate something is "Government approved" or not.
* Summation: Use **clear, direct terms**. If a term could be interpreted differently by different parties, clarify it. For instance, instead of "high quality materials", specify the grade or standard those materials must meet.

**2.9.5 Avoidance of Symbols and Pronouns:**

* We discussed symbols in **2.6.5**: Do not use the actual symbols for feet, inches, degrees, plus/minus, percent, etc., in the text (with the exception of minutes/seconds for angles possibly and the special case noted: foot and inch marks can be used in combined dimensions like 8'-6" as that’s common). The provided table of symbols to avoid includes: `'` (foot), `"` (inch), `#` (pound number sign), `%`, `°`, `+`, `-`, `±`, `×` (they showed "• by" likely meaning the multiplication dot or times symbol), `/` (as substitute for per), `@` (at). Instead, spell them out as indicated in that table: foot, inch, pound, percent, degree, plus, minus, plus or minus, by, per, at.

  * They do allow that in dimensions and tables, `'` and `"` might be acceptable. E.g., 8'-8" in a table is concise. But in running text, prefer “feet” and “inches” to avoid confusion. Possibly compromise: “Pipe 6 ft (1.8 m) long” spelled out “ft”.
* Pronouns:

  * The UFC explicitly says avoid pronouns like “he, his, she, they, their, which, this, who, it” because they can create ambiguity about what noun they replace.
  * In tech specs, instead of “it”, repeat the noun: *“Apply the coating to the surface while **the coating** is still wet”* might be confusing; better: *“Apply the second coat to the surface while **the first coat** is still wet.”*
  * Instead of “they” or “their”, rephrase to plural nouns or restructure the sentence. In many cases, pronouns can be dropped entirely in spec text or replaced by the actual subject (Contractor, materials, etc.). For instance, not “bolts, which are galvanized, shall...” but **“galvanize bolts in accordance with ...”**.
  * If a pronoun is needed to avoid very cumbersome repetition, ensure it’s crystal clear what it refers to. Possibly add an antecedent: e.g., “tiles are delivered in boxes; **these** shall be stored...” (here “these” refers to tiles, but might be clearer to say “store tiles...” directly).
  * Gender-neutral: If referencing personnel in a generic way, use neutral terms. Instead of “workmanlike manner,” use **“skilled manner”** or just remove as noted. If referring to an individual in examples or hypotheticals, use “they” as singular generic (the UFC says to use singular they rather than gendered pronouns if you must use a pronoun).
  * For example, say **“the inspector will approve the work if it meets specifications”** instead of “he will approve...”.

**2.9.6 Capitalization of Defined Terms:**

* Certain terms are capitalized in specifications because they refer to specific defined entities in the contract. The UFC instructs to capitalize:

  * **Contractor** (the party doing the work),
  * **Contracting Officer** (the government’s authorized representative),
  * **Government** (referring to the US Government as party to the contract),
  * **Contract** (when referring to the agreement itself in formal terms).
  * Possibly also capitalize Section names when referencing (some specs do, e.g., “Division 01”).
  * Titles like Architect-Engineer are not typically used in UFGS text, but if it were, likely capitalized as it’s a defined role.
* Do not invent new capital terms without definition. For instance, don't capitalize “Subcontractor” or “Manufacturer” unless the contract definitions have them (usually they don’t define those as proper nouns).
* Use the term **“Contracting Officer”** consistently instead of other terms like “Engineer” or “Owner’s representative.” Navy specs sometimes used “Engineer” historically, but Tri-Service standard is Contracting Officer (and by definition in FAR, that can include their authorized representative).
* The UFC specifically says *“Use the term 'Contracting Officer'; do not use terms such as 'Officer in Charge of Construction', 'Contracting Officer’s Representative', or 'Government Representative'.”*. This means in the spec text, whenever you might refer to the person who will approve or direct, just say **Contracting Officer**. (The actual COR might be doing the action, but contractually, the COR’s authority flows from the CO, so it's fine to just say CO.)
* The capitalization helps denote these as defined contract terms (which are defined in the contract’s General Provisions, e.g., FAR 52.202-1 Definitions).
* Note: We avoid instructing the CO in tech specs as said, but you might mention things like “as approved by the Contracting Officer” or “submit for Contracting Officer approval.”

**2.9.7 Bracketed Options:**
*(This corresponds to “2-9.1 Brackets” in the TOC we derived, but logically fits with style conventions too since brackets are a device for options.)*

* **Use of Brackets \[ ]:** In UFGS master text, brackets enclose options or variables that the spec editor must choose or fill in. For example: *“Color: \[black] \[gray] \[white].”* The editor will choose one and delete the others and the brackets.
* Use brackets for:

  * **Choice of two or more items:** e.g., \[Steel] \[Aluminum] for materials.
  * **Optional text that may not apply:** e.g., *“Apply second coat \[if primer coat is used].”* (Though it's better to restructure or use tailoring if it’s a large conditional.)
  * **Blanks to fill project-specific info:** e.g., *“Design load: \[\_\_\_\_\_] kW.”* Typically shown as underscore placeholders.
* **Blank lines:** The standard is to use **five underscore characters** “\[\_\_\_\_\_]” to indicate a blank to be filled in by the editor. Do not use more or less; five underscores is a convention to catch attention and fit typical short entries. If a longer blank (like a sentence) is needed, it might be better to phrase it as a Note or instruction rather than a blank.
* **Order of Options:** List choices in the order of most likely or most common first. The UFC says “order of most commonly used item first”. For example, *“\[Galvanized steel] \[Stainless steel]”* if galvanized is the typical default, put it first.
* Provide a **space between bracketed options** so that when one is removed, you don't end up with words running together. The UFC explicitly says add a space after the comma and before the next bracket, and no extra spaces inside the brackets except preceding the units if needed. The example given: *“Provide \[galvanized steel] \[stainless steel] enclosure.”*. Notice there's a space after the first bracketed phrase before the next bracket.
* **Brackets vs. Tailoring:** Use brackets for simple variations, especially where the difference is just a word or short phrase. Use tailoring (as covered) for big differences or those that depend on known project or service conditions beyond just designer's choice. Do not mix both on the same content as previously noted.
* **Brackets vs. Notes:** If an option requires explanation (like "choose X in cold climates, Y in warm climates"), put that guidance in a Note to the Designer rather than in the text. The spec text should just have the bracketed options listed neutrally.
* **Clarity after editing:** Ensure that after removing brackets and unused options, the sentence reads correctly and is grammatically sound. E.g., *“Paint shall be \[red]\[blue].”* If “red” is chosen, remove “\[blue]” and the brackets, resulting in "Paint shall be red." (Correct). If the structure is more complex, double-check punctuation.
* **Not both bracket and tailor:** Confirm you’re not bracketing something that’s also under a tailoring tag. That would confuse the editor – better to separate those concerns (maybe nested tailoring for different services each with its own set of bracket options, but ideally avoid too many layers).
* **Nested brackets:** Sometimes a blank is inside a bracket for an optional phrase, etc., but try to avoid complicated nested brackets which can confuse. If needed, break into multiple sentences.
* The UFC gives an example of how to bracket blank lines: *“Provide brackets around five blank underscored characters (\[\_\_\_\_\_]) to indicate the designer is to provide wording.”*.
* Document any unusual bracket usage in a note if needed so the editor knows what to fill. For example, *“\[\_\_\_\_\_] psi \[at 28 days]”* with a note: "(Note: Insert required concrete strength and delete phrase if 28-day strength not needed)".

**2.9.8 Submittals Article and Items:**
*(This corresponds to the Submittal Items guidance, which was a large portion. We have a whole breakdown in 2.9.2-2.9.7 already prepared for submittals from the text above. We'll integrate them here in order.)*

Actually, let's reorganize submittal-related guidelines in the flow:
2.9.8 was a catch-all for submittals, but our outline had:

* 2.9.2 Submittals (SD definitions, etc.),
* 2.9.3 Submittal Naming,
* 2.9.4 Submittals tagged in text,
* 2.9.5 Submittal classifications (G, S, etc.),
* 2.9.6 Submittal Item Reviewers (G-coded Army stuff),
* 2.9.7 Design-Build Submittals after Award (D, C, R, A codes for design review).
* Actually in our TOC, submittals were under 2.9 (Writing Style) which might not be exactly style, but it's spec content style.

Given submittals is a large important part, let's cover them now:

**Submittals in UFGS (Part 1 Section):** UFGS Part 1 usually has a subsection **SUBMITTALS** listing all required submittals for that spec section. UFC 1-300-02 lays out rules for how to handle submittals:

* Only list actual required **submittal items** in the Submittals article – do not include instructions or discussion in that list. It should be a concise enumeration of what the contractor must submit (e.g., product data, shop drawings, test reports, certificates, etc.). Each entry will correlate to an “SD” (submittal description) category.
* **Format of Submittal List:** Typically, it’s a bulleted or enumerated list, each line starting with an “SD-##” code and the name of the submittal item, possibly followed by a classification letter in parenthesis like (G) or (A) – see classifications below. SpecsIntact expects them in a certain tagged format `<SUB>` etc.

  * Example:

    * SD-03 Product Data: **Pump performance curves**
    * SD-06 Test Reports: **Concrete compressive strength test results** (Project Record)
    * SD-07 Certificates: **Installer qualifications** (This example shows categories and items.)
* **Submittal Descriptions (SD numbers):** These are standardized codes defined in [UFGS 01 33 00 Submittal Procedures](https://www.wbdg.org/ffc/dod/ufgs/ufgs-01-33-00). Common ones:

  * SD-01 Preconstruction Submittals (like schedules, plans)
  * SD-02 Shop Drawings
  * SD-03 Product Data
  * SD-04 Samples
  * SD-05 Design Data
  * SD-06 Test Reports
  * SD-07 Certificates
  * SD-08 Manufacturer’s Instructions
  * SD-10 Operation and Maintenance Data
  * SD-11 Closeout Submittals
    ... etc.
    Each category has a specific meaning described in UFGS 01 33 00.
* **Use correct SD category:** When adding a submittal, categorize it under the correct SD. For instance, don't put a test plan under SD-03 Product Data incorrectly; that should be SD-01 (if it's a plan prior to work) or SD-06 (if it’s a report of test results).
* **One Submittal Item per <SUB> tags:** Each listed item should be within its own `<SUB> ... </SUB>` in SpecsIntact. Do not try to jam multiple items into one tag separated by commas. The UFC warns specifically not to list multiple items separated by commas within one set of submittal tags. Why? Because the SpecsIntact submittal register expects one item per entry for tracking. If you write “<SUB>Item 1, Item 2</SUB>” that confuses the automated tracking.

  * If multiple pieces of data naturally go together, consider if they can be described as one item (e.g., “Mix Design (proportions, test data, and certifications)” could be one item).
  * Otherwise, list them separately as “Mix Design – Proportions”, “Mix Design – Test Data”, etc., if needed.
* **Submittal Register and Commas:** Commas within submittal item text can cause misinterpretation by submittal tracking software (they often treat commas as separators). So avoid commas in the item description if possible, or use semicolons or conjunctions. The UFC explicitly says they cause problems when imported into RMS or spreadsheets.

  * If you need to list multiple attributes for one submittal item, consider using "and" or a semicolon in the description rather than a comma.
* **Double-space between items:** The list of submittals in the spec text should have a blank line between each major submittal category group or item for readability (the UFC says “Double-space submittal items.”, meaning likely an empty line after each).
* **Submittal Procedures Section coordination:** UFGS 01 33 00 describes in detail what each SD means and general requirements (e.g., how many copies, how the Government will review them, etc.). The individual spec section should not duplicate that information. Don’t include instructions like “submit 3 copies 14 days in advance” – those belong in 01 33 00 or the contract. The technical section just lists what to submit and possibly specifics like required content or format if needed (e.g., “test report shall include raw data and analysis”).
* Each submittal item must appear in both places: listed under SUBMITTALS in Part 1, and referenced in the relevant Part of the spec where it’s required. SpecsIntact tags allow linking these so the submittal register can be generated.

  * For example, if in Part 3 you say “Perform test X and submit test report.” you would ensure “Test Reports: X results” is listed in SUBMITTALS.
  * Conversely, don’t list something in SUBMITTALS that isn’t called for in parts 2 or 3 of the spec.
* **Detailed requirements in text, not in list:** Provide the details of what each submittal entails in the body of the spec, not in the SUBMITTALS list. The list should be concise titles. For instance:

  * In Part 3 under execution or quality control, you might say: “Submit test reports for concrete compressive strength, including results of each cylinder break and statistical analysis per ASTM C39.”
  * In SUBMITTALS you’d just have “SD-06 Test Reports: Concrete compressive strength results.”
    The UFC: *“Provide a detailed description of the submittal item and its requirements in the section subpart text, and not in the SUBMITTALS article.”*.
* **Don’t repeat Division 01 info:** Do not repeat information already covered in UFGS 01 33 00 in your submittal requirements. For example, 01 33 00 will say how many samples to submit, or what format O\&M data should be in. In your section, just list the O\&M data as a submittal and any section-specific content.
* **Submittals tagged in text:** In the body of the spec, when you mention something that needs to be submitted, you should tag it with <ITM> if using SpecsIntact linking. This ensures it correlates with the SUBMITTALS list. For example, “<ITM><SUB>Fire Hydrants</SUB></ITM>” could be in the text where hydrants are discussed, marking that an SD-03 Product Data submittal (for hydrants) is required. This is an advanced cross-link feature, but the main point: the submittal list and text references should match up.

  * The UFC states: *“Each submittal item in the SUBMITTALS article must appear only once outside the SUBMITTALS article in the section subpart text... The submittal item must appear, within the tags, exactly as written in the SUBMITTALS article... and not in the SUBMITTALS article.”*. This is a bit confusing, but it’s basically instructing that the item wording should be consistent and to provide details in text not in the list.
* **Submittal Naming Convention:** As covered, use unique names for each submittal item to differentiate them. If two different SD categories might otherwise use the same term, make them distinct. The UFC gives an example: if “Wall Louvers” appear under both SD-02 and SD-04, label one “Wall Louvers” and the other “Wall Louver Samples”.
* **Submittal Classifications (G, S, etc.):** After each submittal item, often a parenthesis with a letter is used, like (G) or (S). These indicate special handling:

  * **(G)** = Government approval required. This usually means a **“GA”** in the RMS submittal register, i.e., the submittal is “For Government Approval.” Only critical submittals get this designation – the Contractor can’t proceed without explicit approval. Use (G) sparingly, for items that truly need Government review like design data, critical materials, test reports that affect acceptance. The UFC: *“Only use a ‘G’ in submittal tags for items deemed sufficiently critical, complex, or aesthetically significant to merit approval by the Government.”*.
  * No letter (blank) usually means it’s “For Information Only (FIO)” – the Government does not formally approve; the Contractor just submits and the Government might review but not approve. This is typical for things like certifications, standard product data, etc., that don't need approval to proceed.
  * **(S)** = Sustainability submittal. A relatively new designation for items related to LEED or sustainability tracking that need to be compiled by the contractor for the Government’s sustainability documentation. The UFC goes into detail about “S” submittals.
  * **(A)** sometimes used in Army for “Approval” similarly to G, or might be used in Navy as “Approved, no resubmit needed if unchanged” (less common now).
  * In SpecsIntact, you'll actually put something like `<SUB>G<...>` within the submittal tag to denote the classification, but conceptually, just ensure to mark which need approval.
* **Government (G) Submittals:**

  * Indicate with **“(G)”** after the item in the list. Also, as per Army practice, sometimes the G is followed by a code in brackets to indicate who approves it (discussed in Submittal Item Reviewers below).
  * Use only when necessary. If a submittal is required but doesn't need formal approval, leave it unmarked (implicitly FIO).
  * If the spec is written for multiple agencies, all uses of (G) assume the Government’s representative (could be different titles per service, but unify as (G)).
* **Information Only Submittals:** The ones with no (G) or (S) are considered for information or for Contractor Quality Control only. The UFC says they have no letter following them. E.g., “Fire Hydrants” with no letter is just an FIO submittal.
* **Sustainability (S) Submittals:**

  * Mark submittal items with “(S)” if they pertain to sustainability data required by UFGS 01 33 29 (Sustainability Reporting) or LEED documentation, etc..
  * These ‘S’ submittals are compiled by the contractor into an electronic Sustainability eNotebook (which is described in 01 33 29).
  * Only include (S) if that sustainability requirement is actually applicable (e.g., if a project pursues LEED or similar). Typically, UFGS will include these only if an overarching project requirement triggers them.
  * Examples: Recycled content data, low-emitting materials documentation, energy performance calculations might be (S) submittals.
  * The UFC gives guidelines to ensure S submittals are meaningful:

    * Make sure each master spec product has been evaluated for sustainable options (availability, compliance).
    * Include the minimum compliance (like recycled content minimum) as the default in the spec.
    * Put sustainability requirements in relevant text (e.g., Part 2 material requirements) and tag needed submittals as (S) to capture evidence of meeting those.
    * If a product has multiple sustainable attributes, maybe each attribute could be a separate (S) submittal for clarity (or one combined).
    * They caution to use S classification to the maximum extent possible to lighten text: rather than writing a lot in spec about sustainability, require the submittal of proof so that products not meeting it will be caught. Also, if a Master is edited (like if certain products no longer need an S requirement), ensure those submittals are removed – a product removed means its associated S submittal should also go.
  * The UFC provides an extensive example listing of S submittals (with SD numbers) and items like “Recycled Content for Carpeting – S” etc., showing how they might look, and a list of bullet points of how to ensure each Master’s S submittals are up to date.
* **Submittal Item Reviewers Codes (Army, etc.):**

  * On Army projects, they often follow the (G) with a bracketed code indicating who approves it: e.g., (G)\[AE] or (G)\[DO]. These codes (AE, DO, AO, RO, PO) correspond to Architect-Engineer, District Office, Area Office, Resident Office, Project Office respectively, and are used in RMS to route submittals.
  * The UFC says: *“For Army only, the brackets following a “G” on a submittal item indicate a specific Government reviewer and approval is required for that item... a code of up to three characters may follow the G to indicate the approving authority.”*. It lists the codes as above.
  * For Navy, Air Force, NASA: they typically **do not use those codes** following G in their specs or submittal registers. They handle that differently (Navy might specify in Section 01 33 00 who approves what in narrative).
  * As a UFGS writer, include these codes only if relevant to Army, and likely under an Army tailoring or note. Many UFGS masters do show the Army codes by default, but then other agencies just ignore them. The UFC indicates perhaps to not show them for Navy/AF projects and instruct those services to handle in Division 01. There's mention: *“For Navy only, do not use the brackets following the 'G'. For projects, edit UFGS 01 33 00... to designate who approves Government Approved submittals.”*.
  * So, in the master, they might include (G)\[\_\_] with a note like “(For Army projects, insert AE, DO, etc., as applicable; Navy/AF leave blank).”
* **Design-Build Submittals after Award (D, C, R, A):**

  * These codes appear rarely and are specifically for Army design-build projects (maybe in submittals or text):

    * (D) = Designer of Record Approval required (DA).
    * (C) = Government **Conformance** Review of design (CR) required.
    * (R) = Both D and C required.
    * (A) = Both D and Government Approval (DA + GA) required.
  * Actually, these typically appear in the context of design submittals like design drawings or calculations in RFPs. The UFC section 2-2.12.6 (Design-Build Submittals for Design after Award) was about that:

    * For Army: use D, C, R, A codes as needed and as defined in UFC 1-300-09N (Navy’s design-build instruction? Possibly error, 1-300-09N is for Navy processes, but anyway) and the contract documents.
    * For Navy: just comply with the Navy’s design-build UFC or contract (they likely use just GA or not, and specified in RFP).
  * As a UFGS writer, if writing a performance spec for design-build, you might tag submittals of design documents with these codes (if Army). But these are advanced specifics likely provided via the design-build RFP processes.
  * Given their complexity, a note is often included in Army DB RFP UFGS: e.g., "When a 'D' follows a submittal, it indicates Designer of Record approval required; when 'C' follows, Government Conformance Review required; 'R' indicates both; 'A' indicates both Designer of Record Approval and Government Approval.".
  * For Navy design-build: they often simply require the contractor to submit design for Govt review via NAVFAC procedures without those codes, or they might say "For Navy only, comply with FC 1-300-09N and contract docs for design submittals".
* **Operation and Maintenance (O\&M) Data Packages:**

  * UFGS often need the contractor to submit O\&M manuals. These fall under SD-10 category.
  * The UFC guidance (2-2.12.7.1) detailed how O\&M Data is structured:

    * They have *Data Package Types 1-5* in UFGS 01 78 23, which escalate in complexity. The spec writer should indicate which data package level is required for that equipment/system. E.g., "O\&M Data (Data Package 5)" which is the most detailed.
    * Create submittal item under SD-10 for each required O\&M manual, stating the system and the data package type required.
    * The example given in UFC text: listing as an example a submittal "SD-10 Operation and Maintenance Data – Electrical Systems; Data Package 5; G".
    * And in the execution text, provide an idea of contents if needed but mostly trust UFGS 01 78 23 to detail what Data Package 5 entails.
    * The spec should instruct: "If additional content is needed beyond standard, include it in a subparagraph of the section.". E.g., if a particular manual needs an extra diagram not normally required, state that in Part 3 under O\&M.
    * Add change date in section tag if O\&M data package goes in changed sections maybe, but that's minor detail.
  * In summary for O\&M:

    * Always include O\&M data submittal requirements for any maintainable equipment in the spec (most UFGS masters do).
    * Reference UFGS 01 78 23 for how to compile them.
    * Annotate type (1-5).
    * Indicate Government approval (G) if needed (Army often marks O\&M manuals (G) because they want to ensure completeness).
    * If you require something specific in that manual, say so in the text.

This covers the submittal process integration in writing style and content.

**2.9.9 Warranty Clauses:**

* Already discussed under brand names and style: "Ordinarily, do not include warranty clauses in UFGS" because the base contract has a standard 1-year warranty clause (FAR 52.246-21).
* Only if a longer or special warranty is needed should it be in the spec, and even then:

  * The UFC says two exceptions:

    1. If industry routinely offers longer warranties (e.g. roof 20-year warranty) and it's cost-effective, you can require it.
    2. If adding terms for a warranty, only do so in rare cases with proper approval (Level 1 Contracting Officer per some criteria).
  * If a special warranty is added, ensure the clause is phrased carefully to not conflict with the contract warranty. Usually, they phrase as: “Provide a manufacturer’s warranty of 5 years for X covering defects in materials and workmanship, in addition to the standard 1-year construction warranty.” Something like that.
  * If you extend the period or conditions, mention that it's been coordinated with contracting (maybe a note).
  * Too many or too onerous warranty requirements can cause issues or require more approvals (since it might narrow competition).
* So in practice, only include a warranty requirement if:

  * It's common for that product (like chillers often come with 5-year compressor warranty).
  * It’s truly needed beyond the normal one year.
  * You have the authority/approval to do so.
  * Otherwise, rely on the standard one-year warranty in the contract (don’t restate it).
* Refrain from phrases like "The contractor shall warrant the work for two years..." unless approved, because that effectively modifies the contract clause and should be handled by a modification of the warranty clause by contracting.
* The UFC suggests if one does it, one should ensure the Level 1 Contracting Officer (i.e., the top procurement authority) has reviewed and approved that extension, or the spec should note that such extension has been reviewed and approved (they mention with a written approval or such).
* Essentially, think twice before including an extended warranty requirement.

**2.9.10 Excluding Contract Boilerplate from Specs:**

* Already covered: Do not put the actual content of contract clauses, procedural instructions for the Government, legal rights, etc., in the technical sections. That belongs in Division 00 or 01 typically.
* Focus on technical requirements (what materials, how to install, how to test).
* If there's a need to mention a contract mechanism, perhaps refer to it indirectly or coordinate with Division 01. For example, instead of writing dispute resolution steps in a spec, rely on the contract's Disputes clause.

*(We have actually encompassed this in various points above, such as not instructing the CO, not duplicating contract clauses, etc.)*

Finally, ensure the language is unambiguous and enforceable. After writing, a good practice is to ask: Could a competent contractor misunderstand this or exploit a loophole? If yes, clarify.

---

Given the length, I'll now incorporate all those points in a structured narrative following our list format.

## 1. UFC 1-300-01 – Criteria Format Standard (for UFC Documents)

**1.1 Purpose & Scope:** Establishes a unified format for all **Unified Facilities Criteria (UFC)** documents. UFCs provide planning, design, construction, and O\&M criteria for DoD facilities, ensuring consistency across Army, Navy, Air Force, Marine Corps, etc.. All UFCs (and single-service Facility Criteria) must follow this standard’s layout and style.

**1.2 Applicability:** Applies to **all** UFCs and FCs prepared under MIL-STD-3007. Variations are only allowed if approved by the Coordinating Panel (CP) early in development. Service-specific requirements should be clearly identified and only included when that service is the executing agent.

**1.3 References & Authority:** UFCs derive authority from DoD Directive 4270.5 and MIL-STD-3007. The **Foreword** of each UFC should note that UFCs are mandated by MIL-STD-3007 and issued under the authority of the Tri-Service Engineering Senior Executive Panel (ESEP). All references cited in the UFC must be listed in a **References** section (typically an appendix) using official titles and, if needed, publication dates. For example, list standards like *“ASTM E119-20, Standard Test Methods for Fire Tests of Building Construction”*. Use the **Unified Master Reference List (UMRL)** acronyms and titles for consistency.

**1.4 Format & Organization:** UFCs should be structured into chapters, sections, and appendices in a logical order:

* **Template & Styles:** Use the official **UFC MS Word template** (latest version) for drafting. It includes preset heading styles, paragraph numbering, cover page format, etc., to ensure compliance. Do not modify template styles (font, margins, etc.). Final documents are published as PDF with proper bookmarks and hyperlinks.

* **Cover/Front Matter:** Include a standard title page with UFC number, date, and title (e.g. *UFC 3-600-01, 12 May 2023, FIRE PROTECTION ENGINEERING FOR FACILITIES*). The cover should show *“Approved for Public Release; Distribution Unlimited.”* Also list preparing activity (USACE, NAVFAC, AFCEC) as appropriate. Following the cover, provide a **Record of Changes** table (change number, date, and location/description of changes) – for a new UFC this may be blank. Next, include a **Foreword** that explains the UFC program and includes signatures of the approving officials from each service.

* **Chapters & Headings:** Start with **Chapter 1 – INTRODUCTION**, covering purpose, scope, applicability, and other general info (like reissues/cancellations of older UFCs). Subsequent chapters contain the technical criteria content. Use a **decimal numbering** system for sections and paragraphs (e.g., 2-1, 2-2.3, etc.). **All numbered paragraphs must have titles** for clarity. Use Title Case or ALL CAPS consistently for headings (the UFC template typically uses ALL CAPS for chapter titles and Title Case for paragraph titles). If a recommended heading is not applicable, omit that paragraph entirely (do not leave it blank).

* **Table of Contents:** Provide a TOC listing all chapters, major sections, appendices, figures, and tables with page numbers. Use the template’s auto-TOC feature. Ensure it updates after final edits.

* **Numbering & Hierarchy:** Chapters are numbered 1, 2, 3, etc. Paragraphs use chapter-paragraph numbering (e.g., 2-1, 2-2). Subparagraphs use a hyphen and sequential numbers (2-2.1, 2-2.2, etc.). Use at least two subdivisions if you subdivide (e.g., if there is a 2-2.1, there should be a 2-2.2). Keep hierarchy logical. Typically limit to three levels deep in UFCs for clarity.

* **Appendices:** Label as Appendix A, B, C, etc. Appendices may include supporting material like **Glossary** (acronyms/terms) and **References**. For example, UFC 1-300-01 provides an **Appendix B – Glossary** and **Appendix C – References**. Only include appendices if needed. Otherwise, incorporate information in chapters.

* **Variations in Format:** The standard format is intended to be uniform. If a specific UFC requires a format deviation (due to unique content), the DWG must request CP approval. E.g., if an extremely large UFC needs to be split into **Volumes**, get approval. (UFCs over \~20 MB or covering disparate topics can be divided into Volume 1, Volume 2, etc., each with its own TOC.)

* **Publication Numbering:** Assign UFC numbers according to subject area. The DWG will recommend a series per MIL-STD-3007’s hierarchy. For example, Series “1-200” for general building requirements, “3-XXX” for discipline-specific design (300 structural, 400 mechanical, 500 electrical, etc.), “4-XXX” for specific facility types. Ensure the number does not conflict with existing UFCs (coordinate via the UFC program office). Once assigned, include a **supersession note** if it replaces a previous document (e.g., *“This UFC supersedes UFC 1-300-01, dated 18 July 2018.”*).

**1.5 Publication & Maintenance:**

* **Distribution:** UFCs are published electronically on the **Whole Building Design Guide (WBDG)** website ([http://www.wbdg.org/ffc/dod/unified-facilities-criteria-ufc](http://www.wbdg.org/ffc/dod/unified-facilities-criteria-ufc)) which is the official source. No paper distribution. Make sure final PDFs are 508-compliant (searchable text, alt-text for images) as needed for public access.

* **Classified/CUI Handling:** If a UFC contains Controlled Unclassified Information (CUI) or classified info (rare), it won’t be posted publicly. Instead, a notice is posted with instructions to obtain the full document through proper channels. (For example, some sensitive UFCs can be requested via a Protective Design Center with justification.) Otherwise, assume content will be public.

* **Record of Changes:** Limit to **5 changes** (after that, issue a Revision). Maintain a change log page. Each change should be identified by Change number, date, and a brief summary of what was changed. If a UFC has multiple changes, incorporate those in the next revision to avoid confusion.

* **Assigning Dates:** The **publication date** on the cover is the official release date. Changes are labeled by change number and date (e.g., *“Change 2, 08-2024”* will appear in headers or footers) but the cover date remains the original publication date until a full revision is done. Coordinate with NIBS (WBDG) to schedule posting so that the date on the document matches the actual availability.

* **Document Size/Volumes:** If a UFC is over \~20 MB or extremely lengthy, consider issuing it in parts or volumes. For example, a UFC might be split into Volume 1 (Chapters 1-9) and Volume 2 (Appendices) for ease of use. Each volume would have its own cover and TOC, and the overall UFC number is the same with Vol. indicators. This should be done at the discretion of the DWG and noted in the document (e.g., *“UFC 3-XXX-YY, Vol 1 of 2”* on the cover).

**1.6 Updates: Changes vs Revisions:**

* **Changes (Minor Updates):** A **Change** is an interim update that modifies part of an existing UFC without reissuing the entire document. Changes typically address specific criteria updates, new technology insertion, or correction of errors and usually affect less than 25% of the content. Changes must be approved by the DWG and CP. When a Change is issued:

  * Update the **Record of Changes** page with the change number and summary.
  * Modify the **section headers/footers** to include “Change X, \[Date]”.
  * **Identify changed text**: Mark new/changed text with change indicators. Use the convention **\X\…/X/** in bold around changed text (where “X” is the change number). For example: *\1\This sentence is added in Change 1./1/*. Provide a space after \1\ and before /1/ marks. Remove previous change marks if they are no longer needed for clarity.
  * *Simple editorial fixes (typos, formatting) are “clerical” and might not be marked or listed as formal changes.* They can be done without generating a Change number if they don’t alter requirements.
  * Do not change the base publication date for a mere Change; use the change date in the banner instead.

* **Limit on Changes:** No more than 5 changes should accumulate. Beyond that, a **Revision** is required. (One exception noted: the DoD Pricing Guide UFC can exceed 5 due to frequent updates, but it must still be revised every 5 years.)

* **Revisions (Major Updates):** A **Revision** is a complete update/reissue of a UFC (superseding the prior version). Triggers for a Revision:

  * More than \~25% of content is changed, or
  * Significant shifts in criteria (new codes, new design philosophies), or
  * The document has reached the 5-change limit or the 5-year mark without full update.
  * *Revisions require full coordination/approval by DWG, CP, and ESEP (senior executive sign-off).* Essentially treat it like a new UFC.
  * For a Revision: Update the **publication date** to the new release date. Remove all change marks from previous changes (start fresh). On the cover and Record of Changes, indicate it as a revision (e.g., *“Revised on 01 November 2025”*). List the previous version as superseded.
  * Also update the **Superseding statement**: e.g., *“This UFC supersedes UFC 3-XXX-YY, dated 1 Jan 2010, with Changes 1-4.”* so readers know it replaces the older doc entirely.
  * Revisions typically get a new **PDF filename and WBDG listing** (same UFC number but new date).
  * **Formatting a Revision:** Ensure it conforms to the latest template (if the template changed since the last version, apply those updates – e.g., new cover design or new section numbering). Delete obsolete appendices like old change logs, and reset the change count.

* **Identifying Changes in Text:** Within a draft, mark additions or edits with the change number as described. Minor wording or typographical corrections might not be marked if they don’t change meaning. Always remove change markings when incorporating into a revision baseline. The UFC provides an example (Figure 1-1) of marking changes: the changed text is bracketed by \1\ and /1/, and the letter X in those symbols corresponds to the change number. Do **not** leave these markings in the final PDF (unless policy is to show them; usually, official UFC PDFs do not show change markup except via the change record or a note in margins).

**1.7 Electronic Format Requirements:**

* **Use of UFC Template:** All UFC drafts **must be created using the official UFC template** (usually a Word template). This template includes the required styles for headings (Chapter, paragraph, subparagraph), tables, figures, headers/footers, etc. It also contains boilerplate text (e.g., the Foreword, signature blocks). Following the template ensures consistent **appearance (fonts, headings)** and makes it easier to generate PDF with bookmarks and hyperlinks.

* **Digital Publication (PDF):** Final UFCs are published as **PDF files**. Ensure the Word (or source) file is converted to PDF:

  * **Bookmarks:** All major headings (chapters, first-level paragraphs) should be bookmarked in the PDF for navigation.
  * **Hyperlinks:** Embed hyperlinks for cross-references and URLs. E.g., references to other UFCs or external websites should be clickable in the PDF. The WBDG online version often automatically links references like other UFC numbers to their download page.
  * **Page Layout:** The UFC template sets page size (Letter 8.5x11), margins (\~1 inch), and a header or footer with the UFC number and date. Typically, each page header shows the UFC number and date on the right, and page number centered or right on the footer (the template covers this). Verify that odd/even pages are correct if double-sided.
  * **Fonts & Styles:** Generally use a legible serif font like Times New Roman 12 pt for body text (template default). Headings might be bold. Avoid using multiple fonts or custom styles.
  * **Figures & Tables:** If included, ensure they fit within margins and have captions (Figure X-#, Table X-#) and are referenced in text. They should appear either on the same page as referenced or as close as possible. Use the template’s figure and table styles.
  * **Accessibility:** Provide alternative text for figures (in Word, set “Alt Text” describing the image content). Ensure reading order of textboxes or multi-column content is logical for screen readers (usually not an issue if using simple layouts).
  * If Controlled Unclassified Information is present, mark the PDF according to DODI 5200.48 (banner markings on top/bottom of each page).

* **UFC Content on WBDG:** In addition to PDF, the WBDG listing for the UFC will often show a summary, date, change numbers, and allow downloading the PDF. The **source Word file** is not public, only the PDF. (However, a **Change Request (CCR)** form is provided on WBDG for users to suggest improvements.)

**1.8 Copyright & Trademarks:**

* **Copyrighted Material:** If you need to include any content from non-government copyrighted sources (text, tables, figures), you **must obtain permission** and acknowledge it. The UFC foreword typically states *“Any copyrighted material included in this UFC is identified at its point of use.”*. So, insert a credit in a footnote or parenthesis right where it’s used. For example: *“(Reproduced with permission from ASHRAE Handbook 2019.)”* Also, likely include a notation in the reference section or an appendix of the source. Prefer not to include large chunks of copyrighted text – paraphrase or reference instead.

  * Common cases: reference standards text is usually copyrighted (e.g., NFPA, ASTM). Do not copy their exact wording; just require compliance. If absolutely necessary to quote (like a definition), keep it minimal and include **permission** from the publisher.
  * Use of **figures or tables** from copyrighted sources also requires permission and credit. For each such figure, put *“Source: \[Organization Name]”* or similar in the caption if allowed.
  * It’s better to create original figures or tables if possible, to avoid issues.

* **Trademarks:** Avoid using trademarked names unless necessary. Use generic terms instead of brands (e.g., say “polytetrafluoroethylene coating” instead of “Teflon™ coating,” unless the spec legitimately requires Teflon specifically). If a trademark is used, denote it (® or ™) on first use and perhaps footnote the owner. For example: *“**Kevlar**® (a para-aramid fiber by DuPont).”* The UFC suggests not using terms like “Officer in Charge of Construction” or other organization-specific titles that might be like internal jargon – stick to standard terms (this is more about roles, but similarly, don’t use a trademark like “Scotch® tape” – use “pressure-sensitive tape”).

  * Terms like MasterFormat®, SectionFormat™, etc., can be mentioned as they are industry standards (include the ® or ™ as appropriate at first use). In the references, you might cite CSI formats with their trademark symbols.
  * If the spec needs to refer to a proprietary system as an example (rare in UFCs), clearly state it’s an example and not an endorsement, and use a descriptor as well.

**1.9 Glossary of Terms:** If the UFC uses many acronyms or technical terms, include a **Glossary** (typically Appendix B) defining them. For example, list “**DWG** – Discipline Working Group” or “**CUI** – Controlled Unclassified Information.” Spell out acronyms on first occurrence in text with the acronym in parentheses. After that, use the acronym. Use abbreviations consistently (e.g., ft for foot, psi for pound-force per square inch). Avoid ambiguous acronyms: if “CO” could mean Contracting Officer or Carbon Monoxide, don’t use CO alone – clarify by context or use different abbreviation (e.g., “KO” for Contracting Officer is sometimes used internally, but here just spell it out to avoid confusion).

**1.10 Writing Style (General):**

* **Active Voice & Imperative Mood:** Write requirements **directly** – e.g., use **imperative** form addressing the contractor. *Do not write “The Contractor shall X”* when you can just write **“X.”** (It’s understood to be directive to the contractor in specs.) For example:

  * *Bad:* “The Contractor shall install the pump according to the manufacturer’s instructions.”
  * *Good:* **“Install pump in accordance with the manufacturer’s instructions.”** (No need to say “Contractor shall”). The spec document itself implies the contractor’s obligations.

* **“Shall” vs. “Will” vs. “Should”:** In UFCs and UFGS:

  * Use **“shall”** sparingly (some agencies prefer to avoid it entirely). Often, simply stating the requirement in imperative form is enough. If needed, *“shall” can denote a mandatory requirement.* (In UFC narrative text, it might be used occasionally for stating that “the design **shall** meet criteria X.”)
  * Use **“will”** for actions performed by the Government or a document (not by the Contractor). E.g., “Calculations **will** be reviewed by the Government.” Or, “Figure 4 **will** illustrate the layout.” In UFCs, you might see statements like “This UFC **will** be used for all DoD projects…” – that’s stating policy in future tense. Generally in specs, **“will”** indicates something the Government or document states.
  * Do **not** use “should” in requirements text – it implies an option or recommendation, which is not enforceable. If content is advisory (like design guidance in a UFC), “should” can appear, but if it’s a requirement, use must/shall or just state it definitively. (UFCs sometimes include advisory language for designers, which can use “should” to mean “it’s recommended”. But be cautious; clear directives are better.)
  * Use **“must”** in place of “shall” if needed to avoid ambiguity (some DoD style guides now favor “must” for obligations to comply with plain language guidance). E.g., “All designs **must** comply with UFC 1-200-01.” is equivalent to shall.

* **Directed Subject:** Specifications are **directed to the Contractor**, so:

  * Refer to the Contractor as “Contractor” (capitalized) when needed, but avoid overuse. The context usually implies the subject. For instance, instead of “Contractor shall submit test reports,” just say **“Submit test reports.”**
  * Do **not** address instructions to subcontractors, manufacturers, or others; funnel requirements through the Contractor. (E.g., not “Manufacturer shall provide…,” but rather **“Provide \[product] with manufacturer’s warranty…”** – the contractor is responsible for obtaining that warranty.)
  * Avoid phrases like “to the satisfaction of the Contracting Officer” – instead, specify objective criteria. (The CO’s satisfaction is implicit in meeting the spec requirements.)

* **Avoid Redundancy & Jargon:** Use **concise language**:

  * Don’t use doublets/triplets (e.g., “each and every,” “any and all” – just say “all”).
  * Avoid archaic terms like “hereinafter,” “heretofore,” “therein.” Modernize phrasing (e.g., say **“in this UFC”** instead of “herein”).
  * Eliminate unnecessary qualifiers: words like “completely,” “thoroughly,” “adequately” are subjective. If a surface must be clean, say **“Clean the surface of all dust, oil, and loose debris.”** (That implicitly means completely.)
  * **No “etc.” or “and/or”:** If you list examples, use **“e.g.,”** or **“for example:”** and give representative items. Avoid “etc.” – it leaves ambiguity about what else. Avoid “and/or” – rewrite the sentence to be clear (often just “or” is sufficient in specs, as it’s normally inclusive or; if you mean both, say “and” clearly or phrase it differently).
  * **No vague terms:** Don’t use phrases like “as necessary,” “as required,” without stating by whom or what standard. (Instead of “Clean surface as necessary,” specify the condition: **“Clean surface until free of dust and grease before painting.”**) Similarly, avoid “if necessary” – either it is necessary (then require it) or if it’s conditional, describe the condition.
  * **No “etc.”:** Every list should either be complete or say “including but not limited to” if absolutely needed. Better is to state a general category then examples.

* **Definite vs. Indefinite:** Avoid indefinite words like “any,” “either,” “appropriate,” “suitable.” For example, not **“use any suitable method”** – instead, **“use a method approved by the Contracting Officer”** or specify the method. Not **“connect to any existing outlet”** – specify which outlet or “each existing outlet indicated on drawings.”

  * If something is left to contractor’s choice, still frame it by standards: e.g., **“Use any of the approved products listed in UL Directory…”** rather than “use any product.”

* **Pronouns:** Use nouns instead of pronouns to avoid confusion:

  * Instead of “Install the pump so **it** is accessible for maintenance,” say **“Install the pump so **the pump** is accessible for maintenance.”** Or restructure: **“Install the pump in an accessible location for maintenance.”**
  * Avoid gender-specific pronouns entirely. Use “they” as a singular generic if referring to personnel in examples, or just rewrite to avoid (e.g., “the inspector will…” rather than “he will…”).
  * Often, you can drop pronouns: *“Doors, which are steel, shall be painted”* can be **“Paint steel doors.”** Pronouns like “this” or “which” can make long sentences hard to parse – break into multiple sentences or use clear references.

* **Capitalization of Key Terms:** In UFCs/UFGS, certain terms are capitalized to denote defined entities:

  * **Contractor, Contracting Officer, Government, Contract** – capitalize these. (They correspond to definitions in contract FAR clauses.)
  * Do **not** use outdated titles like “Officer in Charge of Construction” or “Resident Engineer” – always refer to **“Contracting Officer”** for the government’s authoritative role. (Contracting Officer’s Representatives, architects, engineers, etc., all act through the CO, so in specs just use CO when needed.)
  * Other terms often capped: **Drawing, Specification** when referring to the contract documents; **Section** when referencing a spec section; **Appendix** if referencing parts of the UFC.
  * Do not capitalize common nouns that aren’t defined roles (do not capitalize “subcontractor,” “manufacturer,” etc., unless beginning a sentence).

**1.11 References Section:** At the end of the UFC (or in an appendix), list all reference documents cited:

* Use an organized format (e.g., Government documents first, then industry standards, then non-government publications).
* Include MIL-STD-38784A (style guide for manuals), MIL-STD-3007, relevant UFCs, and key codes/standards. For instance, UFC 1-300-01’s reference list includes MIL-STD-38784A and some example UFCs and non-government standards.
* Provide active hyperlinks if available (e.g., to **[http://www.everyspec.com](http://www.everyspec.com)** for MIL-STDs or **[https://www.wbdg.org](https://www.wbdg.org)** for UFCs).
* Each reference entry should include:

  * **For MIL/DoD documents:** Document number, title, issuing agency.
  * **For UFC/FC:** UFC number and title (and date or change if pertinent).
  * **For Codes/Standards:** Identifier (like ANSI/ASHRAE 90.1), full title, and publishing org.
  * **For others:** Sufficient info to find it (could include URL or publisher).
* In the UFC text, cite references by their document number only (e.g., “per MIL-STD-3007” or “as required by UFC 1-200-01”). Don’t include the full title in the text; that belongs in the reference list. The reference tagging (if using the template’s reference tag or superscript numbers) should correspond to the list.

*(End of UFC 1-300-01 section — Now transitioning to the UFGS specifics.)*

---

## 2. UFC 1-300-02 – UFGS Format Standard (for Guide Specifications)

**2.1 Purpose & Scope:** This standard (UFC 1-300-02) provides rules for writing **Unified Facilities Guide Specifications (UFGS)**, which are master construction specification sections used in DoD contracts. It ensures all UFGS, regardless of preparing agency, have a consistent **3-part format**, numbering system, and writing style. UFGS are published by Tri-Service committees (Discipline Working Groups) under ESEP authority and are accessible electronically at no cost. The UFC covers everything from document organization to style and approved terminology.

**2.2 Applicability:** Applies to **all personnel (Tri-Service and contractors) who draft or update UFGS sections**. All UFGS must comply with this format for inclusion in the official UFGS library on WBDG. Service-specific differences in specs must be handled as **tailoring options** within a unified section, rather than creating separate specs, whenever possible. (For example, one UFGS section can cover Army, Navy, and Air Force needs through options, instead of three separate specs.)

**2.3 Essential References & Tools:** Before writing a UFGS, be familiar with these:

* **CSI MasterFormat®:** The construction specification numbering and titling system maintained by CSI. UFGS section numbers and titles are based on the latest MasterFormat edition. Use correct 6-digit numbers (with optional 2-digit extensions for agency-specific versions). *Example:* **03 30 00 – Cast-in-Place Concrete** is a standard MasterFormat section. If there’s a service-specific version, it might be **03 30 00.00 10** (the “10” indicates Army). Always use the MasterFormat title exactly as given for that number (unless a title extension is needed for clarity on an extension section).

* **CSI SectionFormat™ & PageFormat™:** These provide a recommended arrangement of specification text into three parts and standard article titles. UFGS follow the 3-Part SectionFormat structure. Each Part has a typical sequence of topics (see 2.5 below). The PageFormat covers formatting like margins, paragraph numbering – which SpecsIntact handles for UFGS. Use SectionFormat’s standard article names (e.g., “RELATED REQUIREMENTS,” “REFERENCES,” “SUBMITTALS,” “QUALITY ASSURANCE” in Part 1, etc.) where applicable, to maintain consistency.

* **SpecsIntact Software:** UFGS sections **must be authored in SpecsIntact**, an XML-based spec editing tool. SpecsIntact enforces much of the formatting automatically (paragraph numbering, indentation, fonts, etc.) and includes features for reference management and submittal tracking.

  * Download **SpecsIntact** (free) from NASA KSC’s website ([http://specsintact.ksc.nasa.gov](http://specsintact.ksc.nasa.gov)). Also download the **SpecsIntact QuickStart Guides**:

    * *QuickStart Guide – Numeric* (for tagging and numbering paragraphs),
    * *QuickStart Guide – Process & Print/Publish* (for generating TOCs, printing combined sections).
  * **Use the UFGS section template in SpecsIntact** as a starting point for new sections. It has the required tags (like <SEC>, <PRT>, <PAR>, etc.) preset, which comply with this UFC.
  * SpecsIntact produces output in multiple formats: it can publish a project spec in **PDF**, **Word (DOC)**, or its native **SEC** format packaged in a ZIP. The final contract specs are often compiled as one PDF with all sections, plus separate submittal registers.

* **Unified Master Reference List (UMRL):** A tri-service managed list of standard reference documents (codes, standards, etc.) and their approved acronyms. SpecsIntact is integrated with the UMRL, meaning you can insert references by selecting from the UMRL. Always use UMRL entries for references to ensure correct acronym and citation. If you need a reference not in UMRL, coordinate to get it added or use an appropriate acronym consistent with UMRL style.

* **Standard UFGS Sections:** Many Division 01 sections (general requirements) are already written and maintained (e.g., **01 33 00 – Submittal Procedures**, **01 78 23 – O\&M Data**, **01 33 29 – Sustainability Reporting**). Do not duplicate their content in your section – simply enforce the outcomes as needed. For example, if you require O\&M manuals, you don’t describe how to format them; you just list “Operation and Maintenance Data (O\&M Manuals)” as a submittal and reference 01 78 23 for details. **Coordinate with these master sections** instead of overriding them.

* **DoD Policy & Other UFCs:** If your guide spec relates to criteria in a UFC or DoD policy (like anti-terrorism standards, sustainability requirements from UFC 1-200-02, etc.), ensure you reference those criteria properly. The UFGS is to implement design criteria into construction terms, so understanding the source criteria (other UFCs) is essential to writing the spec correctly.

**2.4 Content & Format Guidelines:**

**2.4.1 Content Guidance (General Principles):**

* **Three-Part Format:** Every UFGS section must be divided into **Part 1 – GENERAL, Part 2 – PRODUCTS, Part 3 – EXECUTION** (in that order). This is a fundamental CSI format and mandatory. Each part covers specific types of information:

  * **Part 1 – GENERAL:** Describes the administrative and procedural requirements specific to that section. Typically includes: **SUMMARY** (scope of section if needed), **REFERENCES** (list of cited standards), **SUBMITTALS** (what the contractor must submit), **QUALITY ASSURANCE** (qualifications, certifications, mock-ups, inspections by contractor), **DELIVERY, STORAGE, AND HANDLING** (any special requirements), **SITE CONDITIONS** or **DESIGN REQUIREMENTS** (if applicable), etc.
  * **Part 2 – PRODUCTS:** Details all the materials, products, equipment, mixes, systems, or fabricated items required by the section. This includes material properties, standards they must meet, acceptable manufacturers (if applicable and allowed), and so on. Organize Part 2 by subsystem or material type in a logical order (often following the flow of installation or importance).
  * **Part 3 – EXECUTION:** Specifies how products are to be installed, applied, or erected, as well as methods of workmanship and field quality control (tests, inspections). Common Part 3 articles: **EXAMINATION** (pre-install checks), **PREPARATION**, **INSTALLATION/APPLICATION** (or similar titles describing the work), **FIELD QUALITY CONTROL** (tests, inspections, acceptance criteria), **CLEANING**, **TRAINING** or **DEMONSTRATION** (if the contractor must train operators or demonstrate a system), **PROTECTION** (of finished work).
  * Appendix A of UFC 1-300-02 gives a recommended outline of paragraphs for Part 1, 2, 3 (mirroring CSI SectionFormat™). Use those standard headings when applicable (e.g., always have a “SUBMITTALS” article in Part 1 if there are any submittals).

* **Use UFGS Masters as Baseline:** UFGS sections are **guide specs** – they contain the baseline requirements that have been agreed upon by the Tri-Services and coordinated with industry. Write the UFGS to provide a **minimum acceptable quality level** and broad applicability. Project-specific editors will tailor them, but you should **not include less stringent requirements than industry standards or criteria** (no “low-balling” quality to cut cost). Conversely, you don’t need to cover extremely project-specific conditions; leave those for project tailoring.

* **Avoid Project-Specific Content:** Do **not** embed specific project data (dimensions, climate specifics, etc.) in the master. Instead, use placeholders or options. The master spec should be generic. For example, do not write “Design for 90 mph wind” in a master; instead, instruct the editor to input the project wind speed or reference the applicable code. As a rule, **requirements or restrictions that vary by project location or climate should not be “hardwired” into the master**. Provide them as options or notes so the project designer can include the correct values. *E.g.,* *“\[**Note to Designer:** Insert local frost depth requirement if applicable.]”*

* **Incorporate Design Criteria:** UFGS translate design criteria into construction requirements. That means if a UFC or other criteria document says “Facility must have X feature,” the UFGS should have the corresponding requirement that *contractor provides X feature meeting Y standard*. Always ensure the spec aligns with the intent of the design criteria:

  * **Do not conflict with higher-level criteria.** If UFC 3-XXX-YY mandates something, UFGS must not omit it or contradict it. Preferably, directly reference the UFC or criteria for clarity (e.g., “Design and install system in accordance with UFC 3-520-01 requirements.”).
  * **Reference Over Rewriting:** Rather than duplicating lengthy design criteria, refer to them. *Example:* Instead of copying seismic design procedures into the spec, say **“Design and detailing shall comply with UFC 3-310-04 Seismic Design for Buildings.”** The spec should then enforce submittals or construction practices to implement that design (like requiring submission of seismic calculations or special inspections). This avoids divergence between design manuals and specs.

* **Keep Content Broadly Applicable:** UFGS are used across many projects. Write requirements that make sense for most cases, with options for variations. Don’t tailor the master to a niche scenario. For instance, if a material is generally available meeting DoD needs, don’t specify a brand or region-specific type in the master; instead allow selection or include multiple options. UFGS content should be **non-geographic** and **non-proprietary** (unless absolutely necessary). This broad applicability also means using normative language that covers a range of conditions (e.g., “apply paint at temperatures above 5 °C (40 °F) or per manufacturer’s recommendations if different,” covers both warm and cold climate usage).

* **Clarity to Avoid Misinterpretation:** Write in a way that contractors and specifiers will interpret correctly and consistently:

  * Use **simple sentence structure**. Break long, complex sentences into shorter ones.
  * Be explicit: e.g., instead of “Install equipment in a workmanlike manner,” specify tolerances or standards: **“Install equipment plumb and level within a tolerance of 0.5%.”**
  * Avoid ambiguous words as noted (e.g., “adequate,” “reasonable,” “proper”). Provide measurable criteria.
  * Make sure every “it” or “they” has a clear antecedent or rewrite to remove them.
  * If using lists, ensure the lead-in phrase and list items grammatically connect.

* **Use of Notes (Editor Guidance):** Include **“Notes to the Designer”** in the master text to guide project editors on how to use the spec. Place these notes at appropriate locations (usually immediately below headings or before specific optional paragraphs) and clearly distinguish them (SpecsIntact prints them in italics or with “NOTE:”). For example: *“**Note:** Include the following paragraph only for projects in corrosive environments.”* These notes are **removed in the final contract specs** – they are purely guidance for the spec editor. Ensure notes are up-to-date and accurate so that editors know how to properly tailor the spec. Do not embed critical requirements only in notes; anything the contractor must do should be in the main text, not in a note.

**2.4.2 Editing UFGS for Projects:** (How masters are intended to be used by designers – as a UFGS writer, you facilitate this editing through format.)

* **Master vs. Project:** Remember that a UFGS is a **master guide** – the project designer **will edit it** to suit the project. Therefore, you should structure the master to make editing easy:

  * Include **bracketed options** and **tailoring tags** for all places where choices exist (so the editor can simply choose/delete rather than rewrite).
  * Use **blanks (\[\_\_\_\_\_])** for insertions where project-specific info is needed (like dimensions, performance values).
  * Provide notes as mentioned to instruct how to make those choices.
  * Ensure the spec text is **modular** – editors can remove a paragraph if not needed without breaking the flow or requirements of other paragraphs.

* **No Placeholder Text to remain:** Any bracket or blank in the master must be resolved by the project spec writer. Write the master such that if an editor fails to fill something in, it’s obviously an error (blanks are apparent). E.g., do not leave “\[Project Name]” or “\[Contractor to define]” – instead just use blanks or a note to prompt insertion.

* **Do Not Weaken Standards:** The UFC explicitly instructs project editors: *“Do not specify lesser quality requirements than are provided in the UFGS.”*. As a master writer, ensure the baseline is solid. Provide higher-end options as optional if needed, but the baseline should not be below industry standard. For example, if UFGS for concrete sets a compressive strength of 4000 psi, a project should not lower it to 3000 psi unless absolutely justified – and even then, that would typically contradict design criteria.

* **Deleting Unused Content:** Expect that project editors will delete any paragraphs that don’t apply. That’s fine – you should organize and word the spec so that deletion is straightforward. Use conditional statements or separate paragraphs for requirements that might not always apply. For instance, have a separate paragraph for “Cold Weather Requirements” which can be removed for a project in a hot climate. Avoid intermixing universally required text with optional text in one paragraph; separate them so optional parts can be removed cleanly.

* **Project Scope Edits:** The project editor might add to the spec for unique project needs. Provide guidance in notes for common additions (e.g., “**Note:** If project involves hazardous materials, include appropriate spec section from Division 02; this section assumes non-hazardous conditions.”). This way, masters set expectations about what they cover and what might need supplementing.

* **Tailoring for Service/Method:** If the project is for a specific service, the editor will activate the corresponding tailoring options (see Tailoring, section 2.8). Ensure that your master clearly labels service-specific content with tailoring tags so that when, say, “Navy” is selected, only Navy-specific text appears and Army/Air Force text is suppressed. Similarly for design-build vs design-bid-build (if you included those options).

* In summary, the **master should be like a toolbox**: it contains all the parts that might be needed, with clear labels and instructions, so the project spec compiler can pick the right parts and remove the rest easily. Your job as the master spec writer is to anticipate those needs and facilitate them through the format and notes.

**2.5 UFGS Section Organization:**

**2.5.1 CSI 3-Part Section Structure:** Every UFGS is organized into the three standard parts (General, Products, Execution) as noted. Additionally, CSI recommends a consistent **sequence of articles** within each part. The UFC Appendix provides guidance on that sequence, and it’s adopted by UFGS:

* **Typical Part 1 order:**

  * **SUMMARY** (or **SCOPE**) – brief overview if needed (not always used if title is self-explanatory).
  * **RELATED REQUIREMENTS:** (optional, list other sections that directly relate; sometimes omitted in UFGS since Division 01 covers coordination).
  * **REFERENCES:** – list of cited standards.
  * **DEFINITIONS:** (if special definitions are needed for terms in this section).
  * **SUBMITTALS:** – list of required submittals.
  * **QUALITY ASSURANCE:** – qualifications, certifications, mock-ups, field samples, regulatory requirements, etc.
  * **DELIVERY, STORAGE, AND HANDLING:** – any special instructions for protection of products.
  * **SITE CONDITIONS** or **PROJECT/SYSTEM DESCRIPTION:** – e.g., “Design Requirements” if the contractor has design/build responsibilities, or specific site constraints (rarely used – many site constraints are in Div 01).
  * **WARRANTY:** – if an extended warranty beyond the standard is required (usually avoided or placed in Part 1 as its own article if needed).
  * (Other Part 1 topics as needed like **SAFETY** or **SCHEDULING** if specific to that section – but general safety and schedule provisions are typically in Div 01).

* **Typical Part 2 order:**

  * **SYSTEM/ASSEMBLY** or **MATERIALS** – you might start Part 2 with a general description if it’s a system. If not, just start listing components.
  * **MANUFACTURERS** (optional – if you allow or require certain manufacturers or a source quality control, list or requirements for them here).
  * Then list distinct products or materials in logical order. For example: *2.1 CEMENT, 2.2 AGGREGATES, 2.3 REINFORCEMENT* (for concrete spec) or *2.1 PUMP, 2.2 MOTOR, 2.3 CONTROLS* (for a pump spec).
  * For each product, specify **standards compliance** (e.g., “Pipe: ASTM A53, Type E or S, Grade B”), **performance criteria** (like capacities, ratings), **fabrication requirements**, and **accessories**.
  * **Mixes or compositions** (if applicable) – e.g., concrete mix design requirements can be an article in Part 2.
  * **Finish or color** selections if any.

* **Typical Part 3 order:**

  * **EXAMINATION** – verify site conditions before work (e.g., “Verify substrates are ready to receive flooring”).
  * **PREPARATION** – actions required before installation (surface prep, demolition, protection of surrounding areas).
  * **INSTALLATION / APPLICATION / ERECTION** – the main execution instructions. Can be broken into multiple articles if different phases (e.g., “Placement,” “Finishing,” “Assembly,” etc., depending on the work).
  * **FIELD QUALITY CONTROL** – tests, inspections, and who performs them. For example, non-destructive testing, concrete cylinder tests, commissioning tests, etc. If independent testing lab or factory-authorized rep needed, say so here.
  * **ADJUSTING AND CLEANING** – any post-installation adjustments, calibrations, initial servicing, and cleanup of debris, touch-up of paint, etc.
  * **DEMONSTRATION / TRAINING** – if the contractor must train personnel or demonstrate systems (common in equipment specs).
  * **PROTECTION** – how to protect the finished work until turnover (e.g., cover flooring with protective board until project completion).
  * **SCHEDULES** – sometimes Part 3 ends with a schedule (tabular information like panel schedules, finishes schedule). If included, label clearly (e.g., “3.X SCHEDULES” with a table).

This sequence is a guideline – not every section will have all these, but if the topic is relevant, include it in that order. **Do not rearrange parts out of the logical order** without reason. CSI and UFC require maintaining a consistent sequence for ease of use across specs.

Also, **do not leave a Part completely empty**. If, for example, Part 2 truly has no content (perhaps in a very procedural spec), then insert *“PART 2 PRODUCTS – (NOT USED)”*. This signals to users that Part 2 is intentionally omitted. Same for Part 3 if it were not used (though that’s unlikely – Part 3 is almost always needed). Insert “Not Used” at the part heading level rather than deleting the part entirely to maintain the 3-part structure.

**2.5.2 Table of Contents (Section TOC):** SpecsIntact can generate a **section Table of Contents** listing the articles and paragraphs within the section. By default, contract specifications often omit the TOC in each section (to save space and because the project manual has an overall TOC). However, within the UFGS master, it’s useful for navigation. The UFC notes SpecsIntact has two options: a combined TOC for the whole project, and a section TOC embedded at the start of each section. For UFGS masters, ensure the section’s major headings are properly tagged so that if a TOC is generated, they’ll appear correctly. Key points:

* Section TOC typically includes Part numbers and titles and first- and second-level headings with their page numbers.
* If you include **attachments or appendices** in a section (rare, see 2.5.3), tag their titles with `<ATT>` so that the section TOC generator will list them.
* For publication on WBDG, some longer UFGS masters might have a TOC in the PDF for easy browsing (especially if over \~20 pages). Check the practice: if other similar UFGS include a TOC, do the same for consistency. (The UFC doesn’t mandate including the TOC in published specs, but it is helpful during editing.)
* **Do not manually type a TOC** – always use auto-generation to avoid errors and update issues. If a section is small (a few pages), a TOC is not necessary.

**2.5.3 Attachments and Appendices:**

* **Attachments (Appendices, Figures, Forms):** Attaching extra content to a UFGS section is **discouraged** and rarely needed. The preference is to keep the specification text self-contained and put extensive data or forms on a project’s drawing set or in electronic form separately. However, if needed:

  * Use the `<ATT>` tag and appropriate SpecsIntact markup to include an **Appendix** at the end of the section. Label it **Appendix X** and give it a title. Appendices in a spec section might be used for lengthy forms, data tables, or design guides that are better not interwoven into the spec text.
  * Note that if an appendix is included, the section’s title page or TOC should mention it. E.g., *“Attachment: Pump Performance Curve Data Sheet (for Contractor’s use)”*.
  * The UFC guidance: *“Attaching appendices to a UFGS section is rarely necessary. Create a simple appendix at the end of a section in SpecsIntact when necessary for project specifications.”* It also says if there is a **complex appendix**, it may be inserted as a separate PDF file into the final project manual. This implies: in such cases, in the spec you might just have a placeholder that says “See Appendix (separately bound)” or similar.
  * **Figures:** The standard is **do not embed figures or drawings directly in the spec text**. If a project needs to include a figure (like a diagram or sketch), the recommended approach is to attach it as a separate PDF or incorporate it into the drawing set. In masters, simply state requirement and perhaps refer to typical details that would be on drawings. If absolutely a figure is needed in the master (perhaps a standard detail), consider making it an appendix or providing it as a resource on WBDG rather than in the body of the spec. Typically, UFGS avoids figures; any necessary diagrams are left to design drawings or design guides outside the spec.
  * **Forms:** If the section references a form (like a checklist or test form), consider if that form is standard (maybe available via a website). If not, an appendix with the form can be included, or instruct via a note to obtain it from an external source.

* The guiding principle: **keep the spec lean**. Attachments increase complexity in maintenance. Often it’s better to provide an external reference or require the contractor to produce something rather than including a big attachment. Only attach what is necessary and cannot be succinctly described in text.

* If attachments are used, ensure they are properly referenced in Part 1 or relevant part (e.g., “Submit results using the form provided in Appendix A”) and included at the very end of the section with clear separation.

**2.6 Formatting Rules:**

*(Many formatting specifics are handled by SpecsIntact, but the following are important for the spec writer to know and check.)*

**2.6.1 Paragraph Numbering & Tags:** UFGS use an outline-style **numeric numbering system**:

* **Parts** are numbered “PART 1”, “PART 2”, “PART 3” (written in the text as such with a title).

* **First-level paragraphs** (Articles) under each part are numbered 1.1, 1.2, 1.3, etc. (The first digit is the part number). They should be in ALL CAPS or Title Case for titles, per CSI format. Usually UFGS masters use Title Case (e.g., “1.2 **REFERENCES**”).

* **Second-level paragraphs**: 1.1.1, 1.1.2, etc., with Title Case titles (capitalize principal words).

* **Third-level:** 1.1.1.1, 1.1.1.2, etc., with Title Case or sentence case titles as appropriate.

* **Fourth-level and beyond:** Typically, CSI recommends not numbering beyond 3 levels in specs. If more detail is needed:

  * Use **lettered or numbered lists** for sub-points (these are not numbered as part of the outline, but as list items). For example: under a third-level paragraph, list sub-items as “a. …, b. …” or “1) …, 2) …” depending on context.
  * If a fourth-level number is used (1.1.1.1.1), it must have a title as well, and it’s unusual but SpecsIntact can handle up to 6th level numeric. The UFC’s table shows levels up to 6 deep. However, deeply nested numbering can be hard to follow; break into sub-lists or separate paragraphs if possible for clarity.

* **No lone subheadings:** Do not leave a heading with no text or with only one sub-paragraph. For example, if 2.1 has no content except it immediately breaks into 2.1.1, 2.1.2, consider moving those up or adding some leading text under 2.1. Each heading should either have some descriptive text and/or at least two sub-points.

* **Titles required:** Each numbered paragraph and subparagraph **must have a title**. The only exception is if you have a short bit of text directly under a higher-level heading that serves as an introductory statement – but typically, even that can be given a title or incorporated into the parent’s text. So 2.3 “INSTALLATION” might have a sentence or two, then 2.3.1 and 2.3.2 subparagraphs. That’s fine, but each of those subparagraphs has a title. Use **Sentence case or Title Case** for subparagraph titles (Title Case is more common).

* **Numbering format example (from UFC Appendix A):**
  PART 1 – GENERAL
   1.1 ARTICLE (1st level)
    1.1.1 Paragraph (2nd level)
     1.1.1.1 Subparagraph (3rd level)
      a. Example (list item, not a numbered paragraph)
       (1) Example (further list)
       (a) Example
       1. Example (another style, if needed)
  *(This illustrates how deeper levels can turn into lettered/numbered lists. SpecsIntact’s Table A-1 shows both “Numeric without Tags” and “Numeric with Tags” views, with tags like <PAR> and <LST>.)*

* **Indentation & Formatting:** SpecsIntact ensures proper indentation for each level (usually increments of about 0.25" or 0.3"). Also, it handles paragraph spacing. As writer, focus on tagging content with the correct level (e.g., <PAR>, <SUBPAR>, <SUBSUBPAR>, etc., or list tags for lists). Visually verify that the rendered output is clear (sub-levels should be indented and/or labeled clearly).

* **Headers/Footers:** Each UFGS section’s header includes the section number, UFC info, and page numbering. SpecsIntact will generate something like “UFGS 08 34 73 (April 2006) Change 2, 08/16” on each page header, and “Page 5” or “8-5” on footers. Ensure the **Section Date (tag <DTE>) is updated** when changes are made. For changes and revisions, update the banner as shown in examples in section 2.12 below.

* **“Not Used” parts/paragraphs:** If a part or major heading is intentionally not used, mark it clearly as **“NOT USED.”**. E.g., *“2.2 Materials – NOT USED”* if all material info is covered elsewhere. This is preferable to deleting it, to show it wasn’t an accidental omission. Do this only at the part or first-level heading level, not for minor subparagraphs (minor ones can just be removed).

**2.6.2 Language & Grammar Conventions:** (Some of this overlaps with “Writing Style” in UFC, but applied to spec context)

* **Imperative Mood:** UFGS sections should be written in imperative language addressing the contractor (same as discussed in 1.10). For example: **“Provide, install, and test three pumps as indicated.”** It’s understood this is the contractor’s obligation. Use third person only as needed for descriptive statements (e.g., “The chillers shall be water-cooled centrifugal type…” could just be **“Chillers shall be water-cooled centrifugal type…”** or better, **“Provide water-cooled centrifugal chillers…”,** making it imperative).

* **No “shall” for Contractor actions:** Avoid phrases like “Contractor shall \_\_\_.” Just state the requirement. The UFC specifically instructs not to use “the Contractor shall” as a phrase.

* **“Shall” vs “shall be”:** Passive constructs like “X shall be Y” can often be rewritten actively: **“Make X Y”** or **“Provide X that is Y.”** For example:

  * “All wiring **shall be** in conduit” -> **“Install all wiring in conduit.”**
  * “Doors **shall be** solid core wood” -> **“Provide solid core wood doors.”**
  * If leaving as descriptive, it's okay to say **“Doors shall be solid-core wood construction, meeting ANSI A250.8.”** It’s clear enough as a requirement.

* **Units & Symbols:** Provide measurements in both metric and US customary:

  * Use the SpecsIntact **<MET>** and **<ENG>** tags to include both. For example: *“Depth: <MET>300 mm</MET><ENG>12 inches</ENG>.”* This will show as “Depth: 300 mm (12 inches).” in dual-unit output.
  * *Do not use the symbols* `"` for inches or `'` for feet in running text (except in tables or combined dimensions if necessary). Spell out *inches, feet, degrees, percent,* etc., or use abbreviations (in., ft, °C, %). Table 2-2 in the UFC lists symbols not to use in text: `'` (foot), `"` (inch), `#` (number or pound), `%`, `°`, `+`, `-`, `±`, `×` (often written as “x” or a dot for by), `/` (per), `@` (at). Instead:

    * Use “ft” or “feet” instead of `'` (except in say 8'-6" notation in tables).
    * Use “in.” or “inch” instead of `"` (except as noted).
    * Use “No.” or just omit if it’s a count instead of `#` (e.g., No. 4 bar, not #4 bar, or just “No.4 bar” spelled out).
    * Use “percent” or “%” (the percent symbol is widely accepted; UFC lists it as symbol to avoid, but in practice, 5% is usually fine. If in doubt, use “percent” in narrative text and % in parentheses or tables).
    * Use “deg.” or the degree symbol for degrees? The UFC forbids the `°` symbol in text, but specs often use “°F” and “°C”. Likely acceptable to use ° for temperatures since that’s standard, but always with a number and scale (e.g., 75 °F).
    * Use “plus/minus” or “±” carefully: they say don’t use ± in text, so write **“plus or minus 5 mm”** instead of “±5 mm”.
    * Use “by” instead of `×` for dimensions in text (e.g., “50 mm by 100 mm” not “50×100 mm”). In tables or short notation, “×” might appear but try to avoid.
    * Use “per” spelled out or better **“in accordance with”** instead of slash `/` (e.g., “kg per cubic meter” instead of “kg/m³” in running text, unless it’s a standard unit expression).
    * Use “at” spelled out instead of “@” (e.g., **“@ 600 mm o.c.”** should be **“at 600 mm o.c.”**).
  * These rules are to prevent misinterpretation and ensure clarity if fonts don’t render, etc.
  * **Metric first:** Always put SI units first, then English in parentheses or subsequent tags. *Example:* **“Thickness: <MET>10 mm</MET><ENG>3/8 inch</ENG>.”**
  * Maintain **consistent precision**. If you say 25 mm (1 inch) in one spot, don’t switch to 26 mm (1 inch) elsewhere – be consistent about conversion (1 inch = 25.4 mm, but typically round to 25 mm). The UFC suggests using industry practice or ASTM SI 10 for conversions. Avoid excessive precision that implies more accuracy than needed.

* **Abbreviations:** Define each acronym on first use as per 1.10. In a single spec section, define once in Part 1 if needed or at first occurrence in any part. Use abbreviations consistently (e.g., “PVC” for polyvinyl chloride after definition, “psi” for pressure, “°C” for degrees Celsius, etc.). Follow the discipline’s common usage – e.g., electrical sections use “kVA”, mechanical uses “CFM”, etc., but ensure they’re spelled out once (Cubic Feet per Minute (CFM)). Keep units standardized (don’t sometimes say “lbs/sq in” and elsewhere “psi” – pick one, preferably “psi”).

* **Spelling & Capitalization:** Use American English spelling (e.g., “labor” not “labour,” “center” not “centre”). Capitalize product names only if they derive from a proper noun or are trademarked (e.g., “Portland Cement” (from proper noun – named after Isle of Portland), but “epoxy paint” is lowercase). Capitalize references to sections (e.g., **“Section 09 90 00 PAINTS AND COATINGS”** – usually the title is in caps).

* **Lists:** Use bulleted or numbered lists for clarity when enumerating options, requirements, or steps. SpecsIntact has list tags that will automatically format:

  * **Bullet style (•)** is often not used in formal specs; instead, lettered or numbered lists are used.
  * Use **letters (a., b., c.)** for lists within a paragraph, and **numbers (1), 2), 3))** for sublists under letters, etc., following CSI’s hierarchical list format.
  * Each list item should end with a semicolon if continuing the sentence from the lead-in, or a period if it’s a full sentence item. Use “; and” or “; or” at the second-to-last item if grammatically needed.
  * Introduce lists with a colon after the lead-in phrase (e.g., “The following tests shall be performed: a. Pressure test; b. Leakage test; c. Operational test.”).

**2.6.3 Subpart Titles & Content:**

* **Titled Subsections:** As emphasized, every numbered subsection needs a title. For UFGS:

  * **ARTICLE (1st level under Part):** Use uppercase or bold Title Case. e.g., “3.1 **INSTALLATION**”.
  * **Lower-level subpart titles:** Use Title Case (capitalize first letter of principal words). e.g., “3.1.1 **Equipment Placement**”.
  * Titles should succinctly describe the content. If a paragraph is about a specific material or test, make the title that term.
  * If a subpart contains multiple paragraphs under it, you might not need a title for each if they flow as one, but usually if it’s a separate requirement, give it a separate number and title.

* **Untitled Text:** The UFC states use *no more than two untitled text paragraphs* in a row under a heading. Typically:

  * You might have an opening paragraph under a first-level heading that is a general statement, followed by specific subparagraphs. That opening could be untitled (it effectively carries the heading’s title). But if you need another untitled after, consider merging or giving it a title.
  * E.g., “2.2 Materials:” could be just a heading and then directly start listing materials 2.2.1, 2.2.2. That heading “Materials” is itself the title, so no need for an introductory paragraph unless needed for clarity.
  * If you find multiple consecutive paragraphs with no titles, consider whether they should be part of one paragraph or each merits a sub-number and title.

* **Paragraph Groupings:** Use paragraph numbers down to the level needed. If listing options or distinct cases, consider using separate numbered paragraphs rather than a run-on paragraph.

  * For example, instead of writing a huge paragraph describing 3 types of installation, break it into 3 subparagraphs, each titled for the type.

* **Part Titles in Section TOC:** Part titles (“GENERAL”, “PRODUCTS”, “EXECUTION”) will show in all caps. Article titles might show in the TOC as written (CSI suggests all caps for first-level articles, which many UFGS follow, but Title Case is also acceptable if consistent).

**2.6.4 Notes to the Designer:** *(Already covered in concept, but here focusing on format.)*

* Denote **Notes** clearly so they are not mistaken for spec text. SpecsIntact does this by italicizing or bracketing them and not numbering them.

* Place **Notes** immediately after the heading to which they pertain, before the actual requirement text starts. For instance:

  ```
  2.4 COATINGS
  **NOTE:** Select Option A for mild climates; Option B for coastal.
  <TAI OPT=A>Use Coating Type A ...</TAI>
  <TAI OPT=B>Use Coating Type B ...</TAI>
  ```

  Here the note tells the editor how to choose between A and B.

* Use notes to:

  * Explain purpose of an option or bracketed text.
  * Indicate **when** to include or exclude something (e.g., “**Note:** Omit this article if no standby generator is used on project.”).
  * Provide cross-references to other sections or criteria that the editor might need (e.g., “**Note:** Coordinate the following firestopping requirements with Section 07 84 00 Firestopping.”).

* Keep notes succinct. They are instructions, not general info. And avoid including critical technical data only in a note – notes won’t be in contract docs.

* **Tailoring of Notes:** If a note only applies under certain tailoring conditions, put it inside the tailoring tags as well, so it disappears when not relevant. For example, a note specific to Army usage can be wrapped in `<TAI OPT=ARMY>` so Navy/Air Force editors don’t even see it.

* **Removal:** SpecsIntact can strip notes when printing the final project spec (by default, notes are excluded in “Ready to Advertise” output). The spec writer should ensure that *none of the note text is needed by the contractor*. If something in a note is actually a requirement, move it to the main text.

**2.6.5 Units of Measure:** *(We already went over dual units in 2.6.1, but to reiterate key points specific to UFGS usage.)*

* All UFGS masters are written in **dual units** (SI and Imperial). The <MET>/<ENG> tags facilitate output in either or both.
* **Metric first, then English:** e.g., *Length: <MET>50 mm</MET><ENG>2 inches</ENG>*.
* **No parenthetical in input file:** Let SpecsIntact handle formatting. As the author, you just ensure both tags are present. Don’t manually put parentheses; the software may add them. (The UFC says don’t use parentheses to show dual units in the master file.)
* **Check conversions:** Use standardized conversions (1 inch = 25 mm (approx), 1 ft = 0.30 m, etc.). If using nominal units (like 1/2 inch rebar which is actually #4, 12.7 mm), you can round metric to a neat number or vice versa. The key is to reflect common practice: e.g., if a product is typically 3/4 inch (19 mm), list it that way, not 20 mm.
* **Set Project Units:** The editor, when using the UFGS, will decide if the project will be in metric, imperial, or dual. *Design-bid-build MILCON jobs are often in metric (with inch in parentheses); many repair jobs are in inches (with metric in parentheses). The master provides for both.*
* In pure metric output, the <ENG> content is dropped; in pure English output, the <MET> is dropped. Write sentences such that removal of either still yields a grammatically correct result (SpecsIntact normally handles the punctuation – it won’t leave a dangling comma, etc., if you didn’t put one inside the tags incorrectly).
* Example formatting in master vs output: Master: `Equipment shall weigh not more than <MET>450 kg</MET><ENG>1000 lb</ENG>.`

  * Metric-only print: “Equipment shall weigh not more than 450 kg.”
  * English-only print: “Equipment shall weigh not more than 1000 lb.”
  * Dual print: “Equipment shall weigh not more than 450 kg (1000 lb).” (assuming the software adds parentheses).
* **Job set to one system:** The UFC reminds, project specs will be one or the other (except sometimes dual shown for info). The master must accommodate both.

**2.7 Referenced Standards & Cross-References:**

**2.7.1 References Article:** In Part 1 (usually after Summary or before/after Submittals), list all references cited in the spec:

* Begin with a standard clause like: **“REFERENCES**: The publications listed below form a part of this specification to the extent referenced. The publications are referred to within the text by the basic designation only.”\* (This indicates that in the spec text you’ll just use “ASTM C150” and here you’ll list the full title.)
* **Listing format:** Each reference should be listed by:

  * **Identifier** (like ASTM C150, ISO 9223, UFC 3-501-01, etc.) – usually bold or all caps, followed by a comma,
  * **Title** of the document (and possibly publication date or edition if not the latest).
  * Optionally, the **publisher/organization** if not obvious from the acronym (for less-known acronyms).
  * Many UFGS use a format with bullets or dashes. The UFC snippet shows bullets for each reference.
  * *Example entries:*
    • **ASTM SI 10** – *Standard for Use of the International System of Units (SI)*
    • **ISO 9223** – *Corrosion of Metals and Alloys – Corrosivity of Atmospheres*
    • **DoD 4270.5** – *Military Construction, 5 February 2005*
    • **MIL-STD-3007** – *Standard Practice for Unified Facilities Criteria and Unified Facilities Guide Specifications*
    • **MasterFormat** (CSI MasterFormat – *Master List of Numbers and Titles*, latest edition)
    • **SectionFormat/PageFormat** (CSI SectionFormat™ and PageFormat™, 2008)
    • **UFGS 01 33 00** – *Submittal Procedures*
    • **UFGS 01 78 23** – *Operation and Maintenance Data*
    etc.
* **Tagging in SpecsIntact:** Use the <REF> tag for each reference in the list. It usually has an attribute for the reference ID (RID) and displays the text. In the spec text, wrap references in <REF> tags too (like `<REF>ASTM C150</REF>`). This links them so that if the reference list is updated or the spec is checked, it knows whether all references are accounted for.
* **Don’t list unused references:** The list should not include standards that are not actually cited in the text. Conversely, every standard mentioned in text should be listed here. Use SpecsIntact’s report features to verify no orphan references.
* **No contract clauses here:** As per 2.7.3, do not include FAR or DFARS clauses in the references list, even if mentioned. Those are not “publications” in the same sense (they are contractual requirements included in Division 00). If you mentioned FAR in text, that was just advisory; it’s not typically listed here.

**2.7.2 Reference Citations in Text:**

* In the UFGS text, when referring to a standard, use the **publication number only** (no date, no title). e.g., **“Comply with ASTM C150 for cement.”** or **“IEEE C2, National Electrical Safety Code (NESC)”** might be referenced just as “IEEE C2”.
* Do **not** say “latest edition” in the text; that is understood. Do not include issue dates in text either.
* Use the acronyms for organizations as defined: e.g., use **“ANSI/AISC 360”** not “American Institute of Steel Construction Standard 360” in text. Use the acronym that is listed in the references (UMRL will have the proper acronym).
* If multiple standards from the same org are referenced, they each get their own entry. If one reference is superseding or replacing another, don’t list the obsolete one unless it’s still needed for context.
* If an **acronym conflict** arises (two different organizations share one, or a standard is co-issued), follow UFC guidance: pick one acronym (preferably the issuing body). E.g., if a spec references **ANSI/IEEE Std 142**, list it under IEEE and just call it IEEE 142 in text (the UMRL might list it as IEEE 142 with a note that it’s an ANSI-approved IEEE standard).
* Use **consistent acronyms** as per UMRL: e.g., use **“ACI”** (American Concrete Institute), **“NFPA”** (National Fire Protection Association), etc., not spelling them differently elsewhere. If new, define them in References or Glossary.

**2.7.3 FAR and Contract Clauses:** (Summarizing to reinforce)

* Avoid referencing FAR/DFARS clauses in the spec text. If you must mention them (for context like “Brand Name or Equal”), cite by number and title only, no text. E.g., **“(as defined in FAR 52.236-2 **Differing Site Conditions**)”**. But typically, prefer to handle contract matters in Division 01 or let contracting include the clause.
* *Never include full clause text.* It’s legally repetitive and could conflict if updated.
* Don’t include them in the **References** list.

**2.7.4 Reference Standards – Editions & Dates:**

* UFGS aim to use the **most current standard** at time of publication. As a master spec writer, update references to latest editions during periodic revisions or when a CCR (Criteria Change Request) mandates it. Project editors and SpecsIntact will update to newer versions if UMRL is updated, but your master should not lock in an outdated version without reason.
* If there’s a **specific reason to use an older version**, note it (perhaps in a note to the editor or in the text if needed). Otherwise, it’s assumed latest edition. Do not put years in the spec text. In the References list, you may or may not include years – many UFGS omit the year to avoid needing to change the spec text when the standard updates. Some list year in parentheses for clarity. Follow UMRL convention: UMRL entries often include the year in the title or designation if necessary.
* **Revisions and Amendments:** If referencing a particular revision state (R, C for Change, etc.), separate by semicolon as instructed. This is rare in UFGS text – typically done in references if at all. E.g., “ASTM E119-2018; E119-20a (errata 2021)” – but again, usually just referencing the base standard is enough.
* **Automatic updates via UMRL:** SpecsIntact can generate a submittal register and verify references via UMRL. If a reference is updated in UMRL (say, ASTM issued a new year version), the software might flag it. As writer, encourage use of the UMRL tool to keep the spec current.

**2.7.5 Quoting Reference Content:**

* Do not copy large chunks of standards or codes into the UFGS. Instead, enforce them by reference. Only **quote small critical excerpts** if absolutely necessary to clarify something and ensure it’s legally allowed.
* If a specific test method or formula from a standard is crucial, you could include it, but then you must maintain it if the standard changes. It’s often better to say **“Perform test in accordance with ASTM E119. If an element does not meet criteria, it will be considered a failure.”** – rather than copy ASTM acceptance criteria verbatim.
* If you do quote or paraphrase a reference, identify its source (and if needed, treat it as potential copyrighted content – e.g., if quoting a paragraph from an ASME standard, that’s copyrighted; try to avoid doing so, or paraphrase in your own words).
* Quoting internal references: e.g., referencing a paragraph within another spec section – better to avoid as numbers can change. Instead, incorporate the needed requirement in this spec if it’s essential, or instruct the project editor to coordinate.

**2.7.6 Cross-References to Other Sections:**

* **Within UFGS text, refer to other spec sections by number and title** when needed. For example: **“Coordinate openings with **Section 08 11 13 STEEL DOORS AND FRAMES**.”** Use the full section number (with leading zeros and spaces per MasterFormat) and the exact section title in caps. SpecsIntact <SRF> tag can format a cross-reference like that and keep track if needed.
* Do not refer to specific paragraphs of other sections (those can renumber with edits). Instead, refer generally: e.g., “as specified under **Section 23 07 00 THERMAL INSULATION** for duct insulation requirements.”
* If referencing a part of the same section, use the paragraph title not number: e.g., “as specified in **3.2 FIELD QUALITY CONTROL** of this section” (title in caps, or in quotes). Because if you add a new test above, what was 3.2 might become 3.3, but the title “Field Quality Control” remains the same.
* Try to minimize these cross-references. Overuse can cause a chain of dependencies that complicate editing. Use them only to avoid duplication of common info. For instance, if this spec section needs something that is fully detailed in another section, then reference it rather than copying.
* **Ensure cross-referenced sections exist:** If you reference a section that might not be in all projects, include a **Note to Designer**: *“Include Section XX XX XX \_\_\_\_ in the project if not already included, as it is referenced above.”* Or provide an option if that section isn’t used.
* The UFC specifically says avoid cross-referencing unless necessary for clarity. Ideally, each section should be as stand-alone as possible.

**2.8 Tailoring Options (Optional Text Control):**

**2.8.1 Service-Specific Tailoring:**

* UFGS often have to accommodate differences between Army, Navy, and Air Force requirements. Instead of separate specs, use **tailoring tags** to include/exclude text for each service.
* **How:** Enclose service-specific text in `<TAI OPT=ARMY>…</TAI>`, `<TAI OPT=NAVY>…</TAI>`, and/or `<TAI OPT=USAF>…</TAI>` (AFCEC for Air Force) as appropriate. The UFC refers to “AFCESA” (old Air Force Civil Engineer Support Agency acronym) and NASA as well for tailoring codes. The section banner often lists which agencies contributed (USACE/NAVFAC/AFCEC/NASA), and those align with tailoring options.
* Mark any service-unique requirements this way. Examples:

  * If the Army requires a certain test that Navy and USAF do not, put that test paragraph in `<TAI OPT=ARMY>…</TAI>`.
  * If Navy has a different submittal process, e.g., no “\[G]” codes, then notes or text related to those can be tailored out for Navy.
* **Default (Tri-Service) text:** Write unified requirements that apply to all services without tailoring. Only use tailoring for the divergent parts. The goal is to maximize common text.
* **Avoid duplicative methods:** Do not have both a bracket and a tailoring for the same difference. If a difference is purely service-related, use tailoring not brackets. Brackets are for project-specific or technical options that any service might choose.
* **Coordination in Part 1 (Submittals):** The big area of differences is often submittal procedures. The UFC notes that Army, Navy, USAF handle submittal coding differently (Army uses the RMS codes in brackets after G, Navy doesn’t, etc.). So UFGS have to tailor the submittal list:

  * Army: might show (G)\[AE] codes.
  * Navy: tailor out the \[\_\_] codes entirely and instruct to use 01 33 00 for details.
  * Air Force: similar to Navy (they typically don’t use letter codes after G either).
* Provide **Notes** along with tailoring: *“NOTE: This paragraph is for Army projects only.”* placed within the ARMY tailoring tags so it’s visible to the Army editor but not to Navy/Air Force.
* **Test the output:** When updating the master, generate each tailored version (Army, Navy, AF, All) to ensure the text flows correctly for each service, with no gaps or grammatical issues.

**2.8.2 Design-Build vs. Design-Bid-Build Tailoring:**

* Some UFGS sections are used in **Design-Build (DB)** contracts (where the contractor designs certain aspects) and in **Design-Bid-Build (DBB)** (where the design is done by government A-E and contractor just builds). The spec needs to cover both scenarios via tailoring:

  * Use a **<TAI OPT=DB>** tag for text that should appear only in design-build projects.
  * Use **<TAI OPT=DBB>** for text only for design-bid-build.
  * Or use combined codes like **OPT=Army-DB**, **OPT=Navy-DBB**, etc., if the requirements vary by both service and project delivery.

* For example, a UFGS might have:

  * DB option: requiring the contractor to submit design calculations and receive Government approval (since they are doing final design).
  * DBB option: not including that requirement because the design was already provided in the plans.
  * So you’d wrap the design submittal requirement in `<TAI OPT=DB>…</TAI>`.

* **Service + DB:** The UFC gave an example list of tailoring categories for “Air Force Design-Build”, “Navy Design-Bid-Build”, etc.. This implies you can set multiple conditions. SpecsIntact tailoring can allow boolean logic (like OPT=AIR\_FORCE and OPT=DB simultaneously). In practice, this might be done by nested tags or by defining a combined option code like "AF\_DB" to use.

* Ensure to guide the editor: Provide a note in the **SUBMITTALS** article or Part 1 to tell the editor to activate DB or DBB tailoring depending on contract type. Typically, the SpecsIntact project settings allow selection of project type.

* Many UFGS have a note at the top: *“NOTE: This section is intended for Design-Bid-Build projects. For Design-Build projects, some tailoring options must be applied as noted.”* Make sure such notes are included.

* **Content differences:** Common DB vs DBB differences:

  * DB specs might include performance requirements and criteria the contractor must design to (like “The contractor’s design shall achieve a U-factor of X for walls”).
  * DBB specs might include very prescriptive requirements (since design is done, e.g., specific dimensions, etc.).
  * DB specs might have submittals like “Design Drawings, SD-02 (G)(A)” etc., which DBB would not have.
  * Where both share text, keep it outside the tailoring to avoid duplication.

* **Example from UFC text:** They mention design-build tailoring for some masters like separate options for "Air Force Design-Build" vs "Air Force Design-Bid-Build" etc., and also a generic “Use the following where requirements apply to all Services: – Design-Build – Design-Bid-Build”. This suggests sometimes you have project delivery differences that apply across the board (not service-specific). In that case, you might have an OPT=DB and OPT=DBB without specifying service. Then if it’s a DB project of any service, those DB bits appear.

* The main goal is to avoid having separate UFGS for DB vs DBB. Tailoring makes one master serve both. The project spec developer will set the appropriate toggles at project creation (in SpecsIntact they can choose project type or manually set which tailored options to include).

**2.9 Writing Style & Best Practices (UFGS-specific focus):**

*(Many style points were addressed in UFC 1.10 above, but we will apply them in UFGS context here as enumerated subpoints for completeness.)*

**2.9.1 Brackets (Optional Choices):**

* Use **square brackets \[ ]** to indicate optional text or choices that the project editor must select.

  * For **mutually exclusive choices**, list them within one set of brackets separated by a vertical bar `|` in SpecsIntact, or as separate bracketed options sequentially. However, the UFC examples show them simply as separate bracketed options next to each other (and instruct to put a space between).
  * For example: *“Provide \[galvanized steel] \[stainless steel] enclosure.”*. The designer will pick galvanized or stainless and delete the other.

* For **text that may or may not apply at all**, you can bracket the whole phrase/clause. e.g., *“Apply second coat \[if primer coat is used].”* The part “if primer coat is used” could be optional – though that example might be better as tailoring if it’s a project scenario rather than a choice.

* **Project-specific fill-ins:** Represent by five underlines within brackets \[*****]. This indicates the editor should fill something (like a value or name). For instance: \*“Compressive strength: \[*****] kPa.”\* with a note like *“Note: Insert required strength.”* The UFC explicitly says use five blank underscores for blanks.

* **Do not nest brackets** (though SpecsIntact can handle nested conditions, it’s confusing). If needing nested conditions, consider using tailoring for one layer and brackets for the other.

* **Keep bracketed text short:** Ideally just a word or short phrase. If an entire paragraph is optional, it’s better to handle it by tailoring or by instructing deletion rather than bracketing a huge block (though you can bracket multiple paragraphs in SpecsIntact by tagging them as optional).

* **Punctuation with brackets:** Include necessary punctuation inside or outside to make the resulting sentence correct:

  * If two full options are separated by nothing, ensure the one chosen yields a grammatically correct sentence. Provide a space **outside** the brackets between adjacent bracketed options. The UFC example: “Provide \[galvanized steel] \[stainless steel] enclosure” – if “galvanized steel” is chosen, there is a space before and after, it becomes “Provide galvanized steel enclosure.” Good. If they forgot the space, it might run “steelstainless” which would be wrong.
  * If the bracket is at end of sentence and optional, make sure to include or exclude the period properly. Usually, put the period outside the bracket if the whole clause is optional. E.g., *“Finish surface smooth\[.]”* – That’s not great; better restructure to avoid that scenario. Or use tailoring for an entire sentence optionality.

* **Use notes to clarify choices** if not obvious: *“**Note:** Select bracketed pipe material based on soil condition (ductile iron for aggressive soils, PVC for non-aggressive).”*

* Avoid using brackets for service differences; that’s tailoring. Brackets are for project conditions (like climate choices, finishes, etc.).

**2.9.2 Submittals (SUBMITTALS Article & Submittal Items):**

* **Listing Items:** Under the **SUBMITTALS** heading in Part 1, list all required submittals in the format **SD-## \[Submittal Description]: Item Name \[and optional classification]**. Follow UFGS 01 33 00’s guidance for submittal descriptions:

  * SD-01 Preconstruction Submittals (e.g., schedules, plans)
  * SD-02 Shop Drawings
  * SD-03 Product Data
  * SD-04 Samples
  * SD-05 Design Data (often calculations, design drawings in DB)
  * SD-06 Test Reports
  * SD-07 Certificates
  * SD-08 Manufacturer’s Instructions
  * SD-10 Operation & Maintenance Data
  * SD-11 Closeout Submittals (e.g., as-builts, warranties)
  * *Use these categories exactly; do not invent new SD numbers.*

* **Format each entry** as:

  * **SD-## \[Submittal Description]:** *Descriptive Name of the submittal item* **(Classification)**.
  * E.g.: *“SD-03 Product Data: **Pump Curve** (G)”*, meaning pump performance curve, Government approval required.
  * Or *“SD-06 Test Reports: **Concrete compressive strength results**.”* (If no G or S, it’s for information only.)
  * If multiple items under one SD category, list each as a separate bullet or line.

* **One item per item tag:** Do not combine different items on one line separated by commas. For example, do **not** do: *“SD-03 Product Data: Pumps, Valves, Controls.”* Instead break into:

  * SD-03 Product Data: **Pump**
  * SD-03 Product Data: **Valves**
  * SD-03 Product Data: **Controls**
    This ensures each can be tracked individually.

* **No explanatory text in list:** The list should just identify the item to be submitted, not the details of what it must contain or why. Explanation belongs in the relevant Part 2 or 3 text. For example, Part 3 might say “Submit test reports indicating results of each batch” – in SUBMITTALS you just put “SD-06 Test Reports: **Batch test results**.”

* **Submittal Tags in Text:** Ensure that wherever in Part 2 or 3 the requirement for the submittal is discussed, you tag it with `<SUB>` or `<ITM>` so that SpecsIntact knows to tie it to the SUBMITTALS list. In practice, in SpecsIntact you might write “<ITM><SUB>Pump Curve</SUB></ITM>” in Part 3 where pump performance is required, and that correlates to the listing “Pump Curve” under SD-03 in Part 1.

* **Unique Names:** Each submittal item name should be unique within the project spec to avoid confusion. For example, don’t have two different “Certificates” both called “Welding Certificate” in two sections – differentiate if needed by context or section, but within one section it should be clear. If an item appears in multiple sections, each section lists it separately anyway.

  * As UFC example: if “Wall Louver” appears as both a Shop Drawing and a Sample, list them distinctly (“Wall Louvers (SD-02)” vs “Wall Louver Samples (SD-04)”).

* **Government Approval (G) and Info Only:** Append **“(G)”** to a submittal item if it requires Government approval. No letter means it’s for information only (or for Contractor Quality Control). Use **“(G)”** sparingly – only for critical items that the Government must approve (as defined in 01 33 00). Many routine submittals (catalog cuts, certificates) are often “For Information Only” by default (no G).

* **Sustainability (S):** Append **“(S)”** for Sustainability submittals which relate to LEED or similar requirements. (S) items are special because they get compiled for LEED credits or SPiRiT, etc. Only use (S) if the content will be used to demonstrate compliance with sustainability mandates (like recycled content data, VOC certificates, etc.).

* **Other Codes:** If the Army uses extra codes like \[AE] after (G), include them within the item entry for Army tailoring only. For example, *“(G)\[AE]\[DO]”* might appear after an Army submittal to indicate the approving office. Ensure these are tailored out for Navy/AF (who handle via 01 33 00).

* **Submittal Procedures Coordination:** Do not specify number of copies or submission timing here – that’s handled by UFGS 01 33 00. If something unusual is needed (like a very early submittal), mention it in the execution text (e.g., “Submit mix design 60 days prior to placement” in Part 3), but still list the item simply as “Mix Design” in SUBMITTALS.

* **Double-Spacing:** The UFC says to double-space submittal items in the list for readability. That means leave one blank line between each submittal entry (and between categories). This is usually done in masters to clearly separate each item.

* **Examples:**

  ```
  SUBMITTALS:

  SD-02 Shop Drawings:
  **Layout Drawings**; plan showing equipment arrangement and clearances (G)

  SD-03 Product Data:
  **Pump**; manufacturer’s catalog sheet with performance curves (G)
  **Valves**; manufacturer’s data sheets

  SD-06 Test Reports:
  **Concrete compressive strength results** (S)
  **Welding Qualifications**; per AWS requirements

  SD-07 Certificates:
  **Installer Qualifications**; signed by Contractor (G)
  ```

  Each item here is clear and unique.

* **Submittal Content in Text:** In Part 2 or 3, describe what each submittal entails:

  * For instance, under “Quality Assurance” you might have “Installer Qualifications: Submit certification that installer meets the experience requirements of paragraph 1.5, at least 30 days before work.” This correlates to **Installer Qualifications (G)** in the list.
  * Under “Field Quality Control,” you might say “Test Reports: Submit reports of each test within 5 days of completion.” This correlates to **Test Reports: \[Name]** in the list.
  * If using SpecsIntact properly, you actually tag “Submit” statements and they generate the list, but in practice, masters usually explicitly list submittals in Part 1 for clarity and use tags in Part 2/3.

* **Submittal Coordination between Sections:** Avoid duplicating the same submittal in multiple sections. If two sections require the same thing (e.g., a certificate of compliance for a code), ideally only one should list it, or each should list only their scope. Usually, separate sections handle their own stuff. If overlap, clarify via notes.

**2.9.3 Submittal Naming & Tagging in Text:**

* As noted, give each submittal a unique descriptive name. If two items could be called “Test Report,” differentiate (e.g., “Concrete Test Reports” vs “Steel Test Reports”). The text in the section can simply say “Submit test reports” but in the list you clarify which test.
* **Tagging:** In SpecsIntact, wrap the item name in `<SUB>...</SUB>` tags in the SUBMITTALS list and in the body. The body might use `<ITM>` to tie an action to that submittal. E.g.:

  ```
  Field Quality Control:
      Perform concrete strength tests in accordance with ASTM C39. 
      <ITM><SUB>Concrete compressive strength results</SUB></ITM> shall include 
      results of all tests and statistical analysis as per ACI 301.
  ```

  This way, the submittal register will reflect that "Concrete compressive strength results" is required and tie it to “Test Reports”.
* Only place submittal tags outside the SUBMITTALS article **once per item**. Do not tag it in multiple places for the same item, except if the item appears in various contexts (rare; usually one tag in the relevant paragraph suffices).
* **Submittals outside Part 1:** Normally, just list them in Part 1 and reference in text. Don’t try to require a submittal without listing it in Part 1 – contractually it might be unenforceable if not listed. Always coordinate the two.

**2.9.4 Submittal Classifications (G, S) & Reviewers:**

* We’ve covered (G) and (S). To reiterate:

  * **(G)** = Government Approval required. Use for critical items only (e.g., design calculations, key engineering data, major equipment drawings, test plans). Overusing (G) can slow down the project and overburden the government with approvals; underusing can lead to lack of oversight on important items.
  * **No letter** (sometimes “(--)” in older format) = For Information Only (contractor must submit, but work can proceed without explicit approval).
  * **(S)** = Sustainability submittal, tracked for LEED or other goals. These often still might be approved or not, but the main point is they feed into sustainability compliance. Typically, treat (S) submittals as info (unless also marked G).
  * You can have a submittal be both (G) and (S). E.g., “Recycled Content (S)(G)” if the government wants to approve the recycled content data.
* **Submittal Reviewers (Army codes):** Only Army uses the bracketed reviewer codes after G. If including, do it like:

  * **(G)\[AE]** or **(G)\[AO]** etc., as applicable. These codes indicate who in the Army must review: AE (Architect-Engineer), DO (District Office), AO (Area Office), RO (Resident Office), PO (Project Office).
  * Each submittal might get one of these based on responsibility (this info usually comes from the Army’s submittal procedures or the spec writer’s knowledge).
  * For Navy and AF, the UFC says do not use these; the contract’s Section 01 33 00 should assign who approves if needed. So tailor them out for Navy/AF by putting those codes inside an Army-only tailoring tag.
* **Design-Build submittals (D, C, R, A):** On DB projects, especially Army, submittal classifications like **D, C, R, A** may be used:

  * D = Designer of Record Approval required (Contractor’s designer must approve before submission to Gov),
  * C = Government **Conformance** review (Gov reviews for conformity to RFP, not full approval),
  * R = Both D and C,
  * A = Both D and **Approval** by Government (a higher level, DA/GA).
  * These typically follow the submittal item: e.g., “Design Drawings (D)(C)”. They are mostly defined in the RFP or Division 01 for DB contracts. If your UFGS section is intended for DB, coordinate with UFC 1-300-07 (Design-Build procedures) or others. The UFC snippet suggests showing them in example:

    ```
    <DTE>11/09, CHG2: 8/16</DTE>   (example date tag showing revision and change)
    2-2.12.6 Design-Build Submittals for Design after Award.
      2-2.12.6.1 Army.
         ... When a "D" follows a submittal item, it indicates Designer of Record Approval (DA) is required... "C" indicates Government Conformance Review (CR)... "R" indicates both DA and CR... "A" indicates both DA and Government Approval (DA/GA)....
      2-2.12.6.2 Navy.
         For Navy only, comply with FC 1-300-09N and contract documents.
    ```
  * As a UFGS writer, you might include a paragraph in Part 1 (or in submittals notes) explaining these if the section is likely used in DB RFPs. Usually, though, DB RFPs have a separate section in Division 01 explaining these codes, and the technical sections just mark submittals as (G) or not, leaving the D/C classification to an overarching list. It depends on agency practice.
  * Keep in mind design-build specs may require the contractor to submit design info that normally wouldn’t be a submittal in DBB (since the government would have produced it). Mark those appropriately.

**2.9.5 Quality Assurance & Testing Language:** (Not a separate heading in our outline, but important writing style for specs)

* When writing **Quality Assurance (QA)** requirements in Part 1 or **Field Quality Control** in Part 3:

  * **Do not instruct government QA** (like “The Government will do XYZ test”) in the contractor’s spec section. Focus on the contractor’s responsibilities. If government QA is needed, that’s usually covered in quality requirements outside the spec or just by contract rights. For example, instead of “The Government will perform core tests,” write **“Perform core tests (by an independent lab retained by the Contractor) and submit results.”** If the Government truly will do a test, you can state it as information, e.g., “(Government may conduct independent core tests; Contractor shall patch core holes.)” but be cautious because it’s tricky territory. Often better to require contractor to do tests and Government verifies.
  * **Qualifications:** If requiring specific personnel qualifications (like certified welders, licensed electricians, etc.), state clearly and require a **Certificate submittal** to prove it. e.g., “Electrician: State-licensed journeyman. **Submit** certification of electrician’s license (SD-07).”
  * **Mock-ups & Samples:** If needed, require them under QA with details: e.g., “Construct a mock-up wall panel approximately 2m by 2m for approval of texture and color. Do not start general work until mock-up is approved (submittal: Mock-up, (G)).”
  * **Testing Standards:** If referencing test methods, use ASTM or industry standards rather than describing method fully. E.g., “Test concrete compressive strength per ASTM C39; if any 28-day strength is below design strength, take action per ACI 301.” – This references known standards. Provide acceptance criteria if not obvious from standard.
* **Warranties:** As noted earlier, avoid adding warranty beyond the standard one year unless justified and approved. If required:

  * Put warranty requirements in Part 1 as an article **WARRANTY** (or in Part 3 under “Closeout” sometimes). E.g., “Provide a written manufacturer’s warranty for roofing with 20-year coverage against leaks.” And list “Warranty (info)” in submittals if you want a copy.
  * Include any special conditions (e.g., installer must be certified by manufacturer for warranty to be valid). But ensure coordination with contract: extended warranties often require a specific contract clause or at least mention in Division 01 to be enforceable.

**2.9.6 Execution & Workmanship Language:**

* **Avoid meaningless phrases**: Instead of “install in a neat and workmanlike manner”, specify tangible outcomes: **“Install without warp or misalignment; finished work shall be clean and free of blemishes.”** Or rely on industry standard quality (e.g., painting spec can say “Apply paint to achieve a uniform color and coverage, with no visible lap marks.”).

* **“As shown on drawings”:** Don’t overuse the phrase “as shown on the drawings.” If a requirement is clearly indicated on the drawings, you can often omit it in text. If you do say it, ensure the drawings indeed show it – if not, the requirement is unenforceable. The UFC warns that if text says "as shown" and the drawing doesn’t show it, the item is not specified. So best practice: either explicitly specify in text or ensure it's on drawings, but minimize cross-reference. Usually, drawings cover layout, location, quantity, and specs cover materials, quality, installation methods.

* **Manufacturer’s Instructions:** If you want installation to follow manufacturer’s instructions (common for equipment), write **“Install per manufacturer’s published instructions.”** Do not just say “properly install” – specify that the manufacturer's guidance must be followed and perhaps require submission of those instructions (SD-08).

* **Coordination with Drawings:** Avoid duplicating dimensional info. If drawings specify dimensions or geometries, the spec can refer generally. If the spec must mention a dimension for clarity, ensure it matches the drawing or put it in brackets for the editor to confirm. It’s often enough to say “as indicated” rather than restate each dimension.

* **Specifying New or Uncommon Items:** If including a new material not widely used:

  * Provide sufficient performance criteria or test results needed to prove it.
  * If it’s an innovation, the UFC said to require evidence like “must have been tested under actual use conditions,” etc.. In spec terms, you could require “Submit documentation from at least two independent laboratories demonstrating performance of the new material under conditions similar to this project.” Or require a **mock-up or trial** usage to validate.
  * Ensure not to inadvertently sole-source a “new” material – if only one supplier exists, consider if it’s permissible or get an exemption for proprietary spec (Level One approval if needed).
  * If you suspect designers might try to include a brand name for a new tech, include guidance to avoid brand names or to allow “or equal” properly (see below).

**2.10 Prohibited & Cautionary Practices:**

*(Summarizing some do-not-do items from earlier points, as a concluding quick list of what *not* to do in UFGS writing.)*

* **Don’t include proprietary names** unless absolutely no generic alternative exists and you have approval. If you must, follow FAR 52.211-6 “Brand Name or Equal” procedures: include **“or approved equal”** and list salient characteristics. Also, add the required notice in the spec header:

  ```
  ***************************** NOTICE *****************************
  This Specification Contains Brand Name Products.
  ******************************************************************
  ```

  as shown in UFC text. And per UFC, get Level One Contracting Officer approval in writing for that brand name use.
* **Don’t repeat contract general conditions:** e.g., don’t copy safety requirements from EM 385-1-1 or FAR Clause 52.236-13 into the technical spec; just enforce results (like require compliance with safety manual, but details are in Div 01 or contract).
* **Don’t put cost or payment info** in specs. E.g., don’t say “The Government will pay separately for XYZ” – that belongs in the contract clauses or bid schedule.
* **Avoid “NIC” (Not in Contract)** notes in specs\*\*:\*\* If something is outside contract scope, it shouldn’t be described in the spec at all (or should be clearly on drawings as NIC). Better to not mention it than to mention and label NIC, to avoid confusion.
* **No instructions to government personnel** – e.g., do not write “Contracting Officer shall do X” or “Government shall furnish…”, except if listing Government-furnished materials in a **“GOVERNMENT-FURNISHED”** article. If there are Government-furnished items, list them in Part 2 or Part 3 (some sections have a Part 1 article “GOVERNMENT-FURNISHED MATERIALS” detailing what Gov provides and when – coordinate with Div 01).
* **No dollar amounts or project-specific cost implications** in spec text. (Those go in cost estimates or contract modifications, not specs).
* **Consistent Terminology:** If you call something “Equipment” in one part, don’t call it “Machine” elsewhere. Use the same term throughout to avoid ambiguity.

**2.11 Tables, Forms, and Figures (Tables and Forms in UFGS):**

**2.11.1 Formatted Tables:**

* You may include tables for clarity (especially for schedules, properties, etc.). The UFC notes any tables should fit the **portrait format** page (UFGS don’t typically use landscape orientation). If a table is too wide, consider breaking it or formatting differently.
* Table text font should match body text (not smaller than 10 pt ideally for readability).
* Use the SpecsIntact table tags or standard Word table with proper style. Include a **Table number and title** (e.g., *Table 1 – Pipe Sizes and Materials*). Refer to the table in text (“see Table 1”).
* Tables can be used to present repetitive data efficiently, e.g., “Table of Standard Symbols” as given in UFC. Use them when it improves readability.
* If a table is long and complex and maybe only needed for reference, consider if it belongs in an appendix or separate document.
* **Notes in Tables:** You can include notes below tables if needed to clarify (like “Notes: 1. All dimensions in mm. 2. \* indicates test is optional if…” etc.). That’s acceptable and often necessary.
* **Don’t duplicate drawing schedules in spec:** e.g., equipment schedules are usually on drawings. The spec should not re-list all the equipment in a table (unless the contract approach requires it). Coordinate with design team to avoid double work.

**2.11.2 External Forms, Graphics, URLs:**

* If the spec references standard forms or external documents (e.g., a safety form, or manufacturer’s data), do not embed them if not needed. Instead instruct: **“Use form XYZ (available at \[URL])”** or provide a hyperlink to WBDG or other repository.
* The UFC suggests providing instructions for designers to download forms/graphics from WBDG instead of embedding them in the spec file. For example, they mention *“UFGS Forms, Graphics, and Tables”* available on WBDG and instruct to append them to the final PDF if needed. This implies: if there’s a big figure or graphic, the spec might say, *“(Designer shall insert Figure X from WBDG library here.)”* as a note. The actual content might be too large to keep in the text file.
* **Hyperlinks:** Provide the full URL for external references in either the References section or in a footnote if appropriate. (The UFC included URLs for WBDG, ASTM, etc., in references.)
* If the contractor needs to access something online (like a government standard or database), include that URL or information in the spec (ensuring it’s a public or accessible link).

**2.12 Modifications & Approval (UFGS Maintenance Process):**

*(This is more internal for spec managers, but the UFC covers how to indicate changes and revisions within the UFGS itself.)*

* **2.12.1 Clerical Repairs:** Minor non-technical edits (typos, format fixes, reference updates) are considered *“clerical”* and aren’t recorded as official changes in the Change Log or revision history. Do not document them in the section’s Change Log or Revision List. They can be incorporated quietly. (The master should still be updated in the system, but no need for a published “Change X” for grammar fixes.)

  * SpecsIntact and UFGS managers often bundle such fixes and release as “Change 1” if more substantive changes are included, but purely clerical ones might be done at next revision.

* **2.12.2 Technical Change (Change):** A **Change** to a UFGS section is a published update addressing a specific issue or improvement. It is often triggered by a Criteria Change Request (CCR) from users.

  * Changes are limited in scope and do not overhaul the entire section. They might add a new material option, correct a requirement, update references, etc.
  * **Indicating Changes in Section Banner:** When a change is issued, the section’s title banner should note *“Change – \[number]/\[date]”*. The UFC example for a banner after changes:

    ```
    USACE / NAVFAC / AFCEC / NASA   UFGS-08 34 73 (November 2009)
                                   Change 2 – 08/16
    Preparing Activity: NASA       Superseding
                                   UFGS-08 34 73 (October 2006)
    ```

    This shows a **Change 2 in August 2016** and that it superseded an older version from 2006. The “Preparing Activity” is listed (the lead agency for that spec).
  * **Change Log (within section):** Some UFGS include a CHANGE/REVISION SUMMARY at the end or in the section notes, but often changes are tracked on WBDG. The UFC says “provide the nature of changes to Database Managers for Change List or Revision List”.
  * As writer, ensure any changed paragraphs are marked with \1\…/1/ (or appropriate change number) in the master file for review purposes (as described in UFC 1-300-01). When published, UFGS typically integrate the change without showing strikeouts; instead, the published Change bulletins on WBDG or the revision summary note what changed.

* **2.12.3 Revision:** A **Revision** in UFGS context would be a republishing of the section with a new date, possibly a new section number if MasterFormat changed.

  * Revisions incorporate all prior changes and update the **“Superseding”** line to the last version. For example, after a revision, the banner might drop the “Change” line and just show a new date. The “Superseding” line would list the old section number/date that it replaces.
  * **Superseding Section Number/Date:** If a section number itself changed (e.g., MasterFormat renumbered that spec), the banner should show the old number being superseded. Example from UFC: a section changed from 08 34 73 to 08 34 73.00 40 (added a suffix) in a revision; the banner lists the old number/date as superseded.
  * Provide a new section date tag <DTE> with new date (month/year) in the file.
  * Remove old change markers and integrate all changes.
  * Revisions likely coincide with a UFC change that triggers multiple spec updates or a periodic update cycle.

* **2.12.4 Superseding Dates:**

  * The UFC states: *“If there is a Revision to the section, change the date in the Section Header to current release month/year. The previous section number/date will become the Superseding section number/date.”* (They mean “Superseded” actually – the previous becomes the superseded one listed under Superseding line).
  * Always update the <DTE> tag in the SpecsIntact file to reflect either new revision date or latest change date as required.
  * If a section number changed due to MasterFormat updates, that is handled as a supersession (old number referenced).

* **2.12.5 UFGS Approval Process:**

  * New or revised UFGS must be coordinated tri-service. According to UFC:

    * DWG technical reps review each UFGS.
    * Solicit input from major commands, facility users, industry as appropriate (especially on big changes).
    * Preparing Activity (lead agency for that spec) coordinates changes with other agencies’ counterparts.
    * After tri-service concurrence, submit to the **Technical Proponent** (maybe the ESEP or designated lead) for final approval and signature.
    * Only after that is a UFGS change or new spec published on WBDG.
    * If an agency disagrees on a change that affects technical content, it must be resolved or at least considered – unilateral changes should be avoided because UFGS is unified.
    * The Preparing Activity is obligated to address other agencies' requests for changes.
  * *As a spec writer, be aware your changes will undergo this coordination. Use comments in draft to highlight rationales for other reviewers.*

This approval info is more for context; it’s not content in the spec itself, but understanding it ensures the spec writer follows the needed steps (like not unilaterally adding a requirement that Navy can’t implement, etc.).

---

**Conclusion:** By adhering to the above guidelines, UFC and UFGS writers will produce documents that are consistent, easy to navigate, and enforceable. The **Executive Summary** at the beginning of this document highlights the critical do’s and don’ts (use the standard format, clear language, avoid proprietary bias, etc.), while the detailed sections provide a roadmap for organizing and writing content in a way that meets DoD standards and serves the end-users (designers and contractors) effectively.
