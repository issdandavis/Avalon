#!/usr/bin/env python3
"""
Test script to validate all agent system components
Checks that all scripts, workflows, and dependencies are properly configured
"""

import os
import sys
import subprocess
from pathlib import Path
import json

class AgentSystemTester:
    """Tests the entire agent management system"""
    
    def __init__(self):
        self.repo_root = Path(__file__).parent.parent.parent
        self.scripts_dir = self.repo_root / ".github" / "scripts"
        self.workflows_dir = self.repo_root / ".github" / "workflows"
        self.results = {
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'tests': []
        }
    
    def run_test(self, name, test_func):
        """Run a test and record results"""
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print('='*60)
        
        try:
            result = test_func()
            if result.get('status') == 'pass':
                print(f"✅ PASS: {result.get('message', '')}")
                self.results['passed'] += 1
            elif result.get('status') == 'warning':
                print(f"⚠️ WARNING: {result.get('message', '')}")
                self.results['warnings'] += 1
            else:
                print(f"❌ FAIL: {result.get('message', '')}")
                self.results['failed'] += 1
            
            self.results['tests'].append({
                'name': name,
                'status': result.get('status', 'unknown'),
                'message': result.get('message', ''),
                'details': result.get('details', {})
            })
            
            return result
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            self.results['failed'] += 1
            self.results['tests'].append({
                'name': name,
                'status': 'error',
                'message': str(e)
            })
            return {'status': 'error', 'message': str(e)}
    
    def test_python_scripts_exist(self):
        """Check that all required Python scripts exist"""
        required_scripts = [
            'agent_orchestrator.py',
            'scene_writer_agent.py',
            'content_polisher.py',
            'ai_autonomous_worker.py',
            'stat_analyzer.py',
            'validate_choicescript.py',
            'find_dead_ends.py',
            'auto_reviewer.py',
            'auto_fixer.py',
            'auto_merger.py',
            'conflict_resolver.py'
        ]
        
        missing = []
        for script in required_scripts:
            script_path = self.scripts_dir / script
            if not script_path.exists():
                missing.append(script)
            else:
                print(f"  ✓ {script}")
        
        if missing:
            return {
                'status': 'fail',
                'message': f'Missing scripts: {", ".join(missing)}',
                'details': {'missing': missing}
            }
        
        return {
            'status': 'pass',
            'message': f'All {len(required_scripts)} required scripts exist',
            'details': {'count': len(required_scripts)}
        }
    
    def test_scripts_executable(self):
        """Check that Python scripts have proper imports and basic syntax"""
        scripts_to_test = [
            'agent_orchestrator.py',
            'stat_analyzer.py',
            'validate_choicescript.py',
            'find_dead_ends.py',
            'conflict_resolver.py'
        ]
        
        errors = []
        for script in scripts_to_test:
            script_path = self.scripts_dir / script
            try:
                # Try to compile the script
                with open(script_path, 'r') as f:
                    compile(f.read(), script_path, 'exec')
                print(f"  ✓ {script} - syntax OK")
            except SyntaxError as e:
                errors.append(f"{script}: {e}")
                print(f"  ✗ {script} - syntax error: {e}")
        
        if errors:
            return {
                'status': 'fail',
                'message': f'{len(errors)} scripts have syntax errors',
                'details': {'errors': errors}
            }
        
        return {
            'status': 'pass',
            'message': f'All {len(scripts_to_test)} scripts have valid syntax'
        }
    
    def test_workflows_exist(self):
        """Check that all required workflow files exist"""
        required_workflows = [
            'agent-management.yml',
            'ai-scene-writer.yml',
            'ai-content-polish.yml',
            'ai-stat-balancer.yml',
            'ai-autonomous-worker.yml',
            'ai-game-tester.yml'
        ]
        
        missing = []
        for workflow in required_workflows:
            workflow_path = self.workflows_dir / workflow
            if not workflow_path.exists():
                missing.append(workflow)
            else:
                print(f"  ✓ {workflow}")
        
        if missing:
            return {
                'status': 'fail',
                'message': f'Missing workflows: {", ".join(missing)}',
                'details': {'missing': missing}
            }
        
        return {
            'status': 'pass',
            'message': f'All {len(required_workflows)} required workflows exist'
        }
    
    def test_required_directories(self):
        """Check that required directories exist"""
        required_dirs = [
            'docs',
            'choicescript_game/scenes',
            'logs/agent-management',
            'config',
            '.github/scripts',
            '.github/workflows',
            '.github/agents'
        ]
        
        missing = []
        for dir_path in required_dirs:
            full_path = self.repo_root / dir_path
            if not full_path.exists():
                missing.append(dir_path)
                print(f"  ✗ {dir_path} - missing")
            else:
                print(f"  ✓ {dir_path}")
        
        if missing:
            return {
                'status': 'warning',
                'message': f'Some directories missing: {", ".join(missing)}',
                'details': {'missing': missing}
            }
        
        return {
            'status': 'pass',
            'message': 'All required directories exist'
        }
    
    def test_config_files(self):
        """Check that configuration files exist and are valid"""
        config_files = {
            'config/automation-settings.json': 'json',
            'docs/AI_TASK_QUEUE.md': 'markdown',
            'docs/AI_WORKER_RULES.md': 'markdown',
        }
        
        issues = []
        for config_path, file_type in config_files.items():
            full_path = self.repo_root / config_path
            if not full_path.exists():
                issues.append(f"{config_path} - missing")
                print(f"  ✗ {config_path} - missing")
                continue
            
            # Validate JSON files
            if file_type == 'json':
                try:
                    with open(full_path, 'r') as f:
                        json.load(f)
                    print(f"  ✓ {config_path} - valid JSON")
                except json.JSONDecodeError as e:
                    issues.append(f"{config_path} - invalid JSON: {e}")
                    print(f"  ✗ {config_path} - invalid JSON")
            else:
                print(f"  ✓ {config_path} - exists")
        
        if issues:
            return {
                'status': 'warning',
                'message': f'{len(issues)} configuration issues',
                'details': {'issues': issues}
            }
        
        return {
            'status': 'pass',
            'message': 'All configuration files valid'
        }
    
    def test_orchestrator_runs(self):
        """Test that the agent orchestrator can execute"""
        try:
            result = subprocess.run(
                ['python', str(self.scripts_dir / 'agent_orchestrator.py')],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Orchestrator may exit with 1 if health is low, that's OK
            if result.returncode in [0, 1]:
                print(f"  ✓ Orchestrator executed successfully")
                print(f"  Exit code: {result.returncode}")
                return {
                    'status': 'pass',
                    'message': 'Agent orchestrator runs successfully',
                    'details': {'exit_code': result.returncode}
                }
            else:
                return {
                    'status': 'fail',
                    'message': f'Orchestrator failed with exit code {result.returncode}',
                    'details': {
                        'exit_code': result.returncode,
                        'stderr': result.stderr[:500]
                    }
                }
        except subprocess.TimeoutExpired:
            return {
                'status': 'fail',
                'message': 'Orchestrator timed out after 30 seconds'
            }
        except Exception as e:
            return {
                'status': 'fail',
                'message': f'Failed to run orchestrator: {str(e)}'
            }
    
    def test_validator_runs(self):
        """Test that the ChoiceScript validator can execute"""
        try:
            result = subprocess.run(
                ['python', str(self.scripts_dir / 'validate_choicescript.py')],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"  ✓ Validator executed successfully")
                return {
                    'status': 'pass',
                    'message': 'ChoiceScript validator runs successfully'
                }
            else:
                return {
                    'status': 'warning',
                    'message': f'Validator exited with code {result.returncode} (may be expected)',
                    'details': {'exit_code': result.returncode}
                }
        except Exception as e:
            return {
                'status': 'fail',
                'message': f'Failed to run validator: {str(e)}'
            }
    
    def test_api_dependent_scripts(self):
        """Test that API-dependent scripts have proper error handling"""
        api_scripts = [
            'scene_writer_agent.py',
            'content_polisher.py',
            'ai_autonomous_worker.py'
        ]
        
        issues = []
        for script in api_scripts:
            try:
                result = subprocess.run(
                    ['python', str(self.scripts_dir / script)],
                    cwd=self.repo_root,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                # These should exit gracefully with helpful error messages
                # when ANTHROPIC_API_KEY is not set
                if 'anthropic package not installed' in result.stdout or \
                   'ANTHROPIC_API_KEY' in result.stdout:
                    print(f"  ✓ {script} - graceful error handling")
                else:
                    issues.append(f"{script} - unexpected output")
                    print(f"  ✗ {script} - unexpected behavior")
                    
            except Exception as e:
                issues.append(f"{script} - {str(e)}")
                print(f"  ✗ {script} - error: {e}")
        
        if issues:
            return {
                'status': 'warning',
                'message': 'Some API scripts may not handle missing dependencies well',
                'details': {'issues': issues}
            }
        
        return {
            'status': 'pass',
            'message': 'All API-dependent scripts have proper error handling'
        }
    
    def generate_report(self):
        """Generate final test report"""
        print("\n" + "="*60)
        print("AGENT SYSTEM TEST SUMMARY")
        print("="*60)
        
        total_tests = self.results['passed'] + self.results['failed'] + self.results['warnings']
        print(f"\nTotal Tests: {total_tests}")
        print(f"✅ Passed: {self.results['passed']}")
        print(f"⚠️ Warnings: {self.results['warnings']}")
        print(f"❌ Failed: {self.results['failed']}")
        
        # Calculate health score
        health_score = 0
        if total_tests > 0:
            health_score = int((self.results['passed'] + self.results['warnings'] * 0.5) / total_tests * 100)
        
        print(f"\n📊 System Health: {health_score}/100")
        
        # Status
        if self.results['failed'] == 0:
            print("\n✅ SYSTEM STATUS: All critical tests passed")
            exit_code = 0
        elif self.results['failed'] <= 2:
            print("\n⚠️ SYSTEM STATUS: Minor issues detected")
            exit_code = 1
        else:
            print("\n❌ SYSTEM STATUS: Critical issues require attention")
            exit_code = 2
        
        # Save detailed report
        report_path = self.repo_root / "logs" / "agent-management" / "test-report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: {report_path}")
        
        return exit_code
    
    def run_all_tests(self):
        """Run all test suites"""
        print("🎯 Agent System Validation Test Suite")
        print("Testing all components of the Avalon AI agent system...\n")
        
        # Core component tests
        self.run_test("Python Scripts Exist", self.test_python_scripts_exist)
        self.run_test("Script Syntax Valid", self.test_scripts_executable)
        self.run_test("Workflows Exist", self.test_workflows_exist)
        self.run_test("Required Directories", self.test_required_directories)
        self.run_test("Configuration Files", self.test_config_files)
        
        # Execution tests
        self.run_test("Agent Orchestrator", self.test_orchestrator_runs)
        self.run_test("ChoiceScript Validator", self.test_validator_runs)
        self.run_test("API-Dependent Scripts", self.test_api_dependent_scripts)
        
        # Generate final report
        return self.generate_report()

if __name__ == "__main__":
    tester = AgentSystemTester()
    exit_code = tester.run_all_tests()
    sys.exit(exit_code)
