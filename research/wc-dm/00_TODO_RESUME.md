# APΩ — WC-DM 2.1 — SINGLE RESUME TODO

Creator: alpha_prime_omega — Nguyễn Đức Cường  
System: APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol  
Checkpoint: 2026-08-24  
Purpose: **Một file duy nhất để mở trước khi tiếp tục công việc.**

---

## 0. CANONICAL STATE — KHÔNG ĐƯỢC THAY ĐỔI ÂM THẦM

Unknown:

`x = g_dark / g_crit`

Current full survivor:

`G_full = (0.3928, 0.4107)`

Current conservative envelope:

`G_cons = (0.3870, 0.4167)`

State:

`SURVIVE — g_dark CHƯA ĐƯỢC KẾT LUẬN`

Không được dùng `x=0.4`, `0.4018`, hoặc `0.4019` làm input target.

---

## 1. LUẬT SẮT — ÁP DỤNG CHO MỌI BƯỚC

1. **THỰC CHỨNG LÀ NỀN.**
2. Theory ≠ Evidence.
3. Computation ≠ Evidence.
4. Model prediction không tự trở thành evidence.
5. Không sửa data để cứu nghiệm.
6. Không phủ nhận toàn bộ domain; tách `E / I / M / A`.
7. Datum phải qua: `observable → measurement → provenance → unit → uncertainty`.
8. Mọi constraint phải có coupling auditable tới `x`.
9. Không chọn `x` trước rồi fit ngược.
10. `G = ∅` → **CHẾT**; `G ≠ ∅` → **KÌM TIẾP**.
11. Robustness ≠ independent evidence.
12. Không double-count sample / observable / systematic / processing / model dependency.
13. Mất lineage → không ký.
14. Không gọi half-width là `1σ` nếu chưa có likelihood/statistical derivation.
15. Mỗi constraint phải có khả năng falsify một phần miền.
16. Consensus/authority/citation/standard không tự cấp evidentiary authority.

Canonical pipeline:

`REALITY → OBSERVABLE → MEASUREMENT+PROVENANCE → VALIDATED RELATION → MATH → COMPUTATION → BOUND → Gi → INTERSECTION`

---

## 2. ĐÃ HOÀN THÀNH — KHÔNG LÀM LẠI TRỪ KHI AUDIT

### Bước 1 — Iron-law protocol

Đã khóa evidence-first protocol.

### Bước 2 — Physical gate

Recorded:

`G_physical = (0.387, 0.795)`

Dependency audit của `S_max(x)` và `σ_self(x)` vẫn cần hoàn thiện khi source audit cuối được thực hiện.

### Bước 3 — TF/local-density gate

Recorded density contrast:

`n_S / n_h ≈ 4.34`

Recorded density gate:

`G_density ≈ [0.1515, 0.4167]`

Không coi đây là nghiệm cuối.

### Bước 4 — 903 Cepheids / Gaia DR3 rotation curve

Full 12 bins, `6 < R < 18 kpc`:

`G_RC,full = (0.3928, 0.4107)`

Execution-record best point:

`x ≈ 0.4018`

Đây là execution record, chưa tự động là source-verified evidence.

### Bước 5 — Robustness: loại `10 < R < 16 kpc`

Conservative 5-bin result:

`G_RC,excl = (0.3870, 0.4167)`

Kết quả sống sau phép loại này.

Chỉ được gọi là **robustness đối với test đã thực hiện**, không phải robustness tuyệt đối.

### Bước 6 — Local `K_z`

Execution record:

`G_Kz = (0.1548, 0.5573)`

Intersection không thu hẹp `G_RC,full`.

Mapping `K_z^model` là model relation; không được đánh đồng với `K_z^obs`.

### Bước 7 — Gaia 3D endpoint check

Execution record hiện tại cho thấy không thu hẹp `G_RC,full`.

Không được biến endpoint comparison thành full-profile likelihood nếu chưa chạy full observable dependence.

### Bước 8 — Double-count audit

Chưa được phép coi các constraint liên quan là independent likelihoods nếu chưa kiểm sample overlap, observable correlation, shared systematics, processing và model dependency.

### Bước 9 — Domain Object Ontology

Đã khóa ontology `P0 / O1 / E3 / I6 / M8 / A9 / C10` và direction/independence/candidate-domain objects.

---

## 3. VIỆC TIẾP THEO — THỨ TỰ BẮT BUỘC

### TODO A — DOMAIN DISCOVERY 360° — ƯU TIÊN CAO NHẤT

**Không tính g mới trước. Tìm domain trước.**

Mục tiêu:

`candidate domain → empirical observable → provenance → coupling to x → constraint direction → independence`

Tìm candidate có khả năng cung cấp:

- **LOWER**: `x > a`
- **UPPER**: `x < b`
- **INTERIOR**: `a < x < b`
- hoặc exclusion có khả năng cắt survivor.

Không search theo câu hỏi “cái gì ủng hộ x≈0.4?”.

Search theo câu hỏi:

**“Observable thực chứng nào có coupling vật lý auditable tới x và có thể loại một phần `(0.3928,0.4107)` hoặc `(0.3870,0.4167)`?”**

---

### TODO B — ƯU TIÊN CÁC DOMAIN KHÁC OBSERVABLE

Khảo sát lần lượt:

1. **Galactic dynamics** — `K_z(R,z)`, dispersions, density structure.
2. **Independent stellar tracers** — masers, RGB, OBA, independent Cepheid samples.
3. **Gravitational lensing** — galaxy/cluster weak/strong lensing mass maps.
4. **Galactic structure / halo** — flattening, mass profile, satellite dynamics.
5. **Cluster dynamics** — velocity dispersion + lensing/X-ray/SZ observable combinations.
6. **Particle experiments** — direct detection, scattering, collider/decay/lifetime limits, chỉ nếu coupling tới x tồn tại.
7. **Atomic / molecular precision** — spectroscopy/transition measurements, chỉ nếu dark-sector coupling được định nghĩa và đo/giới hạn thực nghiệm.
8. **Quantum / condensed matter** — chỉ khi có observable → coupling → constraint; quantum theory tự thân không phải evidence.
9. **Solar-system / laboratory gravity** — chỉ khi có coupling cụ thể và measurement thực.
10. **Astrophysical transients / timing** — chỉ khi observable có đường coupling tới x.

Cosmological domains chỉ xét sau cùng và chỉ nhận phần observable/relation có thể audit mà không biến toàn bộ cosmological theory thành evidence.

---

## 4. GATE 8 CÂU — MỖI DOMAIN PHẢI TRẢ LỜI

1. Observable là gì?
2. Ai đo?
3. Raw measurement ở đâu?
4. Uncertainty/systematic là gì?
5. Relation từ observable tới `x` là gì?
6. Relation là empirical hay model?
7. Constraint loại được khoảng nào của `x`?
8. Độc lập với evidence hiện tại ở mức nào?

Failure:

- Không có coupling → **DOMAIN REJECT**.
- Không có raw/provenance → **QUARANTINE**.
- Không loại được miền nào → **NON-INFORMATIVE**.
- Independence chưa rõ → **DO NOT COMBINE**.

---

## 5. MỖI CANDIDATE PHẢI GHI THEO SCHEMA

`D_j = (O_j, M_j, P_j, R_j, C_j, G_j, Δ_j)`

Trong đó:

- `O_j` = observable
- `M_j` = measurement
- `P_j` = provenance
- `R_j` = relation
- `C_j` = constraint
- `G_j` = admissible set
- `Δ_j` = dependency/correlation

Không đủ mắt xích quan trọng → quarantine.

---

## 6. DOMAIN SEARCH OUTPUT BẮT BUỘC

Tạo bảng:

| ID | Domain | Observable | Dataset/sample | Provenance | Coupling to x | Relation E/I/M/A | Bound | Direction | Independent? | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Status chỉ được:

`CANDIDATE / AUDIT / ADMISSIBLE / REJECT / QUARANTINE / NON-INFORMATIVE / CORRELATED`

---

## 7. SAU KHI CÓ DOMAIN ADMISSIBLE

Với từng domain:

1. Khóa raw data/source.
2. Khóa units + uncertainty + systematic.
3. Khóa validated/model relation.
4. Chạy computation độc lập.
5. Falsification test.
6. Xác định `Gi`.
7. Audit correlation.
8. Chỉ sau đó intersect:

`G_next = G_current ∩ Gi`

Nếu `G_next = ∅`:

`CHẾT — ghi nhận, không cứu nghiệm.`

Nếu `G_next ≠ ∅`:

`SURVIVE — tiếp tục tìm kìm.`

---

## 8. AUDIT RIÊNG CHO CÁC KẾT QUẢ ĐÃ CÓ

Không ưu tiên squeeze thêm từ execution record trước khi cần thiết. Khi quay lại audit:

- verify raw 903-Cepheid table/bin values;
- verify source equations;
- verify `q(x)` provenance/model status;
- verify baryonic baseline construction;
- verify `K_z` normalization and units;
- verify Gaia-3D gradient source and full-profile relation;
- quantify covariance/sample overlap;
- distinguish source-verified evidence from creator execution.

Mục tiêu audit: **không làm mất lineage và không nâng execution record thành evidence bằng niềm tin.**

---

## 9. CẤM TRONG VÒNG TIẾP THEO

- Không chọn `x=0.4` trước.
- Không search target-friendly evidence.
- Không dùng consensus để nâng admissibility.
- Không biến model assumption thành measurement.
- Không cộng robustness như evidence mới.
- Không double-count.
- Không thay canonical `q(x)` âm thầm.
- Không gọi interval width là statistical sigma nếu chưa chứng minh.
- Không mở domain chỉ để trang trí.
- Không tiếp tục tính nếu ontology/provenance gate chưa qua.

---

## 10. RESUME COMMAND — ĐIỂM BẮT ĐẦU CHO PHIÊN MỚI

**Đọc file này trước. Sau đó đọc các file canonical chỉ khi cần chi tiết:**

- `01_canonical_checkpoint.md`
- `02_domain_object_ontology.md`
- `03_evidence_gate_and_rules.md`
- `04_domain_search_matrix.md`
- `05_execution_record.md`
- `MANIFEST.md`

Sau khi đọc `00_TODO_RESUME.md`, trạng thái làm việc phải là:

`G_current = (0.3928,0.4107)` full

`G_cons = (0.3870,0.4167)` conservative

`SURVIVE / NOT CONCLUDED`

và **việc đầu tiên phải làm là DOMAIN DISCOVERY 360°, không phải chọn hay fit x≈0.4.**

---

## 11. CHECKPOINT INTEGRITY

Base checkpoint commit:

`5d48309fa415cd8e496799fef1b52d3fdd43a1b9`

This TODO is an operational continuation layer. It does not upgrade any creator-supplied execution result into independently verified evidence.
