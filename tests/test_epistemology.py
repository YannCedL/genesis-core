# basic tests for the models
"""
Unit tests for genesis_core epistemology and result contract.
"""

from genesis_core.epistemology import EpistemicStatus, Evidence, ResultContract
from genesis_core.provenance import Provenance
from genesis_core.temporal import TemporalValidity
from genesis_core.contradiction import Claim, PreservedContradiction

def test_result_contract_structure():
    contract = ResultContract(
        result={"company_name": "Airbus SE", "siren": "383474814"},
        confidence=0.95,
        engine_version="1.0.0"
    )
    ev = Evidence(
        subject="Airbus SE",
        predicate="siren",
        value="383474814",
        source="INSEE SIRENE API",
        observed_at="2026-06-24T10:00:00Z",
        confidence=1.0,
        status=EpistemicStatus.FACT
    )
    contract.add_evidence(ev)
    
    assert contract.confidence == 0.95
    assert len(contract.evidence) == 1
    assert contract.evidence[0].status == EpistemicStatus.FACT
    assert "INSEE SIRENE API" in contract.sources

def test_preserved_contradiction():
    c1 = Claim(
        claim_id="c1",
        subject="EntityX",
        predicate="headquarters",
        value="Paris",
        source="SourceA",
        timestamp="2026-06-24T10:00:00Z",
        status=EpistemicStatus.OBSERVATION
    )
    c2 = Claim(
        claim_id="c2",
        subject="EntityX",
        predicate="headquarters",
        value="Toulouse",
        source="SourceB",
        timestamp="2026-06-24T11:00:00Z",
        status=EpistemicStatus.OBSERVATION
    )
    contra = PreservedContradiction(
        contradiction_id="contra_01",
        subject="EntityX",
        predicate="headquarters",
        claims=[c1, c2]
    )
    assert len(contra.claims) == 2
    assert contra.resolved is False

