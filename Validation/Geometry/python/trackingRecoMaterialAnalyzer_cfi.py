import FWCore.ParameterSet.Config as cms
materialDumperAnalyzer = cms.EDAnalyzer("TrackingRecoMaterialAnalyser",
                                        folder = cms.string('Tracking/RecoMaterial/'),
                                        tracks = cms.InputTag("generalTracks"),
                                        beamspot = cms.InputTag("offlineBeamSpot"),
                                        usePV = cms.bool(False),
                                        vertices = cms.InputTag("offlinePrimaryVertices"),
                                        DoPredictionsOnly = cms.bool(False),
                                        Fitter = cms.string('KFFitterForRefitInsideOut'),
                                        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
                                        Smoother = cms.string('KFSmootherForRefitInsideOut'),
                                        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
                                        RefitDirection = cms.string('alongMomentum'),
                                        RefitRPCHits = cms.bool(True),
                                        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
                                        #Propagators
                                        PropagatorAlong = cms.string("RungeKuttaTrackerPropagator"),
                                        PropagatorOpposite = cms.string("RungeKuttaTrackerPropagatorOpposite")
)

materialDumper = cms.Sequence(materialDumperAnalyzer)
materialDumper_step = cms.Path(materialDumper)

